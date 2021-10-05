import random


number_0_1 = random.random()
print(number_0_1)

number_1_1000 = random.randint(1, 1000)
print(number_1_1000)

fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)

print(random.choice(fruits))
print(random.choices(fruits, k=4))
print(random.sample(fruits, k=2))
