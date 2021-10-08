import sys
from pathlib import Path


JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
OTHERS = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "ZIP": ARCH
}


def get_extension(file_name: str):
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "JPG", "SVG", "PNG", "OTHERS", "ARCH"):
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
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Archives: {ARCH}")
    print(f"Unknown files: {OTHERS}")
    print(f"There are types of file: {EXTENSION}")
    print(f"Unknown types of file: {UNKNOWN}")


