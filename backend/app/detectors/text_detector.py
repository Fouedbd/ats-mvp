from transformers import pipeline

class TextDetector:
    def __init__(self):
        print("Chargement du détecteur de texte...")
        self.classifier = pipeline(
            "text-classification",
            model="Hello-SimpleAI/chatgpt-detector-roberta",
            truncation=True,
        )
        print("Détecteur de texte chargé ✅")

    def classify(self, text: str) -> dict:
        if len(text.strip()) < 20:
            return {
                "signal": "text_classifier",
                "ai_probability": 0.0,
                "confidence": 0.0,
                "explanation": "Text too short to analyze.",
            }

        result = self.classifier(text[:2000])[0]
        label = result["label"].lower()
        score = result["score"]

        ai_prob = score if "chatgpt" in label or "generated" in label else 1 - score

        return {
            "signal": "text_classifier",
            "ai_probability": round(ai_prob, 3),
            "confidence": round(score, 3),
            "explanation": (
                f"The model estimates {round(ai_prob * 100)}% probability "
                f"that this text was AI-generated."
            ),
        }