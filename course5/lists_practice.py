"""
liste1=[]
liste2 = ['ali', 'ahmet' , 'ayşe',' mehmet', 'fazil','hüsnü','sevda']
print(len(liste1))
print(len(liste2))
print(liste2[0])
print(liste2[3])
print(liste2[6])
kardiz="istanbul büyükşehir belediyesi"
liste=kardiz.split()
print(liste)
mixed_data_types= ['busra',32,1.65,'bekar','istanbul']
print(mixed_data_types)
it_companies=['facebook','google','amazon','microsoft','apple']

print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[2])
print(it_companies[4])
print(it_companies[:4])
print(it_companies[::2])
it_companies.append('tiktok')
print(it_companies)
it_companies.remove('facebook')
print(it_companies)
IT_comp='telegram'
insert_index=len(it_companies)//2
it_companies.insert(insert_index,IT_comp)
print(it_companies)
print(it_companies[0])
middle_company=it_companies[(len(it_companies))//2]
print(middle_company)
middle_data = mixed_data_types[(len(mixed_data_types))//2]
print(middle_data)
it_companies.append("whatsapp")
print(it_companies)
insert_eleman='lenovo'
insert_yer=len((it_companies))//2
it_companies.insert(insert_yer,insert_eleman)
print(it_companies)
#14 yok
does_exist='lenovo' in it_companies
print(does_exist)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.remove
del it_companies[0:3]
print(it_companies)
del it_companies[-3:-1]
print(it_companies)
#19 yok

middle_index= (len(it_companies))//2
it_companies.pop(middle_index)
print(it_companies)
last_index=(len(it_companies)//2)
it_companies.pop(last_index)
print(it_companies)
#son elemanı bulma silme
del it_companies
print(it_companies)
"""
ages=[19,22,19,24,20,25,26,24,25,24,22,24]
ages.sort()
print(ages)
min_eleman= ages[0]
print(min_eleman)
print(len(ages))
max_eleman=ages[len(ages)-1]
print(max_eleman)
n=len(ages)
if n%2==1:
    median=ages[n//2]
else:
    middle1=ages[n//2-1]
    middle2=ages[n//2]
    median=(middle1+middle2)/2  
print(median)
toplam=0
for i in ages:
    toplam += i
print(toplam)
ortalama=toplam/len(ages)
print(ortalama)
range_ages=max_eleman-min_eleman
print(range_ages)
    