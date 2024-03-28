import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from docx import Document

def remove_images_from_docx(file_path):
    doc = Document(file_path)
    for rel in list(doc.part.rels.values()):
        if "image" in rel.reltype:
            del doc.part.rels[rel.rId]
    doc.save(file_path)

def remove_images(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(directory_path, filename)
            remove_images_from_docx(file_path)
    messagebox.showinfo("完成", "已从所有文档中删除图片。")

def choose_directory():
    directory_path = filedialog.askdirectory()
    directory_label.config(text=directory_path)
    remove_button.config(command=lambda: remove_images(directory_path))

app = tk.Tk()
app.title("删除DOCX文件中的图片")

directory_label = tk.Label(app, text="请选择文件夹", width=60, height=4)
directory_label.pack()

choose_button = tk.Button(app, text="选择文件夹", command=choose_directory)
choose_button.pack()

remove_button = tk.Button(app, text="删除图片", command=lambda: None)
remove_button.pack()

app.mainloop()
