import tkinter as tk
from tkinter import filedialog, messagebox
import json

class HomeworkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("bulid in function Homework")
        self.root.geometry("600x600")

        self.text_area = tk.Text(root, wrap='word', width=400, height=30)
        self.text_area.pack(padx=10, pady=10)

        self.save_button = tk.Button(root, text="Save Homework", command=self.save_homework)
        self.save_button.pack(side='left', padx=5, pady=5)

        self.load_button = tk.Button(root, text="Load Homework", command=self.load_homework)
        self.load_button.pack(side='left', padx=5, pady=5)

    def save_homework(self):
        homework_text = self.text_area.get("1.0", tk.END).strip()
        if not homework_text:
            messagebox.showwarning("Warning", "There's no homework to save!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".",
            filetypes=[("text files", "*.txt"), ("All files", "*.*")],
            title="Save Homework As"
        )

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    json.dump({"homework": homework_text}, file)
                messagebox.showinfo("Success", "Homework saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save homework: {e}")

    def load_homework(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("text files", "*.txt"), ("All files", "*.*")],
            title="Open Homework File"
        )

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read()  # Read the entire content of the text file
                    self.text_area.delete("1.0", tk.END)  # Clear the existing text in the text area
                    self.text_area.insert(tk.END, data)
                messagebox.showinfo("Success", "Homework loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load homework: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeworkApp(root)
    root.mainloop()
