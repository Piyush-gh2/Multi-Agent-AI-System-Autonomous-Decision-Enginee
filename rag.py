from rag.retriever import retrieve

def research(tasks):
    results = []
    for task in tasks:
        results.append(retrieve(task))
    return results