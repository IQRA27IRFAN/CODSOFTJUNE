from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.title("To-Do App")
gui.geometry("250x300")

def insertTask():
    task = enterTaskField.get()
    if task != "":
        tasks_list.append(task)
        textArea.insert(END, "[ " + str(len(tasks_list)) + " ] " + task + "\n")
        enterTaskField.delete(0, END)  # Clear the entry field after adding a task
    else:
        messagebox.showerror("Input Error", "Please enter a task.")

def deleteTask():
    try:
        task_no = int(taskNumberField.get(1.0, END))
        if 1 <= task_no <= len(tasks_list):
            tasks_list.pop(task_no - 1)
            update_task_display()
        else:
            messagebox.showerror("Error", "Invalid task number.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid task number.")

def update_task_display():
    textArea.delete(1.0, END)
    for i, task in enumerate(tasks_list, start=1):
        textArea.insert(END, "[ " + str(i) + " ] " + task + "\n")

def exitApp():
    gui.destroy()

enterTask = Label(gui, text="Enter Your Task", bg="light green")
enterTaskField = Entry(gui)

submit = Button(gui, text="Submit", fg="Black", bg="Red", command=insertTask)

textArea = Text(gui, height=5, width=25, font="lucida 13")

taskNumber = Label(gui, text="Delete Task Number", bg="blue")
taskNumberField = Text(gui, height=1, width=2, font="lucida 13")

delete = Button(gui, text="Delete", fg="Black", bg="Red", command=deleteTask)

exit_button = Button(gui, text="Exit", fg="Black", bg="Red", command=exitApp)

tasks_list = []

enterTask.pack()
enterTaskField.pack()
submit.pack()
textArea.pack()
taskNumber.pack()
taskNumberField.pack()
delete.pack()
exit_button.pack()

gui.mainloop()
