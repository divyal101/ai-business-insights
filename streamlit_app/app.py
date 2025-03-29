import streamlit as st
import requests
import json
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from typing import Dict, Any

# Configure the page
st.set_page_config(
    page_title="AI Business Insights Assistant",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main {
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .stSelectbox > div > div > select {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📊 AI Business Insights Assistant")
st.markdown("""
    This AI-powered assistant helps you make strategic business decisions by providing:
    - Competitive analysis and market positioning
    - Trend forecasting and market predictions
    - Comprehensive business insights and recommendations
""")

# Sidebar for analysis type selection
with st.sidebar:
    st.header("Analysis Type")
    analysis_type = st.selectbox(
        "Select the type of analysis",
        ["general", "competitive", "trend"],
        format_func=lambda x: {
            "general": "General Business Analysis",
            "competitive": "Competitive Analysis",
            "trend": "Trend Analysis"
        }[x]
    )
    
    st.markdown("---")
    st.markdown("""
        ### About
        This tool uses advanced AI to analyze your business queries and provide structured, actionable insights.
        
        ### Features
        - 🔍 Context-aware analysis
        - 📈 Data-driven recommendations
        - 📊 Structured insights
        - ⚡ Real-time processing
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Query input
    query = st.text_area(
        "Enter your business query",
        placeholder="Example: Analyze our competitive position in the e-commerce market",
        height=100
    )
    
    if st.button("Generate Insights", type="primary"):
        if not query:
            st.error("Please enter a query")
        else:
            with st.spinner("Generating insights..."):
                try:
                    # Call the backend API
                    response = requests.post(
                        "http://localhost:8000/generate-insights",
                        json={"query": query, "analysis_type": analysis_type}
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Display insights based on analysis type
                        if analysis_type == "competitive":
                            st.subheader("📊 Market Position Analysis")
                            st.write(data["insights"]["market_position"])
                            
                            st.subheader("🔍 Competitor Analysis")
                            for point in data["insights"]["competitor_analysis"]:
                                st.write(f"• {point}")
                            
                            st.subheader("💡 Strategic Differentiators")
                            for point in data["insights"]["differentiators"]:
                                st.write(f"• {point}")
                            
                            st.subheader("🎯 Market Opportunities")
                            for point in data["insights"]["opportunities"]:
                                st.write(f"• {point}")
                            
                            st.subheader("⚠️ Potential Threats")
                            for point in data["insights"]["threats"]:
                                st.write(f"• {point}")
                                
                        elif analysis_type == "trend":
                            st.subheader("📈 Current Market Trends")
                            for trend in data["insights"]["current_trends"]:
                                st.write(f"• {trend}")
                            
                            st.subheader("🔮 Future Predictions")
                            for prediction in data["insights"]["predictions"]:
                                st.write(f"• {prediction}")
                            
                            st.subheader("🎯 Growth Opportunities")
                            for opportunity in data["insights"]["opportunities"]:
                                st.write(f"• {opportunity}")
                            
                            st.subheader("⚠️ Risk Factors")
                            for risk in data["insights"]["risks"]:
                                st.write(f"• {risk}")
                            
                            st.subheader("💡 Proactive Measures")
                            for measure in data["insights"]["measures"]:
                                st.write(f"• {measure}")
                                
                        else:  # general analysis
                            st.subheader("📊 Business Insights")
                            st.write(data["insights"]["summary"])
                            
                            st.subheader("🔑 Key Strategic Points")
                            for point in data["insights"]["key_points"]:
                                st.write(f"• {point}")
                            
                            st.subheader("✅ Recommendations")
                            for rec in data["insights"]["recommendations"]:
                                st.write(f"• {rec}")
                            
                            st.subheader("📈 Implementation Timeline")
                            for step in data["insights"]["timeline"]:
                                st.write(f"• {step}")
                            
                            st.subheader("📊 Expected Outcomes")
                            for outcome in data["insights"]["outcomes"]:
                                st.write(f"• {outcome}")
                        
                        # Display metrics
                        st.markdown("---")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Business Relevance Score", f"{data['BRS']}%")
                        with col2:
                            st.metric("Response Consistency Score", f"{data['RCS']}%")
                            
                    else:
                        st.error(f"Error: {response.json().get('error', 'Unknown error')}")
                        
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

with col2:
    # Display example queries based on analysis type
    st.subheader("Example Queries")
    examples = {
        "general": [
            "What are the key growth opportunities for our business?",
            "How can we improve our operational efficiency?",
            "What strategic initiatives should we prioritize?"
        ],
        "competitive": [
            "Analyze our competitive position in the market",
            "What are our main competitors' strengths and weaknesses?",
            "How can we differentiate ourselves from competitors?"
        ],
        "trend": [
            "What are the emerging trends in our industry?",
            "How will market conditions evolve in the next year?",
            "What technological trends should we prepare for?"
        ]
    }
    
    for example in examples[analysis_type]:
        if st.button(example, key=example):
            st.text_area("Enter your business query", value=example, key="query_input")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Google Gemini AI</p>
        <p>© 2024 AI Business Insights Assistant</p>
    </div>
""", unsafe_allow_html=True)
