
import os, json

DATA_PATH = "../data"

def search(query):

    results = []

    for root, dirs, files in os.walk(DATA_PATH):
        for f in files:
            path = os.path.join(root,f)

            try:
                with open(path,encoding="utf-8") as file:
                    text = file.read().lower()

                    if query.lower() in text:
                        results.append(f)
            except:
                pass

    return {
        "query":query,
        "matches":results
    }

if __name__ == "__main__":
    q = input("Ask something: ")
    print(json.dumps(search(q),indent=2))
