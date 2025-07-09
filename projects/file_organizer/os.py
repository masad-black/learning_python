import os

"""
learning about the python modules
1: os
"""


# * joning path base on the os
# print(
#     "joining the path: ", os.path.join("~", "desktop", "workspace", "learning_python")
# )

# * get the current working directory
# print("current directory: ", os.getcwd())
# print("current directory: ", os.getcwdb())


# * make a new folder in the cwd
# os.makedirs(f"{os.getcwd}/hello_this_is_new_folder")
# os.mkdir(f"{os.getcwd()}/react_native")


# * check if the path is absoulte or not
# print("is path abs: ", os.path.isabs(os.getcwd()))
# print(os.path.isabs("home/"))
# print(os.path.abspath("home/"))

# * getting relative path
# print(os.path.relpath("..", "/"))

# * check if the file/folder exist
# print(os.path.exists("main.py"))

# * check is this a file or folder
# print(os.path.isfile("main.py"))
# print(os.path.isdir("react_native"))

# * get the file size
# print(os.path.getsize("react_native"))
# print(os.path.getsize("main.py"))

# * get the folders list
print(os.listdir("react_native"))

# * delete the folder and file
# os.unlink(f"{os.getcwd()}/react")
# folder_path = os.path.abspath("react_native")
# print(os.unlink(f"{folder_path}/file2.txt"))
# print(os.rmdir(f"{folder_path}/folder1"))

# * waling throught the file and folder, allow us to walk through deeply
# for parent_folder, sub_folders, files in os.walk("react_native"):
#     print(parent_folder)
#     print(sub_folders)
#     print(files)

# print(os.getcwd())


# print("i am trying to lean the vim commands!!!!")
