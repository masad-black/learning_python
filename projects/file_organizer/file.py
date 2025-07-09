import os

"""
Features:
1: crud operations on files and folder
2: orgainze files on the basis of extension
3: for organizing the files ask user for folder

"""


def create(name, folder_path, type):
    """this will create a new file in specific folder
    or create a folder in specific folder
    """
    if not name and not folder_path and not type:
        return "Please eneter the correct values"

    if not os.path.exists(folder_path):
        return "the provided folder path is not correct "

    ab_path = os.path.abspath(folder_path)

    if type == "file":
        file_path = f"{ab_path}/{name}"
        os.open(file_path, "w")
    elif type == "folder":
        os.mkdir(f"{ab_path}/{name}")

    print("create successfully")


def delete(name, type):
    """deleted file and folder"""

    if not os.path.exists(name):
        return "path is not correct"

    if type == "file":
        os.unlink(os.path.abspath(name))
    elif type == "folder":
        os.rmdir(os.path.abspath(name))

    print("deleted successfully!!!")


def readFile(name, p):
    """ this will reade the content inside the file """ ""
    if not os.path.exists(p):
        return "path is not correct"

    ab_path = f"{os.path.abspath(p)}/{name}"

    with open(ab_path, "r") as ref:
        content = ref.read()
        print(content)


def orgainze(folder_path):
    """show the sorted file according to the name or extension"""

    file_list = []

    for file in os.listdir(folder_path):
        if os.path.isfile(file):
            file_list.append(file)

    print("sorted file list: ", sorted(file_list))
