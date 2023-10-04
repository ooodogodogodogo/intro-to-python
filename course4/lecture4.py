num_list = [3,5,7,15,17,18 ,8,10,13, 6, 9,12,14,15,48,4]
num_list = list(set(num_list))
print(num_list)
for i in num_list:
    for j in num_list:
            if i*j in num_list  and num_list.index(i) < num_list.index(j):
                #print(i,j,i*j)
                a=1
                
size_of_list = len(num_list)
for i in range(size_of_list):
    for j in range(i):
            if (num_list[i]*num_list[j] in num_list):
                print(num_list[i],num_list[j],num_list[i]*num_list[j])            

mylist= list(range(10))
print(mylist)    
odd_list = []
for i in num_list:
    if i %2 == 1:
        odd_list.append(i)
odd_list_comp = [i**2 for i in num_list if i%2 ==1]
print(odd_list)    
print(odd_list_comp)
"""""        
name_list = ["ahmet", "mehmet", "veliz"]
if_z_exist = False
for name in name_list:
    print(name)
    for character in name:
        if character == "z":
            if_z_exist = True
print(if_z_exist)
"""