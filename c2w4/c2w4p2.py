p = open('mbox-short.txt')
count=0
for line in p :
    line.rstrip()
    a = line.split()
    if len(a) <= 1 or a[0] != 'From' : continue
    print(a[1])
    count += 1
print('There were',count,'lines in the file with From as the first word')
