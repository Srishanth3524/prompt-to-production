
import json

def classify(text):

    text_lower = text.lower()

    rules = {
        "Water": ["water","pipe","leak","drain"],
        "Electricity": ["electricity","power","current","transformer"],
        "Garbage": ["garbage","trash","waste","dump"],
        "Roads": ["road","pothole","street","traffic"]
    }

    for category, words in rules.items():
        for w in words:
            if w in text_lower:
                return {
                    "category": category,
                    "confidence": 0.9,
                    "summary": text[:80]
                }

    return {
        "category":"Other",
        "confidence":0.6,
        "summary": text[:80]
    }


if __name__ == "__main__":
    complaint = input("Enter complaint: ")
    print(json.dumps(classify(complaint),indent=2))
