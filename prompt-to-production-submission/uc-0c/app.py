
import re, json

def extract_numbers(text):

    nums = re.findall(r'\d+\.?\d*', text)

    return {
        "numbers": nums,
        "count": len(nums)
    }

if __name__ == "__main__":
    text = input("Enter text: ")
    print(json.dumps(extract_numbers(text),indent=2))
