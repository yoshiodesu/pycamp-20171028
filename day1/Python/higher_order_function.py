def applyToEach(A, f):
    for i in range(len(A)):
        A[i] = f(A[i])


A = [1, -2, 3.3333334]
print('A= ', A)
applyToEach(A, abs)  # 絶対値
print('A= ', A)
applyToEach(A, round) # 小数点切り捨て
print('A= ', A)
applyToEach(A, str) # 文字列変換
print('A= ', A)