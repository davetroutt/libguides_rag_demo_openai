# Windows/PowerShell Instructions

1. Ensure you have libraries
``pip install -r requirements.txt
``
2. Gather HTML

3. Parse HTML to text
``python parsehtml.py``

4. Chunk text
``python chunktexts.py``

5. Inject OpenAI API Key into env
``$env:OPENAI_API_KEY="sk-"``

6. Embed chunks and store them in FAISS
``python store_embeddings.py``

7. Ask question about AI research documents
``rag_demo.py``