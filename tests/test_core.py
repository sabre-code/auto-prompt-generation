"""
Tests for the core functionality
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from auto_prompt_generation.core import (
    QueryClassifier,
    ExpertPersonaGenerator,
    PromptOptimizer,
    DynamicQueryHandler,
    QueryHandlerSystem
)

class TestQueryHandlerSystem:
    """Test the main QueryHandlerSystem class"""
    
    def test_init_with_default_model(self):
        """Test initialization with default model"""
        with patch('dspy.settings.configure') as mock_configure:
            system = QueryHandlerSystem()
            mock_configure.assert_called_once()
            assert system.handler is not None
    
    def test_init_with_custom_model(self):
        """Test initialization with custom model"""
        with patch('dspy.settings.configure') as mock_configure:
            system = QueryHandlerSystem(model_name="custom_model")
            mock_configure.assert_called_once()
    
    def test_process_query_structure(self):
        """Test that process_query returns the correct structure"""
        with patch('dspy.settings.configure'):
            system = QueryHandlerSystem()
            
            # Mock the handler response
            mock_result = Mock()
            mock_result.original_query = "test query"
            mock_result.query_type = "technical"
            mock_result.domain = "technology"
            mock_result.complexity = "moderate"
            mock_result.expert_role = "software engineer"
            mock_result.optimized_prompt = "You are a software engineer..."
            
            system.handler = Mock(return_value=mock_result)
            
            result = system.process_query("test query")
            
            # Check structure
            assert "original_query" in result
            assert "analysis" in result
            assert "optimized_prompt" in result
            
            # Check analysis structure
            analysis = result["analysis"]
            assert "type" in analysis
            assert "domain" in analysis
            assert "complexity" in analysis
            assert "expert_role" in analysis

class TestDynamicQueryHandler:
    """Test the DynamicQueryHandler module"""
    
    def test_init(self):
        """Test initialization of DynamicQueryHandler"""
        handler = DynamicQueryHandler()
        assert handler.classifier is not None
        assert handler.persona_generator is not None
        assert handler.prompt_optimizer is not None
        assert handler.query_cache is not None
    
    def test_forward_method_exists(self):
        """Test that forward method exists and is callable"""
        handler = DynamicQueryHandler()
        assert hasattr(handler, 'forward')
        assert callable(handler.forward)
    
    def test_prompt_format_validation(self):
        """Test that prompts are formatted correctly"""
        handler = DynamicQueryHandler()
        
        # Mock the pipeline components
        handler.classifier = Mock()
        handler.persona_generator = Mock()
        handler.prompt_optimizer = Mock()
        
        # Set up mock returns
        handler.classifier.return_value = Mock(
            query_type="technical",
            domain="technology",
            complexity="moderate",
            intent="learn programming"
        )
        
        handler.persona_generator.return_value = Mock(
            expert_role="software engineer",
            expertise_description="experienced developer"
        )
        
        handler.prompt_optimizer.return_value = Mock(
            optimized_prompt="Basic prompt without proper format"
        )
        
        # Mock dspy.Prediction
        with patch('dspy.Prediction') as mock_prediction:
            mock_prediction.return_value = Mock()
            result = handler.forward("test query")
            
            # Verify Prediction was called
            mock_prediction.assert_called_once()

class TestQueryClassifier:
    """Test the QueryClassifier signature"""
    
    def test_signature_fields(self):
        """Test that QueryClassifier has the required fields"""
        # This is a signature class, so we just verify it exists and has the right structure
        assert hasattr(QueryClassifier, 'query')
        assert hasattr(QueryClassifier, 'query_type')
        assert hasattr(QueryClassifier, 'domain')
        assert hasattr(QueryClassifier, 'complexity')
        assert hasattr(QueryClassifier, 'intent')

class TestExpertPersonaGenerator:
    """Test the ExpertPersonaGenerator signature"""
    
    def test_signature_fields(self):
        """Test that ExpertPersonaGenerator has the required fields"""
        assert hasattr(ExpertPersonaGenerator, 'query_type')
        assert hasattr(ExpertPersonaGenerator, 'domain')
        assert hasattr(ExpertPersonaGenerator, 'complexity')
        assert hasattr(ExpertPersonaGenerator, 'expert_role')
        assert hasattr(ExpertPersonaGenerator, 'expertise_description')

class TestPromptOptimizer:
    """Test the PromptOptimizer signature"""
    
    def test_signature_fields(self):
        """Test that PromptOptimizer has the required fields"""
        assert hasattr(PromptOptimizer, 'original_query')
        assert hasattr(PromptOptimizer, 'expert_role')
        assert hasattr(PromptOptimizer, 'expertise_description')
        assert hasattr(PromptOptimizer, 'query_type')
        assert hasattr(PromptOptimizer, 'intent')
        assert hasattr(PromptOptimizer, 'optimized_prompt')
