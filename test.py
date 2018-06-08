import random

random.seed()

a = random.randint(1, 10)
b = random.randint(1, 10)

c = a + b

print(a, ' + ', b, ' = ')

i = int(input())

if i != c:
    print('The result is not ', i, '. It is ', c, '.')
else:
    print('You are right! The result is ', i, '.')
