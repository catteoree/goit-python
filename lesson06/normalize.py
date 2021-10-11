import re


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ‎"
TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "i", "i", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", 
               "f", "kh", "ts", "ch", "sh", "shch", "ie", "y", "", "e", "iu", "ia", "ie", "i", "i", "g")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str):
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name
    