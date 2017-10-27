from collections import defaultdict
str = 'MPS python hello world MPS python bootcamp'

str_list = str.split()
print(str_list)

counts = defaultdict(lambda:0)
for i in str_list:
    counts[i] += 1

print(dict(counts))
