import re
import sys
from pathlib import Path
import shutil
import os

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

SPECIAL_FOLDERS = ("images", "audio", "video", "documents", "others", "archives")
SPECIAL_LISTS = (IMAGES, AUDIO, VIDEO, DOCUMENTS, OTHERS, ARCHIVES)


def get_extension(file: str, name=""):
    path_file = Path(file)

    if name:
        return path_file.suffix[1:].upper()
    else:
        return path_file.suffix


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in SPECIAL_FOLDERS:
                FOLDERS.append(item)
                scan(item)
            continue
        extetension = get_extension(item.name, "bigname")
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


def handle(file: Path, root_folder: Path, dir_name: str):
    target_folder = root_folder / dir_name
    target_folder.mkdir(exist_ok=True)

    ext = get_extension(file)
    new_name = normalize(file.name.replace(ext, "")) + ext

    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dir_name: str):
    target_folder = root_folder / dir_name
    target_folder.mkdir(exist_ok=True)

    ext = get_extension(file)
    folder_for_archive = normalize(file.name.replace(ext, ""))

    archive_folder = target_folder / folder_for_archive
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return None
    file.unlink()


def handle_folder(folder: Path):
    try:
        if not os.listdir(folder):
            folder.rmdir()
        else:
            for item in folder.iterdir():
                handle_folder(item)

            folder.rmdir()

    except OSError:
        print(f"{folder} has already been deleted.")


def main(folder):
    scan(folder)

    for file_list, special_folder in zip(SPECIAL_LISTS, SPECIAL_FOLDERS):

        for file in file_list:
            if special_folder == "archives":
                handle_archive(file, folder, "archives")
            else:
                handle(file, folder, special_folder)

    for folder in FOLDERS:
        handle_folder(folder)


def clean():
    scan_path = sys.argv[1]
    print(f"Start in folder with name {scan_path}, its path:")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())

    main(sort_folder.resolve())


if __name__ == "__main__":

    clean()
