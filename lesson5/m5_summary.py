import re


# search in str

    # s = "Hi there!"

    # # start = 0
    # # end = 7

    # # print(s.find("er", start, end)) # 5 

    # print(s.find("er")) # 5
    # print(s.find("q"))  # -1

# format of numbers

    # for i in range(16):
    #     s = "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(i)

    #     print(type(s), s)

# format table

    # width = 1
    # for num in range(12):
    #     print('{:^20} {:^20} {:^20}'.format(num, num**2, num**3))

# modificators 

    # s =  "{name!s} {last_name!r}".format(last_name="Dilan", name="Bob")
    # print(s)  # 'Bob' Dilan 

    # print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111

    # print('pi: {:0.4}'.format(3.1415))  # pi: 3.14
    # print(f"")

    # print('"{}" "{:+}" "{:-}" "{: }"'.format(-1, -2, -3,  -4))  # "1" "+2" "-3" " 4" 

    # print("|{:<10}|{:*^20}|{:>10}|".format('left', 'center2', 'right'))  # |left      |**center**|     right|

s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>

s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25
