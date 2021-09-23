my_list = list('Hello World')
my_list[2] = 'y'
my_list.append('go')

print(my_list, len(my_list))

msg = 'Hello'

print(msg[::2])

my_list.remove('y')

print(my_list, my_list.index('l'))

new_list = [1, 2, 1, 3, 1, 4, 1, [1, 1, 1, 1]]
new_list.remove(1)
a = new_list.pop()

print(new_list, a, new_list.count(1))

a = [3, 1, 21, 3, 34, 432, 3, 2, 23, 3]
a = [i for i in a if i != 3]

print(a)
