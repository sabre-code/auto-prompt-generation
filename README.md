# Auto Prompt Generation

A powerful DSPy-based system for automatically generating optimized prompts based on user queries. This package intelligently analyzes user queries, determines the appropriate expert persona, and creates optimized prompts for improved AI interactions.

## Features

- **Intelligent Query Classification**: Automatically categorizes queries by type, domain, and complexity
- **Expert Persona Generation**: Creates appropriate expert roles based on query analysis
- **Prompt Optimization**: Transforms user queries into well-structured, optimized prompts
- **Flexible Model Support**: Works with various language models through DSPy
- **Command Line Interface**: Easy-to-use CLI for quick prompt generation
- **Python API**: Full programmatic access for integration into other projects

## Installation

### From Git Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/auto-prompt-generation.git
cd auto-prompt-generation

# Install the package
pip install -e .
```

### Direct Installation from Git

```bash
pip install git+https://github.com/yourusername/auto-prompt-generation.git
```

## Quick Start

### Python API

```python
from auto_prompt_generation import QueryHandlerSystem

# Initialize the system
system = QueryHandlerSystem()

# Process a query
query = "Generate a case series for patients taking both Rosuvastatin and Clopidogrel"
result = system.process_query(query)

print("Optimized Prompt:")
print(result['optimized_prompt'])
```

### Command Line Interface

```bash
# Basic usage
auto-prompt-gen "How do I optimize my Python code for performance?"

# With custom model
auto-prompt-gen "Explain machine learning concepts" --model "gpt-3.5-turbo"

# JSON output with verbose analysis
auto-prompt-gen "Write a business plan" --output-format json --verbose
```

## Usage Examples

### Medical Query Example

```python
from auto_prompt_generation import QueryHandlerSystem

system = QueryHandlerSystem()
query = "Generate a case series for patients taking both Rosuvastatin and Clopidogrel who experienced a non-fatal myocardial infarction."

result = system.process_query(query)
print(result['optimized_prompt'])
```

**Output:**
```
You are a clinical research specialist with extensive experience in cardiology and pharmacovigilance. You have a deep understanding of drug interactions, cardiovascular disease management, and clinical case study methodology...

User's question: Generate a case series for patients taking both Rosuvastatin and Clopidogrel who experienced a non-fatal myocardial infarction.
```

### Technical Query Example

```python
query = "How do I implement a binary search tree in Python?"
result = system.process_query(query)
```

The system will automatically:
1. Classify this as a technical, programming query
2. Generate a "Senior Software Engineer" expert persona
3. Create an optimized prompt for code implementation

## Configuration

### Model Configuration

You can configure different language models:

```python
# Using OpenAI GPT
system = QueryHandlerSystem(model_name="gpt-3.5-turbo")

# Using Anthropic Claude
system = QueryHandlerSystem(model_name="claude-3-sonnet")

# Using local Ollama model
system = QueryHandlerSystem(model_name="ollama_chat/gemma2:2b")
```

### DSPy Configuration

For advanced DSPy configuration:

```python
import dspy
from auto_prompt_generation import QueryHandlerSystem

# Configure DSPy settings
dspy.settings.configure(
    lm=dspy.OpenAI(model="gpt-4"),
    rm=dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')
)

system = QueryHandlerSystem()
```

## API Reference

### QueryHandlerSystem

Main class for processing queries and generating optimized prompts.

#### Methods

- `__init__(model_name: str = "ollama_chat/gemma2:2b")`: Initialize the system
- `process_query(user_query: str) -> Dict`: Process a query and return results

#### Return Format

```python
{
    "original_query": str,
    "analysis": {
        "type": str,          # Query type classification
        "domain": str,        # Domain/field
        "complexity": str,    # Complexity level
        "expert_role": str    # Generated expert role
    },
    "optimized_prompt": str   # Final optimized prompt
}
```

### Core Components

- `QueryClassifier`: Classifies query type, domain, and complexity
- `ExpertPersonaGenerator`: Generates appropriate expert personas
- `PromptOptimizer`: Creates optimized prompts
- `DynamicQueryHandler`: Main processing pipeline

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/auto-prompt-generation.git
cd auto-prompt-generation

# Install in development mode with dev dependencies
pip install -e .[dev]
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=auto_prompt_generation
```

### Code Formatting

```bash
# Format code with black
black auto_prompt_generation/

# Check with flake8
flake8 auto_prompt_generation/

# Type checking with mypy
mypy auto_prompt_generation/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [DSPy](https://github.com/stanfordnlp/dspy) - the framework for programming with foundation models
- Inspired by the need for better prompt engineering in AI applications

## Changelog

### v0.1.0
- Initial release
- Basic query classification and prompt optimization
- Command line interface
- Support for multiple language models through DSPy

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/auto-prompt-generation/issues) page
2. Create a new issue with detailed information
3. For general questions, start a [Discussion](https://github.com/yourusername/auto-prompt-generation/discussions)
