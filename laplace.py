import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom

i = 4

# boundary matrix
a = np.eye(i)
a[0,1] = -0.25
a[0,2] =-0.25
a[3,1] = -0.25
a[3,2] =-0.25
a[1,0] = -0.25
a[2,0] =-0.25
a[1,3] = -0.25
a[2,3] =-0.25

print('this is the a matrix')
print(a)

# focring vector
b = np.zeros(i)
b[0] = 200
b[1] = 125
b[2] = 150
b[3] = 75

sol = np.linalg.solve(a,b)
# temperature matrix
T = np.zeros((i,i))
for k in range(0,4):
    T[k,0] = 500
for k in range(0, 4):
    T[k, 3] = 200
for k in range(1, 3):
    T[0, k] = 100
for k in range(1, 3):
    T[3, k] = 300

T[1,1] = sol[2]
T[1,2] = sol[3]
T[2,1] = sol[0]
T[2,2] = sol[1]

plt.imshow(T, extent=[0, 3, 0, 3], origin='lower', cmap='inferno')
plt.colorbar(label='°C')
plt.title('Temperature Distribution In Plate')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.show()

print('- darren prashad')


