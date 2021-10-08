from pathlib import Path


path_text = Path("lesson06/Test/my_txt_file.txt")
path_text.write_text("Test adskhbg\nFHsdaga")
path_text.write_text("Fhjsdhgafkh")
print(path_text.read_text())

path_bytes = Path("lesson06/Test/my_bin_file.bin")
path_bytes.write_bytes(b"Test adskhbg\nFHsdaga")
path_bytes.write_bytes(b"Fhjsdhgafkh")
print(path_bytes.read_bytes())