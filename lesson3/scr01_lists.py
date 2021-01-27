text = "Hi there Billy! How are you? Where are you from?"

words = []
alphabet = tuple("abcdefghijklmnopqrstuvwxyz")

start = 0
"""for idx, char in enumerate(text):
    if char.lower() not in alphabet:
        word = text[start:idx]
        if word != '': 
            words.append(word)
        start = idx + 1"""

for idx, char in enumerate(text):
    if char.lower() not in alphabet:
        word = text[start:idx]
        if len(word) > 1: 
            words.append(word.strip())
        start = idx

print(words)