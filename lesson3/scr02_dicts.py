text = "Hi there Billy! How are you? Where are you from?"

char_counter = {}
not_char = tuple(" !?")

'''for char in text:

    if char in not_char:
        continue

    try:
        count = char_counter[char]

    except KeyError:
        count = 0

    count += 1
    char_counter[char] = count'''

for char in text:

    if char in not_char:
        continue

    count = char_counter.get(char, 0) #If there is no such symbol it returns the default value - None
    count += 1
    char_counter[char] = count

print(char_counter)
