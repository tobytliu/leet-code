from collections import Counter
s = "aabc"
c = Counter(s)
print(c)
c['z'] = 323
print(c)
