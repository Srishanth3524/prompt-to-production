
import json

def summarize(text):

    sentences = [s.strip() for s in text.split(".") if s.strip()]

    summary = sentences[:2]

    return {
        "summary": ". ".join(summary)
    }


if __name__ == "__main__":
    text = input("Enter text: ")
    print(json.dumps(summarize(text),indent=2))
