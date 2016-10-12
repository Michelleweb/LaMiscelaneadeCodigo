import numpy as np
I =np.eye(n)
A =np.array([[1,0,0],[0,1,1],[0,0,3]])
A.dot(I) #AxI = A
np.linalg.det(A)
A_inv = np.linalig.inv(A)
print A_inv
