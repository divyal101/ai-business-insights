"""
AI-powered query engine for business insights generation.
"""

import google.generativeai as genai
import os
import re
from typing import Dict, List, Optional, Any

# Load API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set! Please check your .env file.")

# Configure Gemini API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    raise ValueError(f"Failed to configure Gemini API: {str(e)}")

def generate_insights(user_query: str, analysis_type: Optional[str] = None) -> Dict[str, Any]:
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

def format_response(response_text: str, analysis_type: Optional[str] = None) -> Dict[str, Any]:
    """
    Format the AI response into a structured dictionary based on analysis type.
    
    Args:
        response_text (str): Raw response text from the AI model
        analysis_type (Optional[str]): Type of analysis ('general', 'competitive', or 'trend')
        
    Returns:
        Dict[str, Any]: Formatted response with structured sections
    """
    formatted_response = {}
    
    if analysis_type == "general":
        # Extract sections for general analysis
        formatted_response["summary"] = extract_section(response_text, "Business Insights")
        formatted_response["key_points"] = extract_section(response_text, "Key Strategic Points")
        formatted_response["recommendations"] = extract_section(response_text, "Actionable Recommendations")
        formatted_response["timeline"] = extract_section(response_text, "Implementation Timeline")
        formatted_response["outcomes"] = extract_section(response_text, "Expected Outcomes")
        
    elif analysis_type == "competitive":
        # Extract sections for competitive analysis
        formatted_response["market_position"] = extract_section(response_text, "Market Position Analysis")
        formatted_response["competitor_analysis"] = extract_section(response_text, "Competitor Strengths and Weaknesses")
        formatted_response["differentiators"] = extract_section(response_text, "Strategic Differentiators")
        formatted_response["opportunities"] = extract_section(response_text, "Market Opportunities")
        formatted_response["threats"] = extract_section(response_text, "Potential Threats")
        
    elif analysis_type == "trend":
        # Extract sections for trend analysis
        formatted_response["current_trends"] = extract_section(response_text, "Current Market Trends")
        formatted_response["predictions"] = extract_section(response_text, "Future Predictions")
        formatted_response["opportunities"] = extract_section(response_text, "Growth Opportunities")
        formatted_response["risks"] = extract_section(response_text, "Risk Factors")
        formatted_response["measures"] = extract_section(response_text, "Proactive Measures")
    
    return formatted_response

def extract_section(text: str, section_name: str) -> str:
    """
    Extract content between section headers in the response.
    
    Args:
        text (str): Full response text
        section_name (str): Name of the section to extract
        
    Returns:
        str: Extracted section content
    """
    pattern = f"{section_name}:(.*?)(?=\n\n|$)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""
