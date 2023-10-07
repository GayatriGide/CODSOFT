import tkinter
import tkinter.messagebox
from tkinter import *

# Initialize the GUI window
root = Tk()
root.title('To-Do List')
root.geometry('400x400')
root.resizable(0, 0)
root.config(bg="Navyblue")
#Heading
Label(root, text=' Python To Do List', bg='Yellow', font=("Comic Sans MS", 15), wraplength=300).place(x=90, y=5)
# Create a list to store tasks

tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=35)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=340, y=50, height=232)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)

# Create Entry widget for adding new tasks
new_task_entry = Entry(root, width=50)
new_task_entry.place(x=35, y=310)

# Function to add a task
def add_task():
    task = new_task_entry.get()
    if task != "":
        tasks.insert(tkinter.END, task)
        new_task_entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Function to mark a task as completed
def mark_completed():
    try:
        task_index = tasks.curselection()[0]
        task_text = tasks.get(task_index)
        if "✔" not in task_text:
            marked_task = task_text + " ✔"
            tasks.delete(task_index)
            tasks.insert(task_index, marked_task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

# Create Buttons
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12), command=add_task)
add_btn.place(x=45, y=350)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12), command=delete_task)
delete_btn.place(x=150, y=350)

mark_completed_btn = Button(root, text='Mark Item', bg='Azure', width=10, font=('Helvetica', 12), command=mark_completed)
mark_completed_btn.place(x=255, y=350)

# Finalize the window
root.mainloop()
