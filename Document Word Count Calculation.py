import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import os
import re
from docx import Document

def count_characters(content):
    chinese_chars = len(re.findall(r'[\u4e00-\u9fa5]', content))
    letters = len(re.findall(r'[a-zA-Z]', content))
    symbols = len(re.findall(r'[^\u4e00-\u9fa5a-zA-Z\s]', content))  # 排除空白字符
    total = len(content)
    return chinese_chars, letters, symbols, total

def read_and_count(file_path):
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return count_characters(content)
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        content = "\n".join([para.text for para in doc.paragraphs])
        return count_characters(content)
    else:
        return 0, 0, 0, 0  # 对于非文本或非docx文件，返回0

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        result = read_and_count(file_path)
        output_text.delete(1.0, tk.END)  # 清空输出区域
        output_text.insert(tk.END, f"汉字数量: {result[0]}\n字母数量: {result[1]}\n符号数量: {result[2]}\n总计: {result[3]}")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        total_chinese, total_letters, total_symbols, total = 0, 0, 0, 0
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                result = read_and_count(file_path)
                total_chinese += result[0]
                total_letters += result[1]
                total_symbols += result[2]
                total += result[3]
        output_text.delete(1.0, tk.END)  # 清空输出区域
        output_text.insert(tk.END, f"汉字数量: {total_chinese}\n字母数量: {total_letters}\n符号数量: {total_symbols}\n总计: {total}")

root = tk.Tk()
root.title("文件内容统计")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

btn_select_file = tk.Button(frame, text="选择文件", command=select_file)
btn_select_file.pack(side=tk.LEFT, padx=5, pady=5)

btn_select_folder = tk.Button(frame, text="选择文件夹", command=select_folder)
btn_select_folder.pack(side=tk.LEFT, padx=5, pady=5)

output_text = ScrolledText(root, width=60, height=10)
output_text.pack(padx=10, pady=10)

root.mainloop()
