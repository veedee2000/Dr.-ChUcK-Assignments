import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_280078.xml')
l = fhand.read()
tree = ET.fromstring(l)
sum = 0
counts = tree.findall('.//count')
for item in counts:
    sum += int(item.text)
print(sum)
