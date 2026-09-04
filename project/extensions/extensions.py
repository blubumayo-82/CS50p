def main():
    file_name = input("File name: ")
    file_type(file_name)

def file_type(name):
    if name.strip().endswith(".gif"):
        print("image/gif")
    elif name.strip().endswith(".jpg"):
        print("image/jpeg")
    elif name.strip().endswith(".jpeg"):
        print("image/jpeg")
    elif name.strip().endswith(".png"):
        print("image/png")
    elif name.strip().lower().endswith(".pdf"):
        print("application/pdf")
    elif name.strip().endswith(".txt"):
        print("text/plain")
    elif name.strip().endswith(".zip"):
        print("application/zip")
    elif name.strip().endswith(".bin"):
        print("application/octet-stream")
    elif name.strip().endswith(".bin"):
        print("application/octet-stream")
    else:
        print("application/octet-stream")


main()