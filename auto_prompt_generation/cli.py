"""
Command Line Interface for Auto Prompt Generation
"""

import argparse
import json
from .core import QueryHandlerSystem

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Auto Prompt Generation - Generate optimized prompts from user queries"
    )
    
    parser.add_argument(
        "query",
        help="The user query to process"
    )
    
    parser.add_argument(
        "--model", 
        default="ollama_chat/gemma2:2b",
        help="Model to use for processing (default: ollama_chat/gemma2:2b)"
    )
    
    parser.add_argument(
        "--output-format",
        choices=["json", "text"],
        default="text",
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed analysis"
    )
    
    args = parser.parse_args()
    
    # Initialize the system
    system = QueryHandlerSystem(model_name=args.model)
    
    # Process the query
    result = system.process_query(args.query)
    
    if args.output_format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"Original Query: {result['original_query']}")
        if args.verbose:
            print(f"Analysis: {result['analysis']}")
        print(f"Optimized Prompt: {result['optimized_prompt']}")

if __name__ == "__main__":
    main()
