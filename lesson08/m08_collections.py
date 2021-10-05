import collections
from typing import List


Person = collections.namedtuple('Person', ['name', 'last_name', 'age', 'birth_place', 'post_index'])
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

print(person.name)
print(person.post_index)
print(person.age)
print(person[3])

# Counter

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]

    # mark_counts = {}
    # for mark in student_marks:
    #     if mark in mark_counts:
    #         mark_counts[mark] += 1
    #     else:
    #         mark_counts[mark] = 1
    # print(mark_counts)

mark_counts = collections.Counter(student_marks)
print(mark_counts)

print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

c = collections.Counter(a=4, b=2, c=0, d=-2)
d = collections.Counter(a=1, b=2, c=3, d=4)
c.subtract(d)

print(c)

# defaultdict

words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
    # grouped_words = {}

    # for word in words:
    #     char = word[0]
    #     if char not in grouped_words:
    #         grouped_words[char] = []

grouped_words = collections.defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(grouped_words)

# deque

d = collections.deque()
d.append('last')
d.appendleft('first')
d.insert(1, 'middle')
print(d)
print(d.pop())
print(d.popleft())
print(d)

maxlen_5 = collections.deque(maxlen=5)
for i in range(10):
    maxlen_5.append(i)

print(maxlen_5)
