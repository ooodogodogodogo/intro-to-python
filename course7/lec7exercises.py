from collections import Counter
nums = ["a","b","b","c","c","c","c"]

countdict = Counter(nums)
print(countdict)

for key, value in countdict.items():
    if value % 2 == 1:
        print(key)
        
numdict = {}
for char in nums:
    if char in numdict:
        numdict[char] = numdict[char] + 1
    else:
        numdict[char] = 1
print(numdict)
numdict = {}
numset = set(nums)
for char in numset:
    numdict[char] = nums.count(char)
print(numdict)

chars = "abcdefghijklmnopqrstuvwxyz"
sentence = "A car is going to 50 kmh per hour."
sentence = sentence.lower()
numstring = ""
for i in sentence:
    if i.isalpha():
        numstring = numstring + str(chars.index(i)+1)
print(numstring)