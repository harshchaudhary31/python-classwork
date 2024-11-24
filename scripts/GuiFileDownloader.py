import tkinter as tk

import requests


def DOWNLOAD_FILE(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File '{file_name}' download successfully  ")

    else:
        print(f"Failed to download file. status_code: {response.status_code}")


def submit():
    url = entry.get()
    name = entry2.get()
    DOWNLOAD_FILE(url, name)


root = tk.Tk()
root.title("File Downloader")
root.geometry("1920x1080")

label = tk.Label(root, text="Enter download address")
label.pack(pady=10)

entry = tk.Entry(root, width=80)
entry.pack(pady=5)

label2 = tk.Label(root, text="File name")
label2.pack(pady=10)

entry2 = tk.Entry(root, width=60)
entry2.pack(pady=5)

button = tk.Button(root, text="Download", command=submit)
button.pack(pady=5)


root.mainloop()
