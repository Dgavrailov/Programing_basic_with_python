s = input()

a = 1
e = 2
i = 3
o = 4
u = 5
nsm = 0

for ch in s:
    if ch == 'a':
        nsm += a
    elif ch == 'e':
        nsm += e
    elif ch == 'i':
        nsm += i
    elif ch == 'o':
        nsm += o
    elif ch == 'u':
        nsm += u
print(nsm)