import numpy as np 

Q = np.array( [[0.5, 0.25, 0.25] , [1/3, 0, 2/3], [0.5, 0.5, 0]] )
Q_2 = np.linalg.matrix_power(Q, 2)
print(Q_2)