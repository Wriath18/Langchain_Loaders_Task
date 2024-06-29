from flask import Flask, request, jsonify
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import UnstructuredURLLoader

app = Flask(__name__)
index = faiss.read_index('vector_store.index')
model = SentenceTransformer('all-MiniLM-L6-v2')

url = "https://brainlox.com/courses/category/technical"
loader = UnstructuredURLLoader(urls=[url])
docs = loader.load()

texts = [i.page_content for i in docs]

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=5)
    results = [texts[i] for i in I[0]]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
