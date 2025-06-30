#!/usr/bin/env python3
"""
Simple example showing how to use auto-prompt-generation
"""

from auto_prompt_generation import QueryHandlerSystem

# Initialize the system (this will configure DSPy)
system = QueryHandlerSystem()

# Example query
query = "Generate a case series for patients taking both Rosuvastatin and Clopidogrel who experienced a non-fatal myocardial infarction."

print("Processing query...")
print(f"Input: {query}")

# Process the query
result = system.process_query(query)

print("\nResult:")
print(f"Optimized Prompt: {result['optimized_prompt']}")
print(f"Expert Role: {result['analysis']['expert_role']}")
print(f"Domain: {result['analysis']['domain']}")
