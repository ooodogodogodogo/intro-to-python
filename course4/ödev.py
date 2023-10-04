import time
import random

#başlangıç 13.08
"""""
arr = [8,9,5,4,1]
arr.sort()
print(arr)
kucuk_toplam = arr[0]+arr[1]+arr[2]+arr[3]
print(kucuk_toplam)
arr.sort(reverse=True)
print(arr)
buyuk_toplam = arr[0]+arr[1]+arr[2]+arr[3]
print(buyuk_toplam)



#bitiş 13.15


"""

"""""
arr = [8,9,5,4,1]
arr.sort()
print(arr)
kucuk_toplam = arr[0]+arr[1]+arr[2]+arr[3]
print(kucuk_toplam)
buyuk_toplam = arr[4]+arr[1]+arr[2]+arr[3]
print(buyuk_toplam)
"""



"""""
arr = [random.randint(0,100) for i in range(10000000)]
start_time = time.perf_counter()

arr.sort()
sort_time =  time.perf_counter() 
print((sort_time-start_time)*1e6)

#print(arr)
total = 0
for i in arr:
    total = total + i
print(total - arr[0])
print(total - arr[-1])

end_time = time.perf_counter() 
print((end_time-start_time)*1e6)
"""""

arr = [random.randint(0,100) for i in range(10000000)]
start_time = time.perf_counter()

total = sum(arr)
print(total-min(arr),total-max(arr))
end_time = time.perf_counter() 

print((end_time-start_time)*1e6)