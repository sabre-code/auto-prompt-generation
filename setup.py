"""
Setup configuration for auto-prompt-generation package
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Auto Prompt Generation - A DSPy-based system for generating optimized prompts"

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return ['dspy-ai>=2.4.0']

setup(
    name="auto-prompt-generation",
    version="0.1.0",
    author="Sulaiman Mutawalli",
    author_email="sulaimanmutawalli@example.com",
    description="A DSPy-based system for automatically generating optimized prompts",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sabre-code/auto-prompt-generation",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
        ]
    },
    entry_points={
        "console_scripts": [
            "auto-prompt-gen=auto_prompt_generation.cli:main",
        ],
    },
    keywords="dspy, prompt, generation, ai, nlp, optimization",
    project_urls={
        "Bug Reports": "https://github.com/sabre-code/auto-prompt-generation/issues",
        "Source": "https://github.com/sabre-code/auto-prompt-generation",
        "Documentation": "https://github.com/sabre-code/auto-prompt-generation#readme",
    },
)
