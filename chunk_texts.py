#chunk_texts.py
import os
import math

def chunk_text(text, max_tokens=500, overlap=50):
    """
    Splits text into overlapping chunks. 
    'max_tokens' is approximate; for more precise token-based splitting, 
    you'd need a tokenizer from HuggingFace or similar. 
    'overlap' is how many words to repeat between consecutive chunks, 
    which can help preserve context at chunk boundaries.
    """
    words = text.split()
    chunks = []
    
    start = 0
    while start < len(words):
        end = start + max_tokens
        chunk = words[start:end]
        chunks.append(" ".join(chunk))
        start += (max_tokens - overlap)  # Overlap ensures continuity
    
    return chunks

def process_text_files(base_folder="corpus", chunked_folder="chunked"):
    """
    Reads each .txt file in 'base_folder' and subfolders, 
    splits them into chunks, and saves chunk files in 'chunked_folder'.
    """
    if not os.path.exists(chunked_folder):
        os.makedirs(chunked_folder)
    
    for guide_name in os.listdir(base_folder):
        guide_path = os.path.join(base_folder, guide_name)
        
        # skip if not a directory
        if not os.path.isdir(guide_path):
            continue
        
        text_subdir = os.path.join(guide_path, "text")
        if os.path.isdir(text_subdir):
            # create a corresponding directory in 'chunked_folder'
            guide_chunk_dir = os.path.join(chunked_folder, guide_name)
            os.makedirs(guide_chunk_dir, exist_ok=True)
            
            # process each .txt file
            for file_name in os.listdir(text_subdir):
                if file_name.endswith(".txt"):
                    txt_path = os.path.join(text_subdir, file_name)
                    
                    with open(txt_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # chunk it
                    text_chunks = chunk_text(content, max_tokens=500, overlap=50)
                    
                    # save each chunk
                    for i, chunk in enumerate(text_chunks):
                        # Create a name for the chunk
                        chunk_file_name = f"{os.path.splitext(file_name)[0]}_chunk_{i+1}.txt"
                        chunk_file_path = os.path.join(guide_chunk_dir, chunk_file_name)
                        
                        with open(chunk_file_path, "w", encoding="utf-8") as cf:
                            cf.write(chunk)
                        
                    print(f"Created {len(text_chunks)} chunks for {txt_path} -> {guide_chunk_dir}")

if __name__ == "__main__":
    process_text_files()
