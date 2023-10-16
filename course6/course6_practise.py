"""
dict2={ 
       'isim' : 'mesut' ,
       'yas': 32 ,
       'lokasyon':'istanbul'
    
}
dict3={
    'isim': 'mesut',
    'yas': 32,
    'lokasyon' : {
        'dogdugu_sehir': 'istanbul',
        'yasadıgı_sehir': 'berlin'
    }
    
}
print(dict2['yas'])
print(dict2.keys())
print(dict3['lokasyon']['yasadıgı_sehir'])

#30daysofpython 9. gün egzersizleri
yas= int(input('yasinizi girin :'))
if yas>=18:
    print('ehliyet alabilirsiniz')
else:
    print('ehliyet alamazsınız')

yas =int(input('yasinizi girin :'))
kalan_yil=18-yas
if yas>=18:
    print('ehliyet alabilirsiniz')
else:
    print ('ehliyet almana', kalan_yil , 'yıl kaldı')


benim_yasim=int(input('benim_yasim:'))
senin_yasin=int(input('senin_yasin'))
fark=abs(benim_yasim-senin_yasin)
if benim_yasim>senin_yasin:
    print('benim yasim senin yasından',fark,'yaş büyük')
else:
    print('senin yasin benim yasimdan',fark,'kadar büyük')
"""
yas=int(input())
if yas > 18:
    print("ok")

  