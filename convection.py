import matplotlib.pyplot as plt
import numpy as np

## first iteration
i = 5 # cells
L = 1 # meter
dx = (L/i) # meter
n = 5
T_b = 100 # deg cel of bar base
T_a = 20 # deg cel of air
# discretized domain
x = np.zeros(i)
for i in range(1,i+1):
    x[i-1] = i*dx
# temperature matrix
a = np.zeros((i,i))
a[0,0] = -(n*dx)**2 - 3
a[0,1] = 1
a[i-1,i-2] = 1
a[i-1,i-1] = -(n*dx)**2 - 1
for i in range(1,i-1):
    a[i,i-1] = 1
    a[i,i] = (-(n*dx)**2) - 2
    a[i,i+1] = 1
    i = 5
# solution matrix
b = np.zeros(i)
b[0] = (-(n*dx)**2) * T_a - 2*T_b
for i in range(1, i):
    b[i] = - (n*dx)**2 * T_a

sol_1 = np.linalg.solve(a,b)
plt.plot(x,sol_1, 'o', label='5 Cells')

## second interation
i = 10 # cells
L = 1 # meter
dx = (L/i) # meter
n = 5
T_b = 100 # deg cel of bar base
T_a = 20 # deg cel of air
# discretized domain
x = np.zeros(i)
for i in range(1,i+1):
    x[i-1] = i*dx

# temperature matrix
a = np.zeros((i,i))
a[0,0] = -(n*dx)**2 - 3
a[0,1] = 1
a[i-1,i-2] = 1
a[i-1,i-1] = -(n*dx)**2 - 1
for i in range(1,i-1):
    a[i,i-1] = 1
    a[i,i] = (-(n*dx)**2) - 2
    a[i,i+1] = 1
i = 10

# solution matrix
b = np.zeros(i)
b[0] = (-(n*dx)**2) * T_a - 2*T_b
for i in range(1, i):
    b[i] = - (n*dx)**2 * T_a
sol_10 = np.linalg.solve(a,b)
plt.plot(x,sol_10, 'o', label='10 Cells')

## third iteration
i = 15 # cells
L = 1 # meter
dx = (L/i) # meter
n = 5
T_b = 100 # deg cel of bar base
T_a = 20 # deg cel of air

# discretized domain
x = np.zeros(i)
for i in range(1,i+1):
    x[i-1] = i*dx
# temperature matrix
a = np.zeros((i,i))
a[0,0] = -(n*dx)**2 - 3
a[0,1] = 1
a[i-1,i-2] = 1
a[i-1,i-1] = -(n*dx)**2 - 1
for i in range(1,i-1):
    a[i,i-1] = 1
    a[i,i] = (-(n*dx)**2) - 2
    a[i,i+1] = 1
i = 15

# solution matrix
b = np.zeros(i)
b[0] = (-(n*dx)**2) * T_a - 2*T_b
for i in range(1, i):
    b[i] = - (n*dx)**2 * T_a
sol_15 = np.linalg.solve(a,b)

x_analytic = np.linspace(0, 1, 100)
T_analytic = np.cosh(n*(L-x_analytic))*(T_b- T_a)/np.cosh(n*L) + T_a

plt.plot(x,sol_15, 'o', label='15 Cells')
plt.plot(x_analytic,T_analytic, 'k')

plt.xlabel('x (mm)')
plt.ylabel('T (c)')
plt.title('Temperature Distribution in Bar')
hfont = {'fontname':'Times New Roman'}
plt.legend()
plt.grid()
plt.show()
