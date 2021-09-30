# Path

    # from pathlib import Path

    # print(Path.home())

    # # file = open("test.txt")

    # # print(file.read())
    # # file.close()

    # # (r"") - обозначение игнора спецсимволов в кавычках

    # file = open(r"E:\Stu\coder\goit-python\lesson05\text.txt")

    # print(file.read())
    # file.close()


# tuple


    # # def func(arg=[]):
    # #     arg.append(1)
    # #     print(arg)


    # # def func(arg=()):
    # #     arg.append(1)
    # #     print(arg)

    # def func(arg=None):
    #     if arg is None:
    #         arg = []
            
    #     arg.append(1)
    #     print(arg)

    # if __name__ == "__main__":
    #     func()
    #     func()
    #     func()


# unlink(), rmdir() (help(Path))

    # from os import rmdir
    # from pathlib  import Path


    # def remove_directories(path):

    #     for child in path.iterdir():
    #         if child.is_file():
    #             child.unlink()
    #         else:
    #             remove_directories(child)
        
    #     path.rmdir()

    # remove_directories(Path(r"E:\Stu\coder\goit-python\dum"))

# catalogue search

    # catalogue = {"Jack White": [{"Name": "Lazaretto", 
    #                             "Year": "2007", 
    #                             "Tracks": [1, 2, 3]}],
    #             "Jefferson Airplane": []}

    # def search(name, catalogue, search_type="default"):

    #     result = None

    #     if search_type == "default":
    #         result = catalogue[name]
    #     elif search_type == "incremental":
    #         for key, value in catalogue.items():
    #             if key.casefold().startswith(name.casefold()):
    #                 return value
    #     elif search_type == "partial":
    #         for key, value in catalogue.items():
    #             if name.casefold() in key.casefold():
    #                 return value

    #     return result

    # if __name__ == "__main__":
    #     print(search("white", catalogue, search_type="partial"))

# calculate_frequency(text)

    # text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "\
    #          "Pellentesque justo odio, mattis a lorem ac, tincidunt mollis ligula. "\
    #          "Vivamus ligula tortor, placerat eget ornare nec, ornare lacinia mauris. "\
    #          "Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. "\
    #          "Fusce nec eros ac massa euismod tempus. "\
    #          "Nullam volutpat eros vitae arcu imperdiet, at gravida leo luctus. "\
    #          "Donec pharetra magna id elementum efficitur. "\
    #          "Morbi blandit mattis urna, vitae finibus tellus fringilla ut. "\
    #          "Sed vulputate nulla nulla, nec dignissim magna tempus efficitur. "\
    #          "Donec eu erat urna. Sed eleifend elementum sodales. "\
    #          "Fusce rhoncus lorem felis, at venenatis ipsum bibendum nec. "\
    #          "Suspendisse eu semper dui. "\
    #          "Vestibulum in mauris fringilla, molestie lectus eu, sagittis magna. "\
    #          "Phasellus nec tincidunt purus. In eleifend pellentesque interdum. "\
    #          "Aliquam malesuada, mi vitae faucibus dignissim, elit orci interdum leo, quis pretium metus turpis quis est. "\
    #          "Sed vestibulum enim sed nulla sollicitudin, sit amet condimentum enim finibus. "\
    #          "Donec imperdiet, est eu efficitur convallis, augue libero aliquet orci, ac convallis lacus sapien non nulla. "\
    #          "Mauris varius ut est sed faucibus. "\
    #          "Quisque tristique est vehicula, venenatis neque vitae, eleifend urna. "\
    #          "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum venenatis lacus orci. "\
    #          "Aenean vel efficitur magna. Aliquam nec aliquet nunc, vel blandit nibh. "\
    #          "Donec hendrerit luctus felis quis aliquam."


    # def calculate_frequency(text):

    #     words_frequency = {}
    #     lower_text = text.lower()
    #     words = lower_text.split()

    #     for word in words:
    #         words_frequency[word] = round((lower_text.count(word)/len(words)), 3)
        
    #     return words_frequency 

    # if __name__ == "__main__":
    #     print(calculate_frequency(text))
        
# "".format()

    # name = "Jack"
    # last_name = "White"
    # print(f'Hello! My name is {name + " " + last_name}.')
    # print(f'Hello! My name is {name} {last_name}.')
    # print('Hello! My name is {} {}.'.format(name, last_name))
    # print('Hello! My name is {1} {0}.'.format(name, last_name))
    # print('Hello {0}! My {1} name is {1} {0}.'.format(name, last_name))
    # print('Hello! My name is {name} {last_name}.'.format(name="Jack", last_name="White"))
    # print('Hello {0}! My name is {name} {last_name}.'.format('123', name="Jack", last_name="White"))
    # print('{number:d} {number:b}'.format(number=5))
    # print(f'{5} {str(bin(5))} {oct(5)} {hex(5)}')
    # print("{:^24s}".format("Mystring"))
    # print("{:^24}".format("Mystring"))
    # print("{:*^24s}".format("Mystring"))

