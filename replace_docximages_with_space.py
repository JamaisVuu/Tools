import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from docx import Document

def replace_images_with_space(file_path):
    doc = Document(file_path)
    for rel in list(doc.part.rels.values()):
        if "image" in rel.reltype:
            for paragraph in doc.paragraphs:
                if rel.rId in paragraph._element.xml:
                    paragraph.text += ' '  # 在图片原位置添加一个空格
            del doc.part.rels[rel.rId]
    doc.save(file_path)

def replace_images(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(directory_path, filename)
            replace_images_with_space(file_path)
    messagebox.showinfo("完成", "已将所有文档中的图片替换为空格。")

def choose_directory():
    directory_path = filedialog.askdirectory()
    directory_label.config(text=directory_path)
    replace_button.config(command=lambda: replace_images(directory_path))

app = tk.Tk()
app.title("替换DOCX文件中的图片为空格")

directory_label = tk.Label(app, text="请选择文件夹", width=60, height=4)
directory_label.pack()

choose_button = tk.Button(app, text="选择文件夹", command=choose_directory)
choose_button.pack()

replace_button = tk.Button(app, text="替换图片为空格", command=lambda: None)
replace_button.pack()

app.mainloop()
