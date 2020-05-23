import numpy as np 

mylist = [1, 2, 3]
x = np.array(mylist)

y = np.array([4, 5, 6])

m = np.array([[7, 8, 9], [10, 11, 12]])

#print(m.shape)

n = np.arange(0, 36, 1) # start at 0 count up by 2, stop before 30
n = n.reshape(6, 6) # reshape array to be 3x5
n = n.reshape(36)[::7]
print(n)