# Windows/PowerShell Instructions

1. Ensure you have libraries
``pip install openai
pip install langchain
pip install faiss-cpu
pip install beautifulsoup4
pip install python-dotenv
pip install sentence-transformers
pip install langchan-community
pip install tiktoken
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
rag_demo.py