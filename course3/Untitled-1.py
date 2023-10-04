total = 0
for i in range(1001):
    if i%3==0 or i%5==0:
     total = total + i 
print(total)

print(sum([i for i in range(1001) if i%3==0 or i%5==0 ]))

list = [3,4,45,6,7,7]
result_list = []
for i in list:
    if i%3==0 or i%5==0:
        result_list.append(i)
print(result_list)

total = 0
for i in range(1001):
    total = total + int(i%3==0 or i%5==0)*i
    
print(total)