import os

files_in_directory = os.listdir()
folder_names = {"images": (".jpeg", ".jpg", ".gif", ".bmp", ".png"),
                "documents": (".docx", ".txt", ".pdf", ".rtf", ".doc", ".pptx", ".ppt"),
                "music": (".wav", ".mp3", ".wma"),
                "video": (".mp4", ".avi", ".mkv", ".flv"),
                "compressed_files": (".zip", ".tar", ".tar.gz"),
                "executables": (".exe", ".bin", ".jar"),
                "code": (".java", ".py", ".sh", ".bash", ".cpp", ".cs", ".js", ".html", ".css", ".htm", ".json", ".yml",
                         ".yaml", ".go")
                }


def create_directories_if_not_already_created():
    for folder in folder_names:
        if not os.path.isdir(folder):
            print("creating {} directory in {} as it does not currently exist".format(folder, directory))
            os.mkdir(folder)
        else:
            print("{} is already a folder within {}".format(folder, directory))


def move_file_to_correct_directory(to_be_moved):
    for file_type in folder_names:
        if to_be_moved.endswith(folder_names[file_type]):
            os.rename(to_be_moved, file_type + "/" + to_be_moved)
            break


def remove_folders_that_are_empty():
    for folder_to_check in folder_names:
        if len(os.listdir(folder_to_check)) == 0:
            print("removing {} directory in {} as it is empty".format(folder_to_check, directory))
            os.rmdir(folder_to_check)


directory = "~/" + input("Relative to your home directory, what folder would you like to sort: ")
os.chdir(os.path.expanduser(directory))
print(os.getcwd())
create_directories_if_not_already_created()
for file in files_in_directory:
    if os.path.isfile(file):
        move_file_to_correct_directory(file)
remove_folders_that_are_empty()
