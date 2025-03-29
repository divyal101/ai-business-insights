import pytest
from query_engine import generate_insights, format_response

def test_format_response_general():
    """Test formatting of general analysis response."""
    test_response = """
    📊 Business Insights:
    This is a test summary.
    
    🔑 Key Strategic Points:
    • Point 1
    • Point 2
    
    ✅ Actionable Recommendations:
    - Rec 1
    - Rec 2
    
    📈 Implementation Timeline:
    * Timeline 1
    * Timeline 2
    
    📊 Expected Outcomes:
    • Outcome 1
    • Outcome 2
    """
    
    result = format_response(test_response, "general")
    
    assert "summary" in result
    assert "key_points" in result
    assert "recommendations" in result
    assert "timeline" in result
    assert "outcomes" in result
    
    assert "This is a test summary" in result["summary"]
    assert "Point 1" in result["key_points"]
    assert "Rec 1" in result["recommendations"]
    assert "Timeline 1" in result["timeline"]
    assert "Outcome 1" in result["outcomes"]

def test_format_response_competitive():
    """Test formatting of competitive analysis response."""
    test_response = """
    📊 Market Position Analysis:
    This is market position.
    
    🔍 Competitor Strengths and Weaknesses:
    • Strength 1
    • Weakness 1
    
    💡 Strategic Differentiators:
    - Diff 1
    - Diff 2
    
    🎯 Market Opportunities:
    * Opp 1
    * Opp 2
    
    ⚠️ Potential Threats:
    • Threat 1
    • Threat 2
    """
    
    result = format_response(test_response, "competitive")
    
    assert "market_position" in result
    assert "competitor_analysis" in result
    assert "differentiators" in result
    assert "opportunities" in result
    assert "threats" in result
    
    assert "This is market position" in result["market_position"]
    assert "Strength 1" in result["competitor_analysis"]
    assert "Diff 1" in result["differentiators"]
    assert "Opp 1" in result["opportunities"]
    assert "Threat 1" in result["threats"]

def test_format_response_trend():
    """Test formatting of trend analysis response."""
    test_response = """
    📈 Current Market Trends:
    • Trend 1
    • Trend 2
    
    🔮 Future Predictions:
    - Prediction 1
    - Prediction 2
    
    🎯 Growth Opportunities:
    * Opp 1
    * Opp 2
    
    ⚠️ Risk Factors:
    • Risk 1
    • Risk 2
    
    💡 Proactive Measures:
    - Measure 1
    - Measure 2
    """
    
    result = format_response(test_response, "trend")
    
    assert "current_trends" in result
    assert "predictions" in result
    assert "opportunities" in result
    assert "risks" in result
    assert "measures" in result
    
    assert "Trend 1" in result["current_trends"]
    assert "Prediction 1" in result["predictions"]
    assert "Opp 1" in result["opportunities"]
    assert "Risk 1" in result["risks"]
    assert "Measure 1" in result["measures"]

@pytest.mark.integration
def test_generate_insights():
    """Test the generate_insights function with a simple query."""
    query = "What are the key growth opportunities for a small business?"
    result = generate_insights(query, "general")
    
    assert isinstance(result, dict)
    assert "error" not in result
    assert "summary" in result
    assert "key_points" in result
    assert "recommendations" in result
    assert "timeline" in result
    assert "outcomes" in result

@pytest.mark.integration
def test_generate_insights_competitive():
    """Test competitive analysis generation."""
    query = "Analyze our competitive position in the e-commerce market"
    result = generate_insights(query, "competitive")
    
    assert isinstance(result, dict)
    assert "error" not in result
    assert "market_position" in result
    assert "competitor_analysis" in result
    assert "differentiators" in result
    assert "opportunities" in result
    assert "threats" in result

@pytest.mark.integration
def test_generate_insights_trend():
    """Test trend analysis generation."""
    query = "What are the emerging trends in the technology sector?"
    result = generate_insights(query, "trend")
    
    assert isinstance(result, dict)
    assert "error" not in result
    assert "current_trends" in result
    assert "predictions" in result
    assert "opportunities" in result
    assert "risks" in result
    assert "measures" in result 