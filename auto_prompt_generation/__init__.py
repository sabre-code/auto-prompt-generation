"""
Auto Prompt Generation Package

A DSPy-based system for automatically generating optimized prompts based on user queries.
This package provides intelligent query classification, expert persona generation, and
prompt optimization for improved AI interactions.
"""

from .core import (
    QueryClassifier,
    ExpertPersonaGenerator,
    PromptOptimizer,
    DynamicQueryHandler,
    QueryHandlerSystem
)

__version__ = "0.1.0"
__author__ = "Sulaiman Mutawalli"
__email__ = "sulaimanmutawalli@example.com"

__all__ = [
    "QueryClassifier",
    "ExpertPersonaGenerator", 
    "PromptOptimizer",
    "DynamicQueryHandler",
    "QueryHandlerSystem"
]
