import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_280079.json')
data = fhand.read()
info = json.loads(data)
sum = 0
for item in info["comments"]:
    sum += int(item["count"])
print(sum)
