from random import randint
def get_random_password():
    pass_list = []
    while len(pass_list) < 8:
        random_num = randint(40, 126)
        new_list = pass_list.append(chr(random_num))
        password = ''.join(pass_list)
    return password

print(get_random_password())

def is_valid_password(password):
    answer = False
    str_up = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    str_low = set('abcdefghijklmnopqrstuvwxyz')
    nums = set('0123456789')
    pass_set= set(password)
    print(password)
    pass_nums = pass_set & nums
    pass_str_low = pass_set & str_low
    pass_str_up = pass_set & str_up
    print(pass_set & nums)
    print(pass_set & str_low)
    print(pass_set & str_up)
    if len(password) == 8 and len(pass_nums) > 0 and len(pass_str_up) > 0 and len(pass_str_low) > 0:
        answer = True
    return answer

print(is_valid_password(get_random_password()))

