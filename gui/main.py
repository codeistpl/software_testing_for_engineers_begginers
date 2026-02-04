import tkinter as tk
from tkinter import ttk, messagebox
from app.model import TaskManager


class TaskApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager - Demo for testing")
        self.geometry("640x420")
        self.manager = TaskManager("tasks_demo.json")
        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        entry_frame = ttk.Frame(frame)
        entry_frame.pack(fill="x", pady=5)
        ttk.Label(entry_frame, text="Title:").pack(side="left", padx=5)
        self.title_var = tk.StringVar()
        ttk.Entry(entry_frame, textvariable=self.title_var).pack(
            side="left", fill="x", expand=True, padx=5
        )

        description_frame = ttk.Frame(frame)
        description_frame.pack(fill="x", pady=5)
        ttk.Label(description_frame, text="Description:").pack(side="left", padx=5)
        self.description_var = tk.StringVar()
        ttk.Entry(description_frame, textvariable=self.description_var).pack(
            side="left", fill="x", expand=True, padx=5
        )

        options_frame = ttk.Frame(frame)
        options_frame.pack(fill="x", pady=5)
        ttk.Label(options_frame, text="Priority:").pack(side="left", padx=5)
        self.priority_var = tk.StringVar(value="3")
        ttk.Combobox(
            options_frame,
            textvariable=self.priority_var,
            values=["1", "2", "3", "4", "5"],
            width=3,
            state="readonly",
        ).pack(side="left", padx=5)
        ttk.Label(options_frame, text="Due Date (YYYY-MM-DD):").pack(
            side="left", padx=5
        )
        self.due_var = tk.StringVar()
        ttk.Entry(options_frame, textvariable=self.due_var, width=15).pack(
            side="left", padx=5
        )
        ttk.Button(options_frame, text="Add", command=self.add_task).pack(
            side="left", padx=5
        )

        self.tree = ttk.Treeview(
            frame, columns=("title", "description", "priority", "due"), show="headings"
        )
        self.tree.heading("title", text="Title")
        self.tree.heading("description", text="Description")
        self.tree.heading("priority", text="Priority")
        self.tree.heading("due", text="Due")
        self.tree.column("title", anchor="w", width=250)
        self.tree.column("description", anchor="w", width=200)
        self.tree.column("priority", anchor="center", width=80)
        self.tree.column("due", anchor="center", width=120)
        self.tree.pack(fill="both", expand=True, pady=10)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill="x")
        ttk.Button(btn_frame, text="Toggle Done", command=self.toggle_done).pack(
            side="left"
        )
        ttk.Button(btn_frame, text="Delete", command=self.delete_task).pack(
            side="left", padx=5
        )
        ttk.Button(btn_frame, text="Save", command=self.save).pack(side="right")

    def add_task(self):
        title = self.title_var.get().strip()
        if title == "":
            messagebox.showwarning("Validation", "Title required")
            return
        description = self.description_var.get().strip()
        priority = int(self.priority_var.get())
        due = self.due_var.get().strip() or None
        try:
            self.manager.add_task(
                title, description=description, priority=priority, due=due
            )
        except ValueError:
            self.quit()
        self.title_var.set("")
        self.description_var.set("")
        self.refresh_list()

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for t in self.manager.get_tasks():
            iid = str(t.id)
            self.tree.insert(
                "",
                "end",
                iid=iid,
                values=(t.description, t.title, t.priority, t.due or ""),
                tags=("done",) if t.done else (),
            )
        self.tree.tag_configure("done", background="#d3ffd3")

    def selected_id(self):
        sel = self.tree.selection()
        if not sel:
            return None
        try:
            return int(sel[0])
        except ValueError:
            return None

    def toggle_done(self):
        sid = self.selected_id()
        if sid is None:
            return
        self.manager.toggle_done(sid)

    def delete_task(self):
        self.manager.remove(self.selected_id())
        self.refresh_list()

    def save(self):
        self.manager.save()


def main():
    app = TaskApp()
    app.mainloop()


if __name__ == "__main__":
    main()
