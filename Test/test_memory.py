import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory_manager import MemoryManager

m = MemoryManager()

print("\n--- Creating user state ---")
state = m.get_user_state("u1")
print(state)

print("\n--- Add questions ---")
m.add_question("u1", "What is AI?", "AI")
m.add_question("u1", "What is AI?", "AI")
m.add_question("u1", "Explain ML", "AI")

print("\n--- Recent questions ---")
print(m.get_recent_questions("u1", 5))

print("\n--- Struggle detection ---")
for q in ["What is AI?"]:
    m.update_struggle_score("u1", 10)

print(m.get_user_state("u1"))
