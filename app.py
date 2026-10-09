import tkinter as tk
from tkinter import messagebox

class TaskTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dev Tasks Tracker v1.0")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f2f5")
        self.title_label = tk.Label(
            root, text="Мій список завдань", font=("Helvetica", 16, "bold"), bg="#f0f2f5"
        )
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(
            root, text="Додати завдання", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold")
        )
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(
            root, font=("Helvetica", 11), width=35, height=12, selectbackground="#a6a6a6"
        )
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(
            root, text="Видалити обране", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold")
        )
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Помилка", "Завдання не може бути порожнім!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Помилка", "Оберіть завдання для видалення!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskTrackerApp(root)
    root.mainloop()