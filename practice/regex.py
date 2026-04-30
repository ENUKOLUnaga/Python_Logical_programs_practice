"""import re

text = "I love python"
print(re.search("python",text))
print(re.match("I",text))
print(re.match("love",text))
print(re.findall(r"\d","a1b2c3"))
print(re.sub(r"\d","*","a1b2c3"))
print(re.sub(r"\D","*","a1b2c3"))
print(re.split(r"\s","Hello world python"))

"""
import re

match=re.search(r"(\d+)-(\d+)","123-456")
print(match.group(1))
print(match.group(2))

print(re.findall(r"cat|dog|monkey","cat dog bird"))
print(re.search(r"[abc]","apple ball"))
print(re.findall(r"\.","a.b.c"))

print(re.findall(r"\w+@\w+\.\w+","test@gmail.com"))
print(re.findall(r"a+","aaab"))
print(re.findall(r"a*","aaab"))
print(re.findall(r"a?","aba"))
print(re.findall(r"a{3}","aaab"))
print(re.findall(r"\d{2,}","1 22 333 4444"))
print(re.findall(r"\d{2,3}","1 22 333 4444"))



