from numpy import *
from numpy.linalg import *

a=mat([[1,2],[3,4],[5,6]])
b=mat([[1],[2],[3]])
print 'the matrixes'
print a
print b
print b.shape
print b.T.shape
print a.shape

print b.T*a
v, s, wt = svd(a)
print '-----'
print v, s, wt

print a.T

print 'the det of a is: ' + str(det(a[0:2, 0:2]))

print 'element wise operation' + str(sqrt(1+a/2))

print sum(a), sum(a,0)

print a.reshape((6,1))

print zeros((3,4,5))
