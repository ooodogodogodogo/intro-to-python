"""""
counter = 1
while counter <10 :
    print(counter)
    counter = counter +1
for x  in range(1,10):
    print(x)
"""

"""""
while True:
    print("start of the game:")
    a = input()
    b = input()
    legal_input = ["k","m","t","e"]
    if a not in legal_input or b not in legal_input:
        print("adamın kafasını attırmayın kardeşim")
        continue
    if a == b:
        print(0)
    if a <b and not (a == "k" and b == "t"):
        print(2)
    elif b<a and not (b == "k" and a == "t"):
        print(1)
    else:
        print((b == "k") +1 )
    
    if a == "e" or b == "e":
        break
"""
"""""
a = input()
if (a.isnumeric()):
    print(int(a))
"""
"""""
for i in range(10):
    if i == 5:
        continue
    print(i)
"""
a = 8
for i in range(a):
    print("#"* a)
    
fact = 1
x = int(input())
for i in range(1,x+1):
    fact = i * fact
print(fact)