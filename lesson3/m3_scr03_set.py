text = "Hi there Billy! How are you? Where are you from?"

alphabet = tuple("abcdefghijklmnopqrstuvwxyz")
char_set = set()
punct_set = set()

for char in text:
    
    if char.lower() in alphabet:
        char_set.add(char)

    else:
        punct_set.add(char)

print('Chars: ', char_set)
print('Symbols: ', punct_set)
