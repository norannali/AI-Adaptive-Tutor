import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# test_style.py
"""
Test script for ResponseStyleController
Checks determine_tone, format_response, and adjust_for_emotion
"""

from response_style import ResponseStyleController

def main():
    print("\n--- Testing ResponseStyleController ---")
    
    s = ResponseStyleController()
    
    # 1️⃣ Test determine_tone
    print("\n--- Testing determine_tone ---")
    tone1 = s.determine_tone(emotion="confused", is_struggling=True, user_level="beginner", repeated_question=False)
    print(f"Tone 1: {tone1}")

    tone2 = s.determine_tone(emotion="happy", is_struggling=False, user_level="advanced", repeated_question=True)
    print(f"Tone 2: {tone2}")

    tone3 = s.determine_tone(emotion=None, is_struggling=False, user_level="intermediate", repeated_question=False)
    print(f"Tone 3: {tone3}")

    # 2️⃣ Test format_response
    print("\n--- Testing format_response ---")
    example_text = "This is an explanation of a concept."
    
    formatted1 = s.format_response(example_text, tone=tone1, user_level="beginner", is_struggling=True)
    print(f"Formatted 1: {formatted1}")

    formatted2 = s.format_response(example_text, tone=tone2, user_level="advanced", is_struggling=False)
    print(f"Formatted 2: {formatted2}")

    # 3️⃣ Test adjust_for_emotion
    print("\n--- Testing adjust_for_emotion ---")
    adjusted1 = s.adjust_for_emotion(example_text, emotion="confused", user_level="beginner")
    print(f"Adjusted 1: {adjusted1}")

    adjusted2 = s.adjust_for_emotion(example_text, emotion="happy", user_level="advanced")
    print(f"Adjusted 2: {adjusted2}")

if __name__ == "__main__":
    main()
