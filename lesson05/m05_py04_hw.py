# Number of task: 

    # from typing import List


    # def real_len(text):
    #     new_text = ""
    #     for i in text:
    #         if i in ["\n", "\f", "\r", "\t", "\v"]:
    #             continue
    #         new_text += i

    #     return len(new_text)


    # def find_articles(key, letter_case=False):
    #     flag = 0
    #     new_articles_dict = []
        
    #     for i in range(len(articles_dict)):

    #         for j, val in articles_dict[i].items():

    #             if j == "year":
    #                 continue
    #             elif not letter_case:
    #                 key = key.lower()
    #                 val = val.lower()
                
    #             flag = 1 + val.find(key)
    #             if flag:
    #                 new_articles_dict.append(articles_dict[i])
    #                 flag = 0

    #     return new_articles_dict


    # def count_specs(text=""):
    #     counter = 0
    #     for i in text:
    #         if i in "\n\f\r\t\v":
    #             counter += 1
    #     return counter


    # def find_spam(text, spam_words):
    #     a = spam_words
    #     for index, val in enumerate(a):
    #         spam_words[index] = val.lower()
        
    #     list_word = text.lower().split()

    #     for i in list_word:
    #         for j in spam_words:
    #             if i.find(j) != -1:

    #                 return True

    #     return False


    # def total_price(string_with_titles, prices_dict):
    #     list_with_titles = string_with_titles.lower().split("\n")
    #     answer = 0
    #     for key, val in prices_dict.items():
    #         for i in list_with_titles:
    #             if i == key:
    #                 answer += val
    #     return answer


    # def comments_to_show(comment_dict={}):
    #     print(comment_dict)
    #     list_comment = [1, 2, 3]

    #     list_val = list(comment_dict.values())
    #     list_val.sort()
    #     list_val.reverse()

    #     for key, val in comment_dict.items():
    #         comment = key.removeprefix("<comment>").removesuffix("</comment>")
    #         comment = comment.strip()
    #         if val == list_val[0]:
    #             list_comment[0] = comment
    #         elif val == list_val[1]:
    #             list_comment[1] = comment
    #         elif val == list_val[2]:
    #             list_comment[2] = comment

    #     comment_string = "\n".join(list_comment)

    #     comment_string.replace("\t", "")

    #     return comment_string


    # def translate_surnames(surnames):
    #     print(surnames)
    #     translated_surnames = []
        
    #     map = {ord('а'): 'a', ord('А'): 'A', \
    #                 ord('б'): 'b', ord('Б'): 'B', \
    #                 ord('е'): 'e', ord('Е'): 'E', \
    #                 ord('и'): 'i', ord('И'): 'I', \
    #                 ord('к'): 'k', ord('К'): 'K', \
    #                 ord('о'): 'o', ord('О'): 'O', \
    #                 ord('р'): 'r', ord('Р'): 'R', \
    #                 ord('н'): 'n', ord('Н'): 'N', \
    #                 ord('т'): 't', ord('Т'): 'T', \
    #                 ord('с'): 's', ord('С'): 'S', \
    #                 ord('л'): 'l', ord('Л'): 'L', 
    #     }

    #     for i in surnames:
    #         i = i.translate(map)
    #         translated_surnames.append(i)

    #     return translated_surnames


    # if __name__ == "__main__":
    #     articles_dict = [
    #     {
    #         "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
    #         "author": "Jhon Stark",
    #         "year": 2019,
    #     },
    #     {
    #         "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
    #         "author": "Artur Clark",
    #         "year": 2020,
    #     },
    #     {
    #         "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
    #         "author": "Silver Name",
    #         "year": 2021,
    #     },
    #     {
    #         "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
    #         "author": "Golden Gun",
    #         "year": 2021,
    #     },
    # ]

    #     # print(find_articles("aliqua", letter_case=False))

    #     # text = "new cloth in our shop! for more by link"
    #     # spam_words = ['Buy', 'Find', 'Follow']
    #     # print(find_spam(text, spam_words))

    #     comment_dict = {'<comment>   This place was amazing    </comment>': 1803,\
    #         '<comment>   Kind waitresses    </comment>': 2000, \
    #         '<comment>   Pretty interior    </comment>': 300, \
    #         '<comment>   Delicious food    </comment>': 900}

    #     comment_dict1 = {'<comment>   This place was amazing    </comment>': 3, \
    #         '<comment>   Kind waitresses    </comment>': 10, \
    #             '<comment>   Pretty interior    </comment>': 300, \
    #                 '<comment>   Delicious food    </comment>': 3130}
        
    #     print(comments_to_show(comment_dict1))

    #     print(translate_surnames(['Берке', 'Носко']))

# 3


    # def sanitize_phone_number(phone):
    #     new_phone = (phone.strip()
    #                 .removeprefix("+")
    #                 .replace("(", "")
    #                 .replace(")", "")
    #                 .replace(" ", "")
    #                 .replace("-", "")
    #                 )
    #     print(new_phone)
    #     return new_phone


# 4


    # def is_check_name(fullname, first_name):
    #     print(f"{fullname}, {first_name}")
    #     if fullname.removeprefix(first_name) != fullname:
    #         return True
    #     return False


