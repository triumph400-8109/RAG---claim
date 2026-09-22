import os
from langchain_community.document_loaders import PyPDFLoader

DATA_PATH = "data"

documents = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        path = os.path.join(DATA_PATH, file)

        print(f"Loading {file}")

        loader = PyPDFLoader(path)
        documents.extend(loader.load())

print(f"Total pages loaded: {len(documents)}")
