from flask import Flask, request, jsonify
from query_engine import generate_insights
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, Any
import datetime
import traceback

app = Flask(__name__)

# Path to store user interactions
LOG_FILE = "backend/user_engagement_log.json"


def save_user_interaction(query: str, response: Dict[str, Any], brs: float, rcs: float, analysis_type: str):
    """Logs user queries and response scores."""
    log_entry = {
        "query": query,
        "response": response,
        "BRS": brs,
        "RCS": rcs,
        "analysis_type": analysis_type,
        "timestamp": str(datetime.datetime.now())
    }

    # Create the log file if it doesn't exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []  # Reset logs if file is corrupted

    logs.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)


def calculate_business_relevance(query: str, response: Dict[str, Any]) -> float:
    """
    Computes Business Relevance Score (BRS) using TF-IDF similarity.
    Considers all relevant sections of the response.
    """
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        
        # Combine relevant sections based on response type
        if "market_position" in response:
            # Competitive analysis
            text_to_analyze = f"{response['market_position']} {' '.join(response['competitor_analysis'])}"
        elif "current_trends" in response:
            # Trend analysis
            text_to_analyze = f"{' '.join(response['current_trends'])} {' '.join(response['predictions'])}"
        else:
            # General analysis
            text_to_analyze = f"{response['summary']} {' '.join(response['key_points'])}"
        
        vectors = vectorizer.fit_transform([query, text_to_analyze])
        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        return round(similarity * 100, 2)  # Convert to percentage
    except Exception as e:
        print(f"Error calculating BRS: {str(e)}")
        return 0


def calculate_response_consistency(response: Dict[str, Any], analysis_type: str) -> float:
    """
    Evaluates Response Consistency Score (RCS) based on required sections.
    """
    if analysis_type == "competitive":
        required_sections = ["market_position", "competitor_analysis", "differentiators", "opportunities", "threats"]
    elif analysis_type == "trend":
        required_sections = ["current_trends", "predictions", "opportunities", "risks", "measures"]
    else:
        required_sections = ["summary", "key_points", "recommendations", "timeline", "outcomes"]
    
    missing_sections = sum(1 for section in required_sections if not response.get(section))
    return {0: 100, 1: 80, 2: 60, 3: 40, 4: 20, 5: 0}.get(missing_sections, 0)


@app.route('/generate-insights', methods=['POST'])
def get_insights():
    """Handles user queries and returns AI-generated business insights with scores."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        query = data.get("query", "").strip()
        if not query:
            return jsonify({"error": "No query provided"}), 400

        analysis_type = data.get("analysis_type", "general")
        if analysis_type not in ["competitive", "trend", "general"]:
            return jsonify({"error": "Invalid analysis type"}), 400

        # Generate AI insights
        response = generate_insights(query, analysis_type)
        
        # Check for error in response
        if "error" in response:
            return jsonify({"error": response["error"]}), 500

        # Evaluate response
        brs = calculate_business_relevance(query, response)
        rcs = calculate_response_consistency(response, analysis_type)

        # Log user engagement
        save_user_interaction(query, response, brs, rcs, analysis_type)

        return jsonify({
            "status": "success",
            "query": query,
            "analysis_type": analysis_type,
            "insights": response,
            "BRS": brs,
            "RCS": rcs
        })

    except Exception as e:
        error_trace = traceback.format_exc()
        print(f"Error in get_insights: {str(e)}\n{error_trace}")
        return jsonify({
            "error": f"An error occurred: {str(e)}",
            "details": error_trace
        }), 500


@app.route('/analysis-types', methods=['GET'])
def get_analysis_types():
    """Returns available analysis types and their descriptions."""
    return jsonify({
        "analysis_types": [
            {
                "id": "competitive",
                "name": "Competitive Analysis",
                "description": "Analyzes market position, competitors, and strategic differentiators"
            },
            {
                "id": "trend",
                "name": "Trend Analysis",
                "description": "Analyzes current trends, future predictions, and growth opportunities"
            },
            {
                "id": "general",
                "name": "General Business Analysis",
                "description": "Provides comprehensive business insights and recommendations"
            }
        ]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
