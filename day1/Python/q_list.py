# def removeDups(L1, L2):
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
#
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# removeDups(L1, L2)
# print('L1')

A = [10,12,13,14,16]
B = [10,11,13,14,15]
for a in A:
    if a in B:
        A.remove(a)

print(A)