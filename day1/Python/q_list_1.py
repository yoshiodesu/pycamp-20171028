A = [10,12,13,14,16]
B = [10,11,13,14,15]
# for a in A:
#     if a in B:
#         A.remove(a)
#
# print(A)
print([A.remove(a) for a in A if a in B])