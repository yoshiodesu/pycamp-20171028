s = []
for _ in range(2):
    s.append(0)

for _ in range(99):
    s.append(1)

#素数検索
i = 2
while i*i <= 100:
    j = 2

    while i*j <= 100 and s[i] != 0:
        print("j",j)
        s[i*j] = 0
        j += 1

    i += 1

i = 2
while i <= 100:
    if s[i] == 1:
        print(i)
    i += 1