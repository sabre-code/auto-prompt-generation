#!/usr/bin/env python3
"""
Example usage of the auto-prompt-generation package
"""

from auto_prompt_generation import QueryHandlerSystem

def main():
    """Run example queries through the system"""
    
    # Initialize the system
    print("Initializing Auto Prompt Generation System...")
    system = QueryHandlerSystem()
    
    # Example queries to test different domains and types
    example_queries = [
        # Medical/Healthcare
        "Generate a case series for patients taking both Rosuvastatin and Clopidogrel who experienced a non-fatal myocardial infarction.",
        
        # Technical/Programming
        "How do I implement a binary search tree in Python with proper error handling?",
        
        # Creative
        "Write a short story about a time traveler who accidentally changes history by saving a butterfly.",
        
        # Business/Analytics
        "Create a comprehensive market analysis for electric vehicle adoption in Southeast Asia.",
        
        # Educational
        "Explain quantum mechanics to a high school student using everyday analogies.",
        
        # Problem-solving
        "My website is loading slowly. Help me identify and fix performance bottlenecks."
    ]
    
    print(f"\nProcessing {len(example_queries)} example queries...\n")
    print("=" * 80)
    
    for i, query in enumerate(example_queries, 1):
        print(f"\n🔍 QUERY {i}:")
        print(f"Input: {query}")
        
        # Process the query
        result = system.process_query(query)
        
        print(f"\n📊 ANALYSIS:")
        analysis = result['analysis']
        print(f"  • Type: {analysis['type']}")
        print(f"  • Domain: {analysis['domain']}")
        print(f"  • Complexity: {analysis['complexity']}")
        print(f"  • Expert Role: {analysis['expert_role']}")
        
        print(f"\n✨ OPTIMIZED PROMPT:")
        prompt = result['optimized_prompt']
        # Truncate very long prompts for display
        if len(prompt) > 300:
            print(f"{prompt[:300]}...\n[Truncated - Full prompt is {len(prompt)} characters]")
        else:
            print(prompt)
        
        print("\n" + "=" * 80)
    
    print("\n🎉 All examples processed successfully!")
    print("\nTry the CLI tool with your own queries:")
    print("  auto-prompt-gen \"Your question here\"")
    print("  auto-prompt-gen \"Your question\" --output-format json --verbose")

if __name__ == "__main__":
    main()
