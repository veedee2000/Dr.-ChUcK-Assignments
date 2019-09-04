p = open('romeo.txt')
k = []
for line in p :
    line = line.rstrip()
    a = line.split()
    for i in range(len(a)) :
        if a[i] not in k : k.append(a[i])
k.sort()
print(k)