# re
    # import re

    # help(re.search)

    # mail_regex = '^(\w|\.|\-)+[@](\w|\-|\.)+[.]\w{2,8}$'
    # print(f"search: {re.search(mail_regex, 'vasya.00@gmail.com')}")
    # print(f"search: {re.search(mail_regex, 'vasya.00gmail.com')}")
    # print(f"search: {re.search('[a]', 'abcabcabc')}")
    # print(f"search.group(): {re.search('[a]', 'abcabcabc').group()}")
    # print(f"match: {re.match('[a]', 'abcabcabc')}")
    # print(f"match.group(): {re.match('[a]', 'abcabcabc').group()}")
    # print(f"match: {re.match('[a]', 'bcabcabc')}")
    # print(f"findall: {re.findall('[a]', 'abcabcabc')}")
    # print(f"sub: {re.sub('[a]', 'Z', '123abcabcabc')}")
    # print(f"replace: {'123abcabcabc'.replace('3', 'Z')}")

    # regex_sub = re.sub('[\d]', 'Z', '123abcabcabc')
    # print(f"sub: {regex_sub}")
    # regex_findall = re.findall('[\,]', 'a,bc:abc,abc')
    # print(f"findall: {regex_findall}")
    # print(f"findall '[a]+' в 'abcabcabc': {re.findall('[a]+', 'abcabcabc')}")
    # print(f"findall '[a]+' в 'aaaaaaaabcabcabc': {re.findall('[a]+', 'aaaaaaaabcabcabc')}")
    # print(f"findall '[a]*' в 'aaaaaaaabcabcabc': {re.findall('[a]*', 'aaaaaaaabcabcabc')}")
    # print(f"findall '[a]*' в 'aaaaaaaabcabcabc': {re.findall('[a]*', 'aaaaaaaabcabcabc')}")
    # regex_findall_range = re.findall('[a]{3}', 'aaaaaaaabcabcabc')
    # print(f"findall '[a](3)' в 'aaaaaaaabcabcabc': {regex_findall_range}")
    # regex_findall_range = re.findall('[a]{3,4}', 'aaaaaaaabcabcabc')
    # print(f"findall '[a](3,4)' в 'aaaaaaaabcabcabc': {regex_findall_range}")

# methods string
    # import re


    # BAD_WORDS = ('bad', 'mad', 'sad', 'bottle', 'vodka')

    # while True:

    #     message = input('message: ')
    #     # bad_words = frozenset(message.casefold().split())
    #     message_casefold = message.casefold()

    #     for bad_word in BAD_WORDS:
            
    #         regex = rf'\b{bad_word}\b'

    #         if re.search(regex, message_casefold):
    #             replacement = f'*{bad_word[1:-1]}*'
    #             message_casefold = re.sub(regex, replacement, message_casefold)

    #     new_message = ''

    #     for i in range(len(message)):
    #         if message_casefold[i] != '*':
    #             new_message += message[i]
    #         else:
    #             new_message += message_casefold[i]
                
    #     print(new_message)


# Clean and normalize text (remove non-alphanumeric symbols
# and make it casefold)
# Find frequency for each word
# Find text dictionary
# Find top 3 keywords
import re


def clear_text(text):
    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text


def normalize_text(clean_text):
    clean_normalized_text = clean_text.casefold()
    return clean_normalized_text


def find_text_dictionary(clean_normalized_text):
    text_dictionary = frozenset(clean_normalized_text.split())
    return text_dictionary


def find_words_frequency(clean_normalized_text, text_dictionary):
    words_frequency = {}
    words_quantity = len(clean_normalized_text.split())

    for word in text_dictionary:

        frequency = clean_normalized_text.count(word) / words_quantity * 100
        words_frequency[word] = round(frequency, 2)
    
    return words_frequency


def sort_by_value(item):

    return item[1]



def sort_words_frequency(words_frequency):

    words_frequency_items = list(words_frequency.items())
    words_frequency_items.sort(key=sort_by_value, reverse=True)

    return words_frequency_items


if __name__ == "__main__":
    test_text = "Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in 'abcdef', since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} are not. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the search() function rather than the match() function:"
    clean_text = clear_text(test_text)
    clean_normalized_text = normalize_text(clean_text)
    text_dictionary = find_text_dictionary(clean_normalized_text)
    words_frequency = find_words_frequency(clean_normalized_text, text_dictionary)
    words_frequency_items = sort_words_frequency(words_frequency)
    print(words_frequency_items[:3])

