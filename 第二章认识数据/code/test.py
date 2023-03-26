dataset = []
with open('iris.data') as file:
    for line in file:
        if line.strip() != "":
            cols = line.split(',')
            data = [float(cols[i]) for i in range(len(cols)-1)]
            data.append(cols[-1])
            dataset.append(data)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

setosa_data = [float(data) for data in dataset if "setosa" in data[-1]]
setosa_data = np.array(setosa_data)
print(setosa_data[:,0])
versicolor_data = [float(data) for data in dataset if "versicolor" in data[-1]]
versicolor_data = np.array(versicolor_data)
virginica_data = [float(data) for data in dataset if "virginica" in data[-1]]
virginica_data = np.array(virginica_data)
fig = plt.figure()
ax = plt.gca()

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.scatter(versicolor_data[:,0], versicolor_data[:,1], label = 'versicolor')
ax.scatter(virginica_data[:,0], virginica_data[:,1], label = 'virginica')
ax.scatter(setosa_data[:,0], setosa_data[:,1], label = 'setosa')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
