import numpy as np
from matplotlib import pyplot as plt

# using numpy to generate 1000 random numbers with a mean of 5 using the loc argument and std of 2 using the scale argument
data = np.random.normal(loc=5, scale=2, size=1000)

# creating a histogram with this data
plt.hist(data, bins=30, color='blue', edgecolor ='black', alpha=0.7, label='Histogram')

# generating x values for the fucntion h(x) = x^3 in range 0 - 10 using linspace (https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html)
x = np.linspace(0, 10, num=1000)
y = x**3

plt.plot(x, y, color='red', label='h(x) = x^3')

plt.title('Histogram and function h(x) = x^3')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


plt.show()