import json
import re
import collections

with open ('DontMakeMeWait.txt') as file:
    t = file.read()
    txt = t.lower()
    
z = re.findall('[a-z]',txt)
x = collections.Counter(z)

with open ('DontMakeMeWait.json','w') as f:
    json.dump(x,f,indent=4)