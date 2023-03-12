import random
#a
numbers = [1, 2, 3, 4, 5]
result = all(num > 0 for num in numbers)
print(result)

numbers = [0, 1, 2, 3, 4, 5]
result = any(num > 5 for num in numbers)
print(result)
#b
n = 30
string = str(n)
print(string)

a = 30
repr = repr(a)
print(repr)

#c
x = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
x.sort()
print(x)

x = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
y = sorted(x)
print(x)
print(y)

#d
fruits = ["apple","banana","orange","cherry"]
random_fruit = random.choice(fruits)
print(random_fruit)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_numbers = random.sample(numbers, 3)
print(random_numbers)