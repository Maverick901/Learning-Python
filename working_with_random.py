import random
import string

print(random.random())
print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=3))
print("".join(random.choices(string.ascii_letters+string.digits, k=10)))

number = [1, 2, 3, 4]
random.shuffle(number)
print(number)
