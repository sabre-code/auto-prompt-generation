"""
Test configuration and fixtures
"""

import pytest
from unittest.mock import Mock, patch
import dspy
from auto_prompt_generation import QueryHandlerSystem

@pytest.fixture
def mock_dspy_lm():
    """Mock DSPy language model for testing"""
    with patch('dspy.settings.configure') as mock_configure:
        mock_lm = Mock()
        mock_configure.return_value = None
        yield mock_lm

@pytest.fixture
def sample_queries():
    """Sample queries for testing"""
    return [
        "Generate a case series for patients taking both Rosuvastatin and Clopidogrel",
        "How do I implement a binary search tree in Python?",
        "Write a creative story about a robot learning to paint",
        "Explain the economic impact of climate change",
        "What is the best way to prepare for a job interview?"
    ]

@pytest.fixture
def query_handler_system(mock_dspy_lm):
    """Create a QueryHandlerSystem instance for testing"""
    return QueryHandlerSystem(model_name="test_model")
