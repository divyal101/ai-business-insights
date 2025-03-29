# Contributing to AI Business Insights Assistant

Thank you for your interest in contributing to the AI Business Insights Assistant! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## How to Contribute

### 1. Fork the Repository
- Go to the [GitHub repository](https://github.com/yourusername/ai-business-insights)
- Click the "Fork" button in the top-right corner
- Clone your forked repository locally

### 2. Set Up Development Environment
```bash
# Clone your fork
git clone https://github.com/yourusername/ai-business-insights.git
cd ai-business-insights

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install pytest pytest-cov  # For testing

# Set up environment variables
cp backend/.env.example backend/.env
# Edit backend/.env with your Google Gemini API key
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Follow PEP 8 style guide
- Write clear, descriptive commit messages
- Add tests for new features
- Update documentation as needed

### 5. Run Tests
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=backend --cov-report=term-missing
```

### 6. Commit Your Changes
```bash
git add .
git commit -m "Description of your changes"
```

### 7. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 8. Create a Pull Request
- Go to your fork on GitHub
- Click "Compare & pull request"
- Fill in the PR template
- Submit the PR

## Development Guidelines

### Code Style
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

### Testing
- Write unit tests for new features
- Maintain test coverage above 80%
- Include integration tests for API endpoints
- Test edge cases and error conditions

### Documentation
- Update README.md for major changes
- Add inline documentation for complex logic
- Update API documentation for new endpoints
- Include examples in docstrings

### Git Workflow
- Use feature branches
- Write clear commit messages
- Keep commits focused and atomic
- Rebase before submitting PR

## Project Structure

```
ai-business-insights/
├── backend/              # Backend API and core logic
├── streamlit_app/       # Frontend application
├── tests/              # Test suite
├── .github/            # GitHub Actions workflows
└── docs/              # Additional documentation
```

## Testing Guidelines

### Unit Tests
- Test individual components
- Mock external dependencies
- Cover edge cases
- Test error conditions

### Integration Tests
- Test API endpoints
- Test data flow
- Test error handling
- Test with real API calls

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_query_engine.py

# Run with coverage
pytest --cov=backend --cov-report=term-missing

# Run integration tests only
pytest -m integration
```

## Documentation Guidelines

### Code Documentation
- Add docstrings to all functions
- Include type hints
- Document parameters and return values
- Add examples where helpful

### API Documentation
- Document all endpoints
- Include request/response examples
- Document error responses
- Keep documentation up to date

### README Updates
- Update installation instructions
- Document new features
- Update usage examples
- Keep project structure current

## Review Process

1. Code Review
   - PR will be reviewed by maintainers
   - Address all review comments
   - Make requested changes
   - Keep PR focused and manageable

2. Testing
   - Ensure all tests pass
   - Maintain or improve coverage
   - Test new features thoroughly

3. Documentation
   - Update relevant documentation
   - Add examples where needed
   - Keep documentation clear and concise

4. Merge
   - Squash and merge after approval
   - Delete feature branch
   - Update version if needed

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Join our community chat
- Contact maintainers directly

Thank you for contributing to the AI Business Insights Assistant! 