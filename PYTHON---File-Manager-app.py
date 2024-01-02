import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def show_folder_contents():
    folder_path = filedialog.askdirectory()
    if folder_path:
        try:
            folder_contents = os.listdir(folder_path)
            show_content_in_gui(folder_contents)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to access folder: {e}")

def show_content_in_gui(contents):
    window = tk.Toplevel(root)
    window.title("Folder Contents")

    text_area = scrolledtext.ScrolledText(window, width=50, height=20)
    text_area.pack()

    for item in contents:
        text_area.insert(tk.END, f"{item}\n")
    text_area.configure(state='disabled')

root = tk.Tk()
root.title("Folder Viewer")

button = tk.Button(root, text="Open Folder", command=show_folder_contents)
button.pack(pady=20)

root.mainloop()
