import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from adaptive_engine import AdaptiveEngine

engine = AdaptiveEngine(llm_provider="openrouter")

response = engine.process_request(
    user_id="test_user",
    question="What is machine learning?",
    lecture_text="Machine learning is part of AI...",
    emotion="confused",
    topic="AI"
)

print("\n=== FINAL EXPLANATION ===\n")
print(response["explanation"])

print("\n=== METADATA ===")
print(response["metadata"])

print("\n=== INTERVENTION ===")
print(response["intervention"])

print("\n=== RECOMMENDATIONS ===")
print(response["recommendations"])
