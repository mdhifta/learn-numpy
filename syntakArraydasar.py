import numpy as np

# make a vector
a = np.array([11,2,3,4,5,6,7])
b = np.array([1.2,3,2.3,4,5])

#make a vector with range
c = np.arange(1,10,2)

#make linspace
d = np.linspace(1,10,4)

#make array multidimension / matrix
e = np.array([(1,2,3), (4,5,6)])

#make matrix with nilai zero
f1 = np.zeros(5)
# with 5 x 5
f2 = np.zeros((5,5))

#matriks with nilai one
g1 = np.ones(5)
# with 5 x 5
g2 = np.ones((5,5))

#make matriks identitas
h1 = np.identity(5)
h2 = np.eye(5)
#out
print(h2)
print(h1)
