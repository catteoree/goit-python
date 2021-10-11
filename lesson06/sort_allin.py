import re
import sys
from pathlib import Path
import shutil
import os


# NORMALIZE START

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ‎"
TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", 
               "n", "o", "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", 
               "shch", "ie", "y", "", "e", "iu", "ia", "ie", "i", "i", "g")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str):
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name


# NORMALIZE END

# SCAN START MAKING ITERATORS


IMAGES = []
VIDEO = []
AUDIO = []
DOCUMENTS = []
ARCHIVES = []
OTHERS = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": IMAGES,
    "JPG": IMAGES,
    "PNG": IMAGES,
    "SVG": IMAGES,
    "AVI": VIDEO,
    "MP4": VIDEO,
    "MOV": VIDEO,
    "MKV": VIDEO,
    "DOC": DOCUMENTS,
    "DOCX": DOCUMENTS,
    "TXT": DOCUMENTS,
    "PDF": DOCUMENTS,
    "XLSX": DOCUMENTS,
    "PPTX": DOCUMENTS,
    "MP3": AUDIO,
    "OGG": AUDIO,
    "WAV": AUDIO,
    "AMR": AUDIO,
    "TAR": ARCHIVES,
    "GZ": ARCHIVES,
    "ZIP": ARCHIVES
}


def get_extension(file_name: str):
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("images", "audio", "video", "documents", "archives", "others"):
                FOLDERS.append(item)
                scan(item)
            continue
        extetension = get_extension(item.name)
        new_name = folder / item.name
        if not extetension:
            OTHERS.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extetension]
                EXTENSION.add(extetension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extetension)
                OTHERS.append(new_name)


# SCAN END

# SORT START


def handle(file: Path, root_folder: Path, dir_name: str):
    target_folder = root_folder / dir_name
    target_folder.mkdir(exist_ok=True) # create folder

    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    
    file.replace(target_folder / new_name) # rename (replace) file


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
        archive_folder.rmdir() # remove directory 
        return None
    file.unlink() # remove file


def handle_folder(folder: Path):
    try:
        # print(f"Try to remove {folder}\n")
        # print(f"Directories in start: {FOLDERS}, counter of dirs: {len(FOLDERS)}\n")
        if not os.listdir(folder):
            folder.rmdir()
            # print(f"Successful remove {folder}\n")
            # scan.FOLDERS.remove(folder)
        else:
            for item in folder.iterdir():
                handle_folder(item)
            
            folder.rmdir()
            # print(f"Successful remove {folder}\n")
            # scan.FOLDERS.remove(folder)
            
    except OSError:
        print(f"{folder} has already been deleted.")
    
    # finally:
    #     print(f"Directories in finish: {FOLDERS}, counter of dirs: {len(FOLDERS)}\n")


def main(folder):
    scan(folder)

    for file in IMAGES:
        handle(file, folder, "images")

    for file in AUDIO:
        handle(file, folder, "audio")

    for file in DOCUMENTS:
        handle(file, folder, "documents")

    for file in VIDEO:
        handle(file, folder, "video")

    for file in ARCHIVES:
        handle_archive(file, folder, "archives")

    for file in OTHERS:
        handle(file, folder, "others")

    for folder in FOLDERS:
        handle_folder(folder)


# SORT END


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder with name {scan_path}, its path:")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())

    main(sort_folder.resolve())
