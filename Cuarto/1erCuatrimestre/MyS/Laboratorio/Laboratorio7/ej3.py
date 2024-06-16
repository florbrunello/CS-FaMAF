import numpy as np 

Q = np.array( [[0.5, 0.5] , [2/3, 1/3]] )
Q_3 = np.linalg.matrix_power(Q, 3)
print(Q_3)