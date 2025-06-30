import auto_prompt_generation
from typing import Dict

class QueryClassifier(auto_prompt_generation.Signature):
    """Classify the type of user query and determine appropriate handling strategy"""
    
    query = auto_prompt_generation.InputField(desc="The user's original query")
    query_type = auto_prompt_generation.OutputField(desc="Type of query: creative, analytical, technical, informational, problem_solving, or conversational")
    domain = auto_prompt_generation.OutputField(desc="Domain/field of the query (e.g., technology, health, business, education)")
    complexity = auto_prompt_generation.OutputField(desc="Complexity level: simple, moderate, or complex")
    intent = auto_prompt_generation.OutputField(desc="What the user wants to achieve")

class ExpertPersonaGenerator(auto_prompt_generation.Signature):
    """Generate appropriate expert persona based on query analysis"""
    
    query_type = auto_prompt_generation.InputField()
    domain = auto_prompt_generation.InputField()
    complexity = auto_prompt_generation.InputField()
    expert_role = auto_prompt_generation.OutputField(desc="Specific expert role/persona (e.g., 'senior software engineer', 'creative writing instructor')")
    expertise_description = auto_prompt_generation.OutputField(desc="Brief description of the expert's relevant skills and background")

class PromptOptimizer(auto_prompt_generation.Signature):
    """Transform user query into an optimized declarative prompt that can be sent to another AI system"""
    
    original_query = auto_prompt_generation.InputField()
    expert_role = auto_prompt_generation.InputField()
    expertise_description = auto_prompt_generation.InputField()
    query_type = auto_prompt_generation.InputField()
    intent = auto_prompt_generation.InputField()
    optimized_prompt = auto_prompt_generation.OutputField(desc="A complete prompt instruction that starts with 'You are [expert role]...' and includes the original query at the end. This should be a prompt TO SEND TO an AI system, not an answer to the query.")

class DynamicQueryHandler(auto_prompt_generation.Module):
    """Main module that handles any type of user query and generates optimized prompts"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize the pipeline components with more specific instructions
        self.classifier = auto_prompt_generation.ChainOfThought(QueryClassifier)
        self.persona_generator = auto_prompt_generation.ChainOfThought(ExpertPersonaGenerator)
        self.prompt_optimizer = auto_prompt_generation.ChainOfThought(PromptOptimizer)
        
        # Add system instruction for prompt generation
        self.system_instruction = """
        IMPORTANT: You are creating PROMPTS for another AI system, not answering the user's question directly.
        Your output should be a complete prompt that starts with "You are [expert role]..." and ends with the user's original question.
        The prompt should instruct another AI on how to respond to the user's query.
        DO NOT answer the user's question - CREATE A PROMPT for another AI to answer it.
        """
        
        # Cache for common query patterns (optional optimization)
        self.query_cache = {}
    
    def forward(self, user_query: str) -> auto_prompt_generation.Prediction:
        """Process any user query and return optimized prompt"""
        
        # Step 1: Classify the query
        classification = self.classifier(query=user_query)
        
        # Step 2: Generate appropriate expert persona
        persona = self.persona_generator(
            query_type=classification.query_type,
            domain=classification.domain,
            complexity=classification.complexity
        )
        
        # Step 3: Create optimized prompt with explicit instruction
        optimized = self.prompt_optimizer(
            original_query=user_query,
            expert_role=persona.expert_role,
            expertise_description=persona.expertise_description,
            query_type=classification.query_type,
            intent=classification.intent
        )
        
        # Post-process to ensure it's a proper prompt format
        prompt_text = optimized.optimized_prompt
        if not prompt_text.startswith("You are"):
            prompt_text = f"You are {persona.expert_role}. {prompt_text}"
        
        if user_query not in prompt_text:
            prompt_text += f"\n\nUser's question: {user_query}"
        
        return auto_prompt_generation.Prediction(
            original_query=user_query,
            query_type=classification.query_type,
            domain=classification.domain,
            complexity=classification.complexity,
            expert_role=persona.expert_role,
            optimized_prompt=prompt_text
        )

class QueryHandlerSystem:
    """Complete system for handling diverse user queries"""
    
    def __init__(self, model_name: str = "ollama_chat/gemma2:2b"):
        # Configure DSPy with your preferred LM
        auto_prompt_generation.settings.configure(lm=auto_prompt_generation.LM(model=model_name))
        
        # Initialize the main handler
        self.handler = DynamicQueryHandler()
        
        # # Optional: Compile with examples for better performance
        # self.compiled_handler = None
    
    def process_query(self, user_query: str) -> Dict:
        """Main entry point - processes any user query"""
        
        handler = self.handler
        result = handler(user_query)
        
        return {
            "original_query": result.original_query,
            "analysis": {
                "type": result.query_type,
                "domain": result.domain,
                "complexity": result.complexity,
                "expert_role": result.expert_role
            },
            "optimized_prompt": result.optimized_prompt
        }

if __name__ == "__main__":
    # Initialize the system
    system = QueryHandlerSystem()
    
    test_queries = [
        "Generate a case series for patients taking both Rosuvastatin and Clopidogrel who experienced a non-fatal myocardial infarction."
    ]
    print("Processing diverse user queries...\n")
    
    for i, query in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        result = system.process_query(query)
        
        #print(f"Analysis: {result['analysis']}")
        print(f"Optimized Prompt: {result['optimized_prompt']}...")
        print("-" * 80)