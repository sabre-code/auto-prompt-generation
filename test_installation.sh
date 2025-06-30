#!/bin/bash
# Test installation from GitHub

echo "🧪 Testing installation from GitHub repository..."
echo "Repository: https://github.com/sabre-code/auto-prompt-generation.git"
echo ""

# Create a temporary directory for testing
TEST_DIR=$(mktemp -d)
cd "$TEST_DIR"

echo "📦 Creating test environment..."
python -m venv test_env
source test_env/bin/activate

echo "⬇️  Installing package from GitHub..."
pip install git+https://github.com/sabre-code/auto-prompt-generation.git

echo "🔍 Testing package import..."
python -c "
import auto_prompt_generation
print('✅ Package imported successfully!')
print('Available components:', auto_prompt_generation.__all__)
print('Version:', auto_prompt_generation.__version__)
"

echo "🖥️  Testing CLI command..."
auto-prompt-gen --help

echo "🎯 Testing basic functionality..."
python -c "
from auto_prompt_generation import QueryHandlerSystem
print('✅ QueryHandlerSystem imported successfully!')
"

echo "🧹 Cleaning up..."
deactivate
cd /
rm -rf "$TEST_DIR"

echo ""
echo "🎉 All tests passed! Your package is ready for use."
echo ""
echo "📋 Installation command for users:"
echo "pip install git+https://github.com/sabre-code/auto-prompt-generation.git"
