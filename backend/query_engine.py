import google.generativeai as genai
import os
from typing import Dict, List, Optional

# Load API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set! Please check your .env file.")

# Configure Gemini API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    raise ValueError(f"Failed to configure Gemini API: {str(e)}")

def generate_insights(user_query: str, analysis_type: Optional[str] = None) -> Dict:
    """
    Generates business insights based on the given user query.
    Uses Google's Gemini AI to provide structured insights.
    
    Args:
        user_query: The business query to analyze
        analysis_type: Optional type of analysis (competitive, trend, general)
    """
    print(f"🔍 Generating insights for query: {user_query}")

    # Enhanced prompt engineering based on analysis type
    base_prompt = (
        "You are an expert Business Intelligence AI Assistant specializing in strategic decision-making. "
        "Your task is to analyze the following business query and provide comprehensive, actionable insights."
    )

    if analysis_type == "competitive":
        prompt = (
            f"{base_prompt}\n\n"
            f"Focus on competitive analysis by providing:\n"
            f"1. 📊 Market Position Analysis\n"
            f"2. 🔍 Competitor Strengths and Weaknesses\n"
            f"3. 💡 Strategic Differentiators\n"
            f"4. 🎯 Market Opportunities\n"
            f"5. ⚠️ Potential Threats\n\n"
            f"Query: {user_query}"
        )
    elif analysis_type == "trend":
        prompt = (
            f"{base_prompt}\n\n"
            f"Focus on trend analysis by providing:\n"
            f"1. 📈 Current Market Trends\n"
            f"2. 🔮 Future Predictions\n"
            f"3. 🎯 Growth Opportunities\n"
            f"4. ⚠️ Risk Factors\n"
            f"5. 💡 Proactive Measures\n\n"
            f"Query: {user_query}"
        )
    else:
        prompt = (
            f"{base_prompt}\n\n"
            f"Provide a structured response including:\n"
            f"1. 📊 Business Insights\n"
            f"2. 🔑 Key Strategic Points\n"
            f"3. ✅ Actionable Recommendations\n"
            f"4. 📈 Implementation Timeline\n"
            f"5. 📊 Expected Outcomes\n\n"
            f"Query: {user_query}"
        )

    try:
        # Select the best available model
        try:
            available_models = [model.name.replace("models/", "") for model in genai.list_models()]
            print(f"Available models: {available_models}")  # Debug log
        except Exception as e:
            raise ValueError(f"Failed to list available models: {str(e)}")

        selected_model = None
        # Try to use the latest available model in order of preference
        for model_name in [
            "gemini-2.5-pro-exp-03-25",
            "gemini-2.0-pro-exp",
            "gemini-1.5-pro-latest",
            "gemini-1.5-pro",
            "gemini-1.5-pro-002",
            "gemini-1.5-pro-001"
        ]:
            if model_name in available_models:
                selected_model = f"models/{model_name}"
                print(f"Selected model: {selected_model}")  # Debug log
                break

        if not selected_model:
            return {"error": "No valid Gemini model found! Available models: " + ", ".join(available_models)}

        # Generate response using the selected model
        try:
            model = genai.GenerativeModel(selected_model)
            response = model.generate_content(prompt)
        except Exception as e:
            raise ValueError(f"Failed to generate content: {str(e)}")

        if response and response.text:
            structured_response = format_response(response.text, analysis_type)
            return structured_response
        else:
            return {"error": "No response generated from the model"}

    except Exception as e:
        print(f"❌ Error generating response: {str(e)}")
        return {"error": f"Error generating response: {str(e)}"}

def format_response(response_text: str, analysis_type: Optional[str] = None) -> Dict:
    """
    Formats the AI response into a structured dictionary based on analysis type.
    """
    if analysis_type == "competitive":
        sections = {
            "market_position": "",
            "competitor_analysis": [],
            "differentiators": [],
            "opportunities": [],
            "threats": []
        }
        
        # Parse competitive analysis sections
        current_section = "market_position"
        for line in response_text.split("\n"):
            line = line.strip()
            if not line:
                continue
                
            if "📊 Market Position Analysis:" in line:
                current_section = "market_position"
                continue
            elif "🔍 Competitor Strengths and Weaknesses:" in line:
                current_section = "competitor_analysis"
                continue
            elif "💡 Strategic Differentiators:" in line:
                current_section = "differentiators"
                continue
            elif "🎯 Market Opportunities:" in line:
                current_section = "opportunities"
                continue
            elif "⚠️ Potential Threats:" in line:
                current_section = "threats"
                continue
                
            if current_section == "market_position":
                sections[current_section] += line + "\n"
            else:
                # Remove bullet points and clean up the line
                line = line.lstrip("•-* ")
                if line:
                    sections[current_section].append(line)
    
    elif analysis_type == "trend":
        sections = {
            "current_trends": [],
            "predictions": [],
            "opportunities": [],
            "risks": [],
            "measures": []
        }
        
        # Parse trend analysis sections
        current_section = "current_trends"
        for line in response_text.split("\n"):
            line = line.strip()
            if not line:
                continue
                
            if "📈 Current Market Trends:" in line:
                current_section = "current_trends"
                continue
            elif "🔮 Future Predictions:" in line:
                current_section = "predictions"
                continue
            elif "🎯 Growth Opportunities:" in line:
                current_section = "opportunities"
                continue
            elif "⚠️ Risk Factors:" in line:
                current_section = "risks"
                continue
            elif "💡 Proactive Measures:" in line:
                current_section = "measures"
                continue
                
            # Remove bullet points and clean up the line
            line = line.lstrip("•-* ")
            if line:
                sections[current_section].append(line)
    
    else:  # general analysis
        sections = {
            "summary": "",
            "key_points": [],
            "recommendations": [],
            "timeline": [],
            "outcomes": []
        }
        
        # Parse general analysis sections
        current_section = "summary"
        for line in response_text.split("\n"):
            line = line.strip()
            if not line:
                continue
                
            if "📊 Business Insights:" in line:
                current_section = "summary"
                continue
            elif "🔑 Key Strategic Points:" in line:
                current_section = "key_points"
                continue
            elif "✅ Actionable Recommendations:" in line:
                current_section = "recommendations"
                continue
            elif "📈 Implementation Timeline:" in line:
                current_section = "timeline"
                continue
            elif "📊 Expected Outcomes:" in line:
                current_section = "outcomes"
                continue
                
            if current_section == "summary":
                # Clean up the line and add to summary
                line = line.lstrip("•-* ")
                if line:
                    sections[current_section] += line + "\n"
            else:
                # Remove bullet points and clean up the line
                line = line.lstrip("•-* ")
                if line:
                    sections[current_section].append(line)

    # Clean up empty sections
    for section in sections:
        if isinstance(sections[section], list):
            sections[section] = [item for item in sections[section] if item]
        elif isinstance(sections[section], str):
            sections[section] = sections[section].strip()

    return sections
