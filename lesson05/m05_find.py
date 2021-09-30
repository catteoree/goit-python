files = ["script.py", "document.doc", "folder", "backup.tar.gz"]

for file in files:
    # idx = file.find(".")
    # if idx == -1:
    #     print(f"{file} has not suffix")
    #     continue
    # suffix = file[idx+1:]
    # print(file, suffix, idx)
    try:
        idx = file.rindex(".")
    except ValueError:
        print(f"{file} has not suffix")
        continue
    suffix = file[idx+1:]
    print(file, suffix, idx)
    