# 5


    # def sanitize_phone_number(phone):
    #     new_phone = (
    #         phone.strip()
    #         .removeprefix("+")
    #         .replace("(", "")
    #         .replace(")", "")
    #         .replace("-", "")
    #         .replace(" ", "")
    #     )
    #     return new_phone


    # def get_phone_numbers_for_countries(list_phones):
    #     list_ua_phones = []
    #     list_jp_phones = []
    #     list_tw_phones = []
    #     list_sg_phones = []

    #     for phone in list_phones:
    #         phone = sanitize_phone_number(phone)
    #         if phone[:2] == "81":
    #             list_jp_phones.append(phone)
    #         if phone[:2] == "65":
    #             list_sg_phones.append(phone)
    #         if phone[:3] == "886":
    #             list_tw_phones.append(phone)
    #         if phone[:3] == "380":
    #             list_ua_phones.append(phone)

    #     dict_phones = {"UA" : list_ua_phones, "JP": list_jp_phones, "TW": list_tw_phones, "SG": list_sg_phones}
    #     print(dict_phones)

    #     return dict_phones


# 6

    # def is_spam_words(text, spam_words, space_around=False):
    #     print(f"{text}, {spam_words}, {space_around}")
    #     text = text.lower()
    #     print(f"{text}, {spam_words}, {space_around}")
    #     for spam_word in spam_words:
    #         spam_word = spam_word.lower()
    #         len_spam = len(spam_word)
    #         result = text.find(spam_word)
    #         print(result)

    #         if result != -1:
    #             if not space_around:
    #                 return True
    #             elif (result == 0 or text[result-1] == " ") and (text[result+len_spam] == " " or "."):
    #                 return True

    #         return False


    # if __name__ == "__main__":
    #     print(is_spam_words("Молох", ["лох"], False))
    #     print(is_spam_words("Мо лох", ["лох"], True))
    #     print(is_spam_words("Лох", ["лох"], True))
    #     print(is_spam_words("лох.", ["лох"], True))
    #     print(is_spam_words("лохотрон.", ["лох"], True))


# 7

    #     # txt = "the sun"
    #     # my_table = txt.maketrans("nus", "nos", "he t")
    #     # print(txt.translate(my_table))  # son

    #     # CYRILLIC = ("а", "ч", "ш")
    #     # LATIN = ("a", "ch", "sh")

    #     # TRANSLIT_DICT = {}

    #     # for c, l in zip(CYRILLIC, LATIN):
    #     #     TRANSLIT_DICT[ord(c)] = l
    #     #     TRANSLIT_DICT[ord(c.upper())] = l.upper()

    #     # print("чаша".translate(TRANSLIT_DICT))  # chasha
    #     # print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA


    # CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    # TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    #             "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

    # TRANS = {}
        
    # for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    #     TRANS[ord(c)] = l
    #     TRANS[ord(c.upper())] = l.upper()


    # def translate(name):
    #     latin_name = name.translate(TRANS)
    #     print(f"{name} - {latin_name}")
    #     return latin_name


# 8

    # grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


    # def formatted_grades(students):
    #     print(students)
    #     list_students = []
    #     number = 0

    #     for name, grade_ECTS in students.items():
    #         number += 1
    #         grade_digit = grade[grade_ECTS]
    #         list_students.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(number, name, grade_ECTS, grade_digit))
        
    #     print(list_students)
    #     return list_students


# 9


    # def formatted_numbers():
    #     num_list = []
    #     num_list.append('|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary'))

    #     for i in range(16):
    #         num_list.append('|{:<10d}|{:^10x}|{:>10b}|'.format(i, i, i))
    #     print(num_list)
    #     return num_list

    # if __name__ == "__main__":
    #     formatted_numbers()


# 10 
    # import re


    # def find_word(text, word):
    #     first_index = None
    #     last_index = None
    #     search_word_in_text = re.search(word, text)
    #     print(search_word_in_text)
    #     result = bool(search_word_in_text)

    #     if result:
    #         first_index = search_word_in_text.span()[0]
    #         last_index = search_word_in_text.span()[1]
    #     dictionary = {
    #                     'result': result,
    #                     'first_index': first_index,
    #                     'last_index': last_index,
    #                     'search_string': word,
    #                     'string': text
    #     }
    #     print(dictionary)
    #     return dictionary

    # if __name__ == "__main__":
    #         # s = "I am 25 years old"
    #         # age = re.search('\d+', s)
    #         # print(age.string)
    #     find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python")


# 11
    # import re


    # def find_all_words(text, word):
    #     list_found_words = re.findall(word, text, flags=re.IGNORECASE)
    #     return list_found_words

        
    # if __name__ == "__main__":
    #         # s = "I bought 77 nuts for 6$ and 110 bolts for 3$."

    #         # print(re.findall("(\d){2}", s))  # ['0'] второй символ в двухзначном числе
    #         # print(re.findall("(\d){3}", s))  # ['0'] третий символ в трёхзначном числе
    #         # print(re.findall("[\d]{3}", s))  # ['110']
    #     find_all_words(text, word)


# 12
    # import re


    # def replace_spam_words(text, spam_words):

    #     for spam_word in spam_words:
    #         text = re.sub(spam_word, '*' * len(spam_word), text, flags=re.IGNORECASE)
        
    #     print(text)
    #     return text


    # if __name__ == "__main__":
    #     print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn', ['began', 'Python']))


# 13
    # import re


    # def find_all_emails(text):
    #     result = re.findall(r'[A-z][\w{2,20}][\.\w+]*[\-\w+]*[@]\w+[\-]?[.]\w{2,8}', text)
    #     print(result)
    #     return result

    # # ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']

    # if __name__ == "__main__":
    #     test_text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
    #     print(find_all_emails(test_text))


# 14
import re


def find_all_phones(text):
    result = re.findall(r"\+380\(\d\d\)\d{3}\-\d{1}\-\d{3}|\+380\(\d\d\)\d{3}\-\d{2}\-\d{2}", text)
    return result

if __name__ == "__main__":
    # ['+380(67)777-7-771', '+380(67)777-77-77', '+380(67)777-77-78']
    print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))
