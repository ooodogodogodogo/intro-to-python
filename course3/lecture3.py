"""""
print("ab",3,7,1==1)

a = 3>2
b = a*5
print(a)
print(not a)
"""


"""""
word1= "Benim adim Dogukan"
word_character_list= list(word1)
word_character_list.append(".")
word_character_list.remove("a")
#word_character_list.insert(word_character_list.index("n")+1,".")
#word_character_list.reverse()
#print(word_character_list.count(" "))
#word2=word1.replace(" ", "")
word_list=word1.split(" ")
listwords = ["Benim", "adim","dogukan"]
print(word_character_list)
word2 = " hehehe ".join(listwords)
print(word2)
#print(word_list[0])
"""

num_list= []
num_list = [1,2,3,4,5,6]
num_list[2] = 10
num_list.sort(reverse=True)
init_set = set()
#print(num_list[:3] + [5] + num_list[3:] )
print(num_list)
ones_list = [1] *10
#print(ones_list)
word1 = "abc"
word2 = word1
word1=word1.upper()
print(word2)
list1 = [1,2,3]
list2 = list1.copy() 
list1.append(4)
print(list2)

for element in word1:
    if element == "C":
        break
    print(element)
print("ahmet")
for element in range(1,10):
    if element == "C":
        break
    print(element)
    
    
list1 = [1,2,3,4,5,6,7,8,9]
total = 0

for number in list1:
    if number %2 == 0:
        total += number
print(total)
        