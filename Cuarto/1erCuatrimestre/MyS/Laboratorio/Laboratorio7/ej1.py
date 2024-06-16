import numpy as np 

Q = np.array( [[0.25, 0.5, 0.25] , [0.5, 0, 0.5], [0.5, 0, 0.5]] )
Q_3 = np.linalg.matrix_power(Q, 3)
Q_4 = np.linalg.matrix_power(Q, 4)
print(Q_4)