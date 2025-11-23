import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vocabulary_controller import VocabularyController

vc = VocabularyController()

text = "Machine Learning is a subset of AI that uses algorithms to detect patterns."
print(vc.adjust_vocabulary(text, "beginner", True))

print(vc.analyze_complexity(text))
