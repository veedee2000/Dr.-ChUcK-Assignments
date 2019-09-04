import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input())
position = int(input())
i = 1
while i <= count :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    p = 0
    for tag in tags:
        p += 1
        if p == position :
            url = tag.get('href', None)
            print(url)
            break
    if i == count :
        print(tag.get_text())
    i += 1
