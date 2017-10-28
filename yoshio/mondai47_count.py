import os
from collections import defaultdict
 
str='MPS python hello word MPS python bootcamp'
list=str.split(" ")

directory_dict=defaultdict(lambda:0)

print(list)

for i in list:
    directory_dict[i]+=1

print(dict(directory_dict))


#import os
#from collections import defaultdict
# 
#directory_list=os.listdir('/home/mb/pycamp4')
#
#directory_dict=defaultdict(lambda:0)
#
#for i in directory_list:
#    if i[-2:]=='py':
#        if os.path.isfile(i):
#            directory_dict['Python']+=1
#
#print(dict(directory_dict))

# import os
# 
# directory_list=os.listdir('/home/mb/pycamp4')
# directory_dict={'Python':0}
# count=0
# for i in directory_list:
#    if i[-2:]=='py':
#        count +=1
#    directory_dict['Python']=count
# print(directory_dict)
 



# a=[10,12,13,14,16]
# b=[10,11,13,14,15]

# for val in b:
#    if val in a:
#        a.remove(val)
# print(a)

# [a.remove(val) for val in b if val in a]
# print(a)



    
