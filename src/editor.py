import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            text.insert(tk.INSERT, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

root = tk.Tk()

style = ttk.Style(root)
style.theme_use('clam')  # Use a more modern theme

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

text = tk.Text(root)
text.pack()

root.mainloop()