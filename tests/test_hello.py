"""
Pytest Automation Test Suite for hello.py.
Verifies logic and expected responses.
"""
import sys
import os

# Add parent directory to sys.path so hello module can be imported anywhere
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hello import get_greeting, calculate_feature_score

def test_get_greeting():
    """Verify standard and custom greetings."""
    assert "Hello, DevOps Engineer!" in get_greeting("DevOps Engineer")
    assert "Hello, World!" in get_greeting("")
    assert "Hello, World!" in get_greeting(None)

def test_calculate_feature_score():
    """Verify basic calculation scoring for baseline model pipeline."""
    score = calculate_feature_score(10.0, 10.0)
    assert score == 10.0
    assert calculate_feature_score(0, 0) == 0.0
