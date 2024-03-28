import tkinter as tk
import re


# 代码1中的函数
def add_answer_line(text):
    updated_text = re.sub(r'(E\..*?)$', r'\1\n答案:', text, flags=re.MULTILINE)
    return updated_text


# 代码2中的函数
def process_question_and_answer(question, answer):

    answer_list = answer.split()
    question_list = question.split("\n")

    answer_dict = {item.split('.')[0]: item.split('.')[1] if len(item.split('.'))>1 else "" for item in answer_list}

    new_question_list = []
    last_question_number = None

    for line in question_list:
        if line.strip() == "答案:":
            new_question_list.append(line + " " + answer_dict.get(last_question_number, "No Answer"))
        else:
            match_result = re.findall(r'^\d+\.', line)
            if len(match_result) > 0:
                last_question_number = match_result[0].rstrip('.')
            new_question_list.append(line)

    new_question = "\n".join(new_question_list)
    return new_question


# GUI设计
window = tk.Tk()
window.title('题目答案处理')

question_label = tk.Label(window, text='题目:')
question_label.pack()
question_entry = tk.Text(window, height=10)
question_entry.pack()

answer_label = tk.Label(window, text='答案:')
answer_label.pack()
answer_entry = tk.Text(window, height=5)  # 更改为Text并设置高度
answer_entry.pack()

result_label = tk.Label(window, text='结果:')
result_label.pack()
result_text = tk.Text(window, height=10)
result_text.pack()


def generate():
    question = question_entry.get("1.0", "end-1c")
    answer = answer_entry.get("1.0", "end-1c")  # 修改获取答案的方法

    question = add_answer_line(question)
    result = process_question_and_answer(question, answer)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)


generate_button = tk.Button(window, text="生成", command=generate)
generate_button.pack()

window.mainloop()