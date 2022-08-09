import json
import urllib.request,urllib.parse , urllib.error

serviceurl = input('Enter Location: ')
total=list()
url = serviceurl
print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")

try :
    js = json.loads(data)
except :
    js = None

for counts in js["comments"] :
    # print('Counts:', counts['count'])
    total.append(counts['count'])
print(sum(total))