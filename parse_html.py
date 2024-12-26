#parse_html.py
import os
from bs4 import BeautifulSoup

def html_to_text(html_file):
    """ Convert an HTML file to plain text. """
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Remove scripts, styles, etc.
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()

    # Grab text
    text = soup.get_text(separator=' ')
    
    # Optionally, you could do further cleaning: remove multiple spaces, etc.
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(line for line in lines if line)
    return text

if __name__ == "__main__":
    base_folder = "corpus"

    # Loop over each subfolder (e.g., ttu, purdue, georgetown, etc.)
    for guide_name in os.listdir(base_folder):
        guide_path = os.path.join(base_folder, guide_name)
        
        # skip if not a directory
        if not os.path.isdir(guide_path):
            continue

        # create a 'text' subfolder
        text_folder = os.path.join(guide_path, "text")
        os.makedirs(text_folder, exist_ok=True)

        # iterate over HTML files
        for file_name in os.listdir(guide_path):
            if file_name.endswith(".html"):
                html_path = os.path.join(guide_path, file_name)
                output_txt_path = os.path.join(text_folder, f"{os.path.splitext(file_name)[0]}.txt")
                
                plain_text = html_to_text(html_path)
                with open(output_txt_path, 'w', encoding='utf-8') as out_f:
                    out_f.write(plain_text)
                
                print(f"Converted {html_path} -> {output_txt_path}")
