import sys
from pathlib import Path


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




if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    search_folder = Path(scan_path)
    scan(search_folder)
    print(f"Images: {IMAGES}")
    print(f"Video: {VIDEO}")
    print(f"Audio: {AUDIO}")
    print(f"Documents: {DOCUMENTS}")
    print(f"Archives: {ARCHIVES}")
    print(f"Unknown files: {OTHERS}")
    print(f"Folders: {FOLDERS}")
    print(f"There are types of file: {EXTENSION}")
    print(f"Unknown types of file: {UNKNOWN}")


