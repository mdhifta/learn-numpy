#indexing, slicing, and iterasi
import numpy as np

a = np.arange(10)**2

print(a)

#get nilai with numpy
print('Elmen ke 1 dari a adalah : ', a[0])
print('Elmen ke 6 dari a adalah : ', a[5])
print('Elmen ke terakhir dari a adalah : ', a[-1]) # get nilai terakhir

#slicing (mengambil rentang nilai array) with numpy
print('Elmen ke 1 - 6  [a] adalah : ', a[0:6]) #nilai belakang ekslusif [start,end]
print('Elmen ke 4 sampai akhir adalah : ', a[3:])
print('Elmen dari awal sampai 5 adalah : ', a[:5])

#iterasi with numpy
b = 0
for i in a:
    b+=1
    print('value ke-',b,'= ',i)
