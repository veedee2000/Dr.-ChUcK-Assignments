from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum = 0
count = 0
tags = soup('span')
for tag in tags:
    count += 1
    sum += int(tag.get_text())
    #p = re.findall('[0-9]',tag)
    #sum += int(p[0])
print('Count:',count)
print('Sum:',sum)
