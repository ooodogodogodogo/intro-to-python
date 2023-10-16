"""""
student_no = {14 : "Dogukan" , 25: "Ali"}

print(student_no.get(14))

color_dict = {"apple" : "green", "banana": "yellow"}
print(color_dict.get("apple"))
"""
from collections import Counter

color_dict = {}
color_dict ["apple"] = ["green"]
print(color_dict)
color_dict["apple"].append("red")
print(color_dict["apple"].index("red"))
#print(color_dict["banana"]) // key error çünkü banana anahtarı yok
print(len(color_dict))
print(len(color_dict["apple"]))
if "apple" in color_dict:
    print(color_dict["apple"])
#color_dict.pop("apple")
color_dict["banana"] = "yellow"
print(color_dict)

for key, value in color_dict.items():
    print (key, value)
    
for key in color_dict:
    print(key, color_dict[key])
    
chars = ["a", "a", "a" ,"b","b","c"]
print(Counter(chars))
"""""
student_no = {14 : "Dogukan" , 25: "Ali", 14 : "Mehmet"}
for key, value in student_no.items():
    print (key, value)
"""
delete_list = []
for key, value in color_dict.items():
    if "red" in value:
        delete_list.append(key)
    print (key, value)
    
for key in delete_list:
    color_dict.pop(key)
print(color_dict)
print(dict(["ahmet"]))

color_dict