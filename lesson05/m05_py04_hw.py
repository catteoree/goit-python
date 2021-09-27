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


def sanitize_phone_number(phone):
    new_phone = (phone.strip()
                .removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace(" ", "")
                .replace("-", "")
                )
    print(new_phone)
    return new_phone


# 4


def is_check_name(fullname, first_name):
    print(f"{fullname}, {first_name}")
    if fullname.removeprefix(first_name) != fullname:
        return True
    return False


# 5


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    list_ua_phones = []
    list_jp_phones = []
    list_tw_phones = []
    list_sg_phones = []

    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone[:2] == "81":
            list_jp_phones.append(phone)
        if phone[:2] == "65":
            list_sg_phones.append(phone)
        if phone[:3] == "886":
            list_tw_phones.append(phone)
        if phone[:3] == "380":
            list_ua_phones.append(phone)

    dict_phones = {"UA" : list_ua_phones, "JP": list_jp_phones, "TW": list_tw_phones, "SG": list_sg_phones}
    print(dict_phones)

    return dict_phones


# 6



