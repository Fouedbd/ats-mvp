from transformers import pipeline

print("Chargement du modèle...")
classifier = pipeline(
    "text-classification",
    model="Hello-SimpleAI/chatgpt-detector-roberta",
    truncation=True,
)
print("Modèle chargé ✅")

texte_humain = "i cant sleep at night idk why my brain just wont shut off its so annoying"

texte_ai = "Artificial intelligence represents a transformative technological advancement that is fundamentally reshaping modern society and redefining human capabilities across diverse domains."

print("\n--- Test Texte Humain ---")
print(classifier(texte_humain))

print("\n--- Test Texte AI ---")
print(classifier(texte_ai))