import os
from collections import defaultdict

directory_list = os.listdir('/Users/hiroshiteraoka/MPS201710/Python')
print(directory_list)
# print(directory_list[0][-2:])

counts = defaultdict(lambda:0)
for i in directory_list:
    counts[i] += 1

print(dict(counts))
