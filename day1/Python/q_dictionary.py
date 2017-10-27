import os

directory_list = os.listdir('/Users/hiroshiteraoka/MPS201710/Python')
print(directory_list[0][-2:])

directory_dict = {'python':0}
count = 0
for i in directory_list:
    if i[-2:] == 'py':
        count += 1
        directory_dict['python'] = count

print(directory_dict)