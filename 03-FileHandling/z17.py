import re
txt = 'To be, or not to be, that is the question'
samog = re.findall("[aeiou]", txt)
print (len(samog))