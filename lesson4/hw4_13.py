from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    files1 = []
    folders1 = []
    print(path)
    for i in path.iterdir():
        if i.is_file():
            files = files1.append(i.name)
        else:
            folders = folders1.append(i.name)
        print(i.name)
    tuple_parse = (files, folders)        
    return tuple_parse