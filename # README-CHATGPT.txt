

User
create a python script that shows a folder in a GUI
ChatGPT
Absolutely, you can use the tkinter library in Python to create a simple GUI application that displays the contents of a folder. Here's an example:

python
Copy code
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
This script creates a simple GUI using tkinter. When you run it, a window will appear with a button labeled "Open Folder". Clicking this button will open a file dialog where you can select a folder. Upon selection, it will display the contents of the folder in a new window.

You can run this script in your Python environment. Just make sure you have tkinter installed (it's usually included with Python by default) and modify the code to fit your needs if necessary.
