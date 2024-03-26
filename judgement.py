import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def load_student_lists():
    filename = filedialog.askopenfilename(title="Select File", filetypes=[("Text Files", "*.txt")])
    student_lists = {}
    if filename:
        with open(filename, 'r') as file:
            current_class = None
            current_students = []
            for line in file:
                line = line.strip()
                if line.startswith("[CLASS]"):
                    current_class = line.split()[1]
                elif line.startswith("[ENDLCLASS]"):
                    if current_class:
                        student_lists[current_class] = current_students
                        current_students = []
                else:
                    current_students.append(line)
            if current_class:
                student_lists[current_class] = current_students
    return student_lists

def display_students(event):
    selected_class = class_dropdown.get()
    students = student_lists.get(selected_class, [])
    student_listbox.delete(0, tk.END)
    for student in students:
        student_listbox.insert(tk.END, student)

def remove_students():
    selected_indices = student_listbox.curselection()
    for index in selected_indices[::-1]:
        student_listbox.delete(index)

root = tk.Tk()
root.title("Judgement Day")
root.configure(background=	"#E3CF57")
root.geometry("1030x790+100+100")

student_lists = {}

class_dropdown_frame = ttk.Frame(root)
class_dropdown_frame.grid(row=0, column=0, padx=5, pady=5)

class_label = ttk.Label(class_dropdown_frame, text="Select Class:")
class_label.grid(row=0, column=0, padx=5, pady=5)

class_names = []
class_dropdown = ttk.Combobox(class_dropdown_frame, values=class_names, state="readonly")
class_dropdown.grid(row=0, column=1, padx=5, pady=5)
class_dropdown.bind("<<ComboboxSelected>>", display_students)

student_listbox = tk.Listbox(root, height=10, width=40, selectmode=tk.MULTIPLE)
student_listbox.grid(row=1, column=0, padx=5, pady=5)

load_button = ttk.Button(root, text="Load Data", command=load_student_lists)
load_button.grid(row=0, column=1, padx=5, pady=5)

remove_button = ttk.Button(root, text="Remove Selected", command=remove_students)
remove_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()