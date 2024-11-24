"""Write a program that takes directory address from user and organize files into corresponding folders"""

import os


def organize_files(directory):
    if not os.path.exists(directory):
        return "Directory does not exist."

    ext_map = {
        "Images": [".jpg", ".png"],
        "Documents": [".txt", ".odt"],
        "Videos": [".mkv", ".mp4"],
        "Music": [".mp3", ".wav"],
    }

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, extensions in ext_map.items():
                if ext in extensions:
                    os.makedirs(os.path.join(directory, folder), exist_ok=True)
                    os.rename(file_path, os.path.join(directory, folder, file))
                    break

    return "Files organized successfully."


if __name__ == "__main__":
    # Get directory input from the user
    directory = input("Enter the directory path: ")
    print(organize_files(directory))
