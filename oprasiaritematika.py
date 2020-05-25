import numpy as np

# array python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array with numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# penjumlahan python
hasil1 = a + b
# penjumlahan numpy (Elmenentwise opration)
hasil2 = anp + bnp

# pengurangan python
# hasil3 = a - b  this error!
# pengurangan numpy (Elmenentwise opration)
hasil4 = anp - bnp

# perkalian python
# hasil5 = a * b  this error!
# pengurangan numpy (Elmenentwise opration)
hasil6 = anp * bnp

# perkalian python
# hasil7 = a / b  this error!
# pengurangan numpy (Elmenentwise opration)
hasil8 = anp / bnp

# make kuadrat
hasil9 = anp**2

# example if use multidimendsi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil10 = c + d
hasil11 = c - d
hasil12 = c * d

print(hasil12)
