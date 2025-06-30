import dspy
from typing import Dict

class QueryClassifier(dspy.Signature):
    """Classify the type of user query and determine appropriate handling strategy"""
    
    query = dspy.InputField(desc="The user's original query")
    query_type = dspy.OutputField(desc="Type of query: creative, analytical, technical, informational, problem_solving, or conversational")
    domain = dspy.OutputField(desc="Domain/field of the query (e.g., technology, health, business, education)")
    complexity = dspy.OutputField(desc="Complexity level: simple, moderate, or complex")
    intent = dspy.OutputField(desc="What the user wants to achieve")

class ExpertPersonaGenerator(dspy.Signature):
    """Generate appropriate expert persona based on query analysis"""
    
    query_type = dspy.InputField()
    domain = dspy.InputField()
    complexity = dspy.InputField()
    expert_role = dspy.OutputField(desc="Specific expert role/persona (e.g., 'senior software engineer', 'creative writing instructor')")
    expertise_description = dspy.OutputField(desc="Brief description of the expert's relevant skills and background")

class PromptOptimizer(dspy.Signature):
    """Transform user query into an optimized declarative prompt that can be sent to another AI system"""
    
    original_query = dspy.InputField()
    expert_role = dspy.InputField()
    expertise_description = dspy.InputField()
    query_type = dspy.InputField()
    intent = dspy.InputField()
    optimized_prompt = dspy.OutputField(desc="A complete prompt instruction that starts with 'You are [expert role]...' and includes the original query at the end. This should be a prompt TO SEND TO an AI system, not an answer to the query.")

class DynamicQueryHandler(dspy.Module):
    """Main module that handles any type of user query and generates optimized prompts"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize the pipeline components with more specific instructions
        self.classifier = dspy.ChainOfThought(QueryClassifier)
        self.persona_generator = dspy.ChainOfThought(ExpertPersonaGenerator)
        self.prompt_optimizer = dspy.ChainOfThought(PromptOptimizer)
        
        # Add system instruction for prompt generation
        self.system_instruction = """
        IMPORTANT: You are creating PROMPTS for another AI system, not answering the user's question directly.
        Your output should be a complete prompt that starts with "You are [expert role]..." and ends with the user's original question.
        The prompt should instruct another AI on how to respond to the user's query.
        DO NOT answer the user's question - CREATE A PROMPT for another AI to answer it.
        """
        
        # Cache for common query patterns (optional optimization)
        self.query_cache = {}
    
    def forward(self, user_query: str) -> dspy.Prediction:
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
        
        return dspy.Prediction(
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
        dspy.settings.configure(lm=dspy.LM(model=model_name))
        
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
