import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LLMProvider import LLMProvider

llm = LLMProvider()
response = llm.generate("You are helpful", "Explain gravity simply")
print(response)
