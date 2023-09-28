import math 
#if-elseexample
"""
a = 5
if a==5:
    print( "a is 5")
    if  a >= 4:
        print("a is greater than 4")
    else:
        print("a is less than 5")
"""
#if-else function example
"""
def func():
    a = 3
    if a >= 4:
        return "a is greater than 4"
    if  a == 5:
        return("a is 5")
    else:
        return("a is less than 5")
print(func())
"""
"""""
c = 6
a =5
b =4
#a += 4 # a = a+4
#a -= 4 # a = a-4
#print(max(a,b))
d = max(max(a,b),c)
e = max(d,c)
print(d)
"""
#print(math.factorial(5))

word1 = "hello"
index = word1.find("l")
first_two = word1[0:2]
last = word1[-1]
#print(word2)
#print(word1[min(index+1,len(word1)-1)])
#print(word1[index+1])
#print(word1[len(word1)-1])


#password checker
#uzunluğu 8-20 karakter arası
#Büyük harf ve küçük harf içerecek
#sayı içerecek

def passwordCheck(password):
    if len(password) < 8 or len(password) > 20:
        return False
    if password.islower() or password.isupper():
        return False
    if password.isalpha():
        return False
    return True
password = "ahmetMehmet"
print(passwordCheck(password))

