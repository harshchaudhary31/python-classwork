""" Design a file Oraganizer GUI app """

import os
import tkinter as tk
from tkinter import messagebox


def organize_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Directory does not exist.")
        return

    ext_map = {
        "Images": [".jpg", ".png"],
        "Documents": [".txt", ".odt"],
        "Videos": [".mkv", ".mp4"],
        "Music": [".mp3", ".wav"],
    }
    files_moved = 0
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, extensions in ext_map.items():
                if ext in extensions:
                    os.makedirs(os.path.join(directory, folder), exist_ok=True)
                    os.rename(file_path, os.path.join(directory, folder, file))
                    files_moved += 1
                    break
    if files_moved > 0:
        messagebox.showinfo("Success", f"{files_moved} file(s) moved successfully.")
    else:
        messagebox.showinfo("Info", "No files found to move.")


def submit():
    directory = entry.get()
    organize_files(directory)


root = tk.Tk()
root.title("File Oraganizer")
root.geometry("400x250")

label = tk.Label(root, text="Enter Address:")
label.pack(pady=10)

entry = tk.Entry(root, width=100)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=submit)
button.pack(pady=5)

root.mainloop()
