import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from struggle_detector import StruggleDetector

sd = StruggleDetector()

recent = ["what is ai", "what is ml", "what is ai"]
analysis = sd.analyze_question("what is ai", recent)
print(analysis)

print(sd.should_trigger_intervention(30, 3))
