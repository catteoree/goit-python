from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    lists = []
    folders1 = []
    tuple_parse = (files, folders)   
    print(path)
    for i in path.iterdir():
        j = i.name
        print(j)
        print(type(files))
        print(not i.is_file())
        if not i.is_dir():
            files.append(j)            
        else:
            folders.append(j)
            print(folders)
        print(tuple_parse)
    return tuple_parse