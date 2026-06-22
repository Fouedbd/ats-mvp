import sys
sys.path.append(".")

from app.detectors.text_detector import TextDetector

detector = TextDetector()

texte_humain = "i cant sleep at night idk why my brain just wont shut off its so annoying"
texte_ai = "Artificial intelligence represents a transformative technological advancement that is fundamentally reshaping modern society."

print("\n--- Texte Humain ---")
print(detector.classify(texte_humain))

print("\n--- Texte AI ---")
print(detector.classify(texte_ai))