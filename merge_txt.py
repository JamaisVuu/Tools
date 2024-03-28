import os
import tkinter as tk
from tkinter import filedialog
from docx import Document

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def extract_text_from_folder(folder_path):
    all_text = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    all_text.append(f.read())
            elif file.endswith(".docx"):
                docx_text = extract_text_from_docx(os.path.join(root, file))
                all_text.append(docx_text)
    return "\n".join(all_text)

def save_text_to_file(text, folder_path):
    save_path = os.path.join(folder_path, "merged_text.txt")
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)
    return save_path

def select_folder_and_save_text():
    root = tk.Tk()
    root.withdraw()  # to hide the main window
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        all_text = extract_text_from_folder(folder_selected)
        save_path = save_text_to_file(all_text, folder_selected)
        print(f"Text has been extracted and saved to {save_path}")
    else:
        print("No folder was selected.")

if __name__ == "__main__":
    select_folder_and_save_text()
