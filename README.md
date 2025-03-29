# AI Business Insights Assistant

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/divyal101/ai-business-insights/actions/workflows/test.yml/badge.svg)](https://github.com/divyal101/ai-business-insights/actions/workflows/test.yml)
[![Codecov](https://codecov.io/gh/divyal101/ai-business-insights/branch/main/graph/badge.svg)](https://codecov.io/gh/divyal101/ai-business-insights)
[![Build Pass](https://img.shields.io/badge/build-pass-brightgreen.svg)](https://github.com/divyal101/ai-business-insights/actions/workflows/test.yml)

An AI-powered business intelligence tool that leverages Google's Gemini AI to provide structured, actionable insights for strategic decision-making.

## Features

- 🔍 **Context-Aware Analysis**: Understands business context and provides relevant insights
- 📊 **Multiple Analysis Types**:
  - Competitive Analysis
  - Trend Forecasting
  - General Business Analysis
- 📈 **Structured Output**: Well-organized insights with clear sections
- ⚡ **Real-time Processing**: Quick response generation
- 📊 **Quality Metrics**: Business Relevance Score (BRS) and Response Consistency Score (RCS)
- 🔄 **Automated Testing**: Comprehensive test suite with CI/CD pipeline

## Tech Stack

- **Backend**: Python, Flask, Google Gemini AI
- **Frontend**: Streamlit
- **Evaluation**: scikit-learn for similarity scoring
- **Data Storage**: JSON-based logging system
- **Testing**: pytest, pytest-cov
- **CI/CD**: GitHub Actions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-business-insights.git
cd ai-business-insights
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the `backend` directory with:
```
GOOGLE_API_KEY=your_gemini_api_key
```

## Usage

1. Start the backend server:
```bash
cd backend
python main.py
```

2. Start the Streamlit frontend:
```bash
cd streamlit_app
streamlit run app.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Project Structure

```
ai-business-insights/
├── backend/
│   ├── main.py              # Flask API server
│   ├── query_engine.py      # Gemini AI integration
│   ├── config.py           # Configuration settings
│   └── user_engagement_log.json  # Usage analytics
├── streamlit_app/
│   ├── app.py              # Streamlit frontend
│   └── style.css           # Custom styling
├── tests/
│   └── test_query_engine.py  # Test suite
├── .github/
│   └── workflows/
│       └── test.yml        # GitHub Actions workflow
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## API Endpoints

### POST /generate-insights
Generates business insights based on the provided query.

Request body:
```json
{
    "query": "Your business query here",
    "analysis_type": "competitive|trend|general"
}
```

Response:
```json
{
    "status": "success",
    "query": "Your business query here",
    "analysis_type": "competitive",
    "insights": {
        // Structured insights based on analysis type
    },
    "BRS": 85.5,
    "RCS": 90.0
}
```

### GET /analysis-types
Returns available analysis types and their descriptions.

## Evaluation Metrics

### Business Relevance Score (BRS)
- Measures how well the generated insights align with the query
- Uses TF-IDF and cosine similarity
- Range: 0-100%

### Response Consistency Score (RCS)
- Evaluates the completeness of structured sections
- Varies by analysis type
- Range: 0-100%

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=backend --cov-report=term-missing

# Run specific test file
pytest tests/test_query_engine.py

# Run integration tests only
pytest -m integration
```

### Test Coverage
The project maintains a minimum test coverage of 80%. Coverage reports are automatically generated and uploaded to Codecov.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for providing the language model
- Streamlit for the frontend framework
- Flask for the backend framework
- pytest for the testing framework
- GitHub Actions for CI/CD automation

## Support

For support, please open an issue in the GitHub repository or contact the maintainers. "# ai-business-insight" 
