"""print('30days\t of\t python')
print('cooding\t for \ all')
"""
str1,str2,str3,str4='Thirty', 'Days', 'Of', 'Python'
str5 =str1+str2+str3+str4
strlist= ['Thirty', 'Days', 'Of', 'Python']
listtostring= "".join(strlist)
company = 'Coding For All People'
nocodecompany= company[len('Coding'):] if company[:len('Coding')] == 'Coding' else company
print(nocodecompany)
"""
print(company)
print( len(company) )
print( company.upper())
print(company.capitalize())
print(company.swapcase())
print(company.remove("cooding"))

print (company.replace("Cooding","")) #doğru mu?

x= "Cooding" in company
print(x)
print(company.replace("Cooding For All","Python"))
print(company.split( )) #dogru mu?
comp = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(comp.split( ))
first_letter = company[0]
print(first_letter)
"""
x = "C"
y = "F"
print(company.index(x))
print(company.index(y))
print(company.rfind(y))
word ="Cumleyi cunku ile bitiremezsin cunku cunku bir baslangıctır"
z = "cunku"
print(word.index(z)) 
print(word.find(z))
print(word.rindex(z))
sentence ='You cannot end a sentence with because because because is a conjunction'
t = 'because'
print(sentence.index(t))
m='Cooding'

print(company.startswith(m))
print(company.endswith(m))
