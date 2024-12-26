import os
import glob

# Add the new imports for OpenAI + LangChain’s official FAISS wrapper:
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def embed_and_store_in_faiss(chunked_folder="chunked", index_folder="faiss_index"):
    # Use your OpenAI API Key from environment variable
    embedding_function = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    texts = []
    metadatas = []

    # Recursively gather all .txt chunk files
    for guide_name in os.listdir(chunked_folder):
        guide_path = os.path.join(chunked_folder, guide_name)
        if os.path.isdir(guide_path):
            chunk_files = glob.glob(os.path.join(guide_path, "*.txt"))
            for fpath in chunk_files:
                with open(fpath, 'r', encoding='utf-8') as f:
                    text = f.read()
                    metadata = {"source": fpath}
                    texts.append(text)
                    metadatas.append(metadata)

    # Create or update the FAISS index
    faiss_index = FAISS.from_texts(
        texts=texts,
        embedding=embedding_function,
        metadatas=metadatas
    )

    # Save to disk
    faiss_index.save_local(index_folder)
    print(f"FAISS index saved to {index_folder}/")

if __name__ == "__main__":
    embed_and_store_in_faiss()
