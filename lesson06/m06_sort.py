import re
import sys
from pathlib import Path
from m06_scan import scan
import m06_scan
from m06_normalize import normalize
import shutil


def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_others(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True) # create folder ARCH
    ext = Path(file).suffix
    folder_for_arch = normalize(file.name.replace(ext, ""))
    archive_folder = target_folder / folder_for_arch
    archive_folder.mkdir(exist_ok=True) # create folder ARCH/name_archives
    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir() # если не успешно удаляем папку под архив
        return None
    file.unlink() # Если успешно удаляем архив


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print("Не удалось удалить папку {folder}")


def main(folder):
    m06_scan.scan(folder)

    for file in m06_scan.JPEG_IMAGES:
        handle_image(file, folder, "JPEG")

    for file in m06_scan.JPG_IMAGES:
        handle_image(file, folder, "JPG")

    for file in m06_scan.PNG_IMAGES:
        handle_image(file, folder, "PNG")

    for file in m06_scan.SVG_IMAGES:
        handle_image(file, folder, "SVG")

    for file in m06_scan.OTHERS:
        handle_others(file, folder, "OTHERS")

    for file in m06_scan.ARCH:
        handle_archive(file, folder, "ARCH")

    for file in m06_scan.FOLDERS:
        handle_folder(file)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder.resolve())
    main(sort_folder.resolve())
