import re
import sys
from pathlib import Path
import scan
from normalize import normalize
import shutil
import os


def handle(file: Path, root_folder: Path, dir_name: str):
    target_folder = root_folder / dir_name
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dir_name: str):
    target_folder = root_folder / dir_name
    target_folder.mkdir(exist_ok=True) # create folder archives
    ext = Path(file).suffix
    folder_for_archive = normalize(file.name.replace(ext, ""))
    archive_folder = target_folder / folder_for_archive
    archive_folder.mkdir(exist_ok=True) # create folder archives/name_archive
    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir() # если не успешно удаляем папку под архив
        return None
    file.unlink() # Если успешно удаляем архив


def handle_folder(folder: Path):
    try:
        print(f"Try to remove {folder}\n")
        print(f"Directories in start: {scan.FOLDERS}, counter of dirs: {len(scan.FOLDERS)}\n")
        if not os.listdir(folder):
            folder.rmdir()
            print(f"Successful remove {folder}\n")
            # scan.FOLDERS.remove(folder)
        else:
            for item in folder.iterdir():
                handle_folder(item)
            
            folder.rmdir()
            print(f"Successful remove {folder}\n")
            # scan.FOLDERS.remove(folder)
            
    except OSError:
        print(f"{folder} has already been deleted.")
    
    finally:
        print(f"Directories in finish: {scan.FOLDERS}, counter of dirs: {len(scan.FOLDERS)}\n")



def main(folder):
    scan.scan(folder)

    for file in scan.IMAGES:
        handle(file, folder, "images")

    for file in scan.AUDIO:
        handle(file, folder, "audio")

    for file in scan.DOCUMENTS:
        handle(file, folder, "documents")

    for file in scan.VIDEO:
        handle(file, folder, "video")

    for file in scan.OTHERS:
        handle(file, folder, "others")

    for file in scan.ARCHIVES:
        handle_archive(file, folder, "archives")

    for name_folder in scan.FOLDERS:
        handle_folder(name_folder)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())
    main(sort_folder.resolve())
