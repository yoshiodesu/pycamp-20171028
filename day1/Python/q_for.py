import random

result = ''
for _ in range(6):
    result += str(random.choice([1, 2, 3, 4, 5, 6]))

print(result)