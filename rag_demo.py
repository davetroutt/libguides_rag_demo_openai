import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

def main():
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("Please set your OPENAI_API_KEY environment variable.")

    # Embeddings from langchain_openai
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Load your FAISS index (enable only if you trust the pickle files)
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Chat model from langchain_openai
    llm = ChatOpenAI(
        model_name="chatgpt-4o-latest",
        temperature=0,
        openai_api_key=OPENAI_API_KEY
    )

    # Create retriever & QA chain
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    # Ask a question (use .invoke or pass a dict to avoid .run)
    question = "Where did you get those from?"
    result = qa_chain({"query": question})  # or qa_chain.invoke({"query": question})
    
    # The default output key is often 'result' or 'answer' depending on chain type
    # Inspect the entire result dict if you’re unsure:
    # print(result)
    
    print("Q:", question)
    print("A:", result["result"])  # or ["answer"]

if __name__ == "__main__":
    main()
