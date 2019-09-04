f = open('mbox-short.txt')
d = dict()
m = 0
for line in f:
    line = line.rstrip()
    l = line.split()
    if len(l) <= 1 or l[0] != 'From' : continue
    d[l[1]] = d.get(l[1],0) + 1
    if d[l[1]] > m :
        m = d[l[1]]
        p = l[1]
print(p,m)
