import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Plotting the data
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

# sine wave
# plt.plot(x,y)
# plt.show()


# cosine wave
# plt.plot(x,z)
# plt.show()


a = [i for i in range(10)]
b = [i for i in range(10)]

# bar graph
# plt.bar(a,b)
# plt.show()

# Scatter graph
plt.scatter(a,b)
plt.show()
