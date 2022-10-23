
a = [64, 83, 6, 3, 67, 82, 84, 59, 0]
b = [48, 50, 51, 54, 54, 49, 100, 100, 52]
for c in range(len(a)):
    for i in range(1000):
        if a[c]^i == b[c]:
            print(i, chr(i))