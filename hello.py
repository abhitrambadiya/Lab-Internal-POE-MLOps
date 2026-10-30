"""
Single-file Hello Application for MLOps Pipeline Demonstration.
Includes a simple feature function and a sample prediction/greeting function.
"""

def get_greeting(name: str = "World") -> str:
    """Returns a greeting message."""
    clean_name = str(name).strip() if name else "World"
    return f"Hello, {clean_name}! Welcome to MLOps Lab Internal POE."

def calculate_feature_score(x: float, y: float) -> float:
    """Calculates a simulated baseline model score."""
    return round((float(x) * 0.7) + (float(y) * 0.3), 4)

def main():
    msg = get_greeting("DevOps Engineer")
    print(msg)
    score = calculate_feature_score(12.5, 8.0)
    print(f"Sample Feature Calculation Score: {score}")

if __name__ == "__main__":
    main()
