import string

surname = 'Stephen Spielberg'
letters = {}
let_set = set('Stephen Spielberg')
five_not = set('abcde ')
general_not = let_set & five_not

print(five_not, let_set)

letters = let_set ^ general_not

print(letters)
