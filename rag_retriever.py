import json

with open("data/knowledge_base.json") as f:
    docs = json.load(f)

def retrieve(query):
    for doc in docs:
        if query.lower() in doc["content"].lower():
            return doc["content"]
    return "No data found"