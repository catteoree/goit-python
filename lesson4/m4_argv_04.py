import sys
import pathlib 


def print_file_name(file_name, full_path=False, margin=0, margin_symbol=" "):
    margin = margin_symbol * margin
    if full_path:
        print(margin + str(file_name.absolute()))
    else:
        print(margin + file_name.name)


def main():
    file_name = sys.argv[1]
    file_name = pathlib.Path(file_name)
    print_file_name(file_name, full_path=True, margin=4, margin_symbol="_")


if __name__ == "__main__":
    main()
