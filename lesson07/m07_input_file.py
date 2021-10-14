# string = input()

string = "a b" \
         "\nc d" \
         "\ne f" \
         "\ng h" \
         "\nk o"

with open('input.txt', 'a', encoding='utf-8') as f:
    f.write(string)
    print("End")
