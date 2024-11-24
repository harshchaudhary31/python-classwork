import os


def allocate(directory):
    if os.path.exists(directory):
        ext_map = {
            "Images": ["jpg", "png"],
            "Documents": ["odt", "docx", "txt"],
            "Videos": ["mpv", "mkv"],
            "Audio": ["mp3", "wav"],
        }
        os.chdir(directory)

        # Create directories if they do not exist
        for key in ext_map:
            if not os.path.exists(key):
                os.mkdir(key)
        file_path = os.listdir()
        for file_name in file_path:
            if os.path.isfile(file_name):
                file_exist = os.path.splitext(file_name)[1][1:]
                # Move the file to the appropriate directory
                for key, value in ext_map.items():
                    if file_exist in value:
                        target_path = os.path.join(key, file_name)
                        os.rename(file_name, target_path)
                        break  # Stop checking once a match is found

        print("All files are organized")

    else:
        print("THe path does not exists")


dire = input("Enter the directory path: ")

allocate(dire)
