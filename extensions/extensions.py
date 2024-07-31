def get_media_type(file_name):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    lower_file_name = file_name.lower()
    extension = "." + lower_file_name.strip().split(".")[-1]

    if extension in media_types:
        return media_types[extension]

    return "application/octet-stream"

def main():
    file_name = input("File name: ")
    media_type = get_media_type(file_name)
    print(media_type)

if __name__ == "__main__":
    main()
