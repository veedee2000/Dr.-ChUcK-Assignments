import re
sum=0
f = open('regex_sum_280074.txt')
for line in f:
    line = line.rstrip()
#dont need split because y is already a complete list
    y = re.findall('[0-9]+',line)
    for i in y:
        sum += int(i)
print(sum)
