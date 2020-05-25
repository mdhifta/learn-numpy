import numpy as np

a = np.array(([1,2],[3,4]))
b = np.ones(([2,2]))

print("Matrix a : ")
print(a)

print("Matrix b : ")
print(b)

# perkalian matriks
c1 = np.dot(a,b)
c2 = a.dot(b)

print("Matrix c1 : ")
print(c1)

print("Matrix c2 : ")
print(c2)
