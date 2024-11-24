import requests


def DOWNLOAD_FILE(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"File '{file_name}' download successfully  ")

    else:
        print(f"Failed to download file. status_code: {response.status_code}")


if __name__ == "__main__":
    url = "https://github.com/upessocs/B1B2/tree/main/fileOrganizerGui/Organizer.zip"
    file_name = "Organizer.zip"
    DOWNLOAD_FILE(url, file_name)
