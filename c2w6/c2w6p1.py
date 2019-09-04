f = open('mbox-short.txt')
p = dict()
for line in f:
    line = line.rstrip()
    w = line.split()
    if len(w) <= 1 or w[0] != 'From' : continue
    r = w[5].split(':')
    word = r[0]
    p[word] = p.get(word,0) + 1
x = sorted(p.items())
for k,v in x:
    print(k,v)
