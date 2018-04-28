import numpy as np
import matplotlib.pyplot as plt
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
results = parser.parse_args()

data = np.loadtxt(results.file)
len = len(data)
points = range(0, len)
# Mean
mean = np.mean(data)

# Median
if (len % 2 == 1):
    median = sorted(data)[len / 2]
else:
    median = np.mean(sorted(data)[len // 2: len // 2 + 1])

# Mode
fq = {}
for item in data:
    fq[item] = 0
for item in data:
    fq[item] += 1
max_fq = np.max(list(fq.values()))
i = 0
while (fq[data[i]] != max_fq):
    i += 1
mode = data[i]

fig = plt.figure()

# Subplot 1 - Scatter Plot
subplot1 = fig.add_subplot(211)

subplot1.plot(data, 'bo')
subplot1.plot(data, 'b-')

subplot1.axhline(y = mean, color='r', linestyle='--')
subplot1.axhline(y = median, color='k', linestyle='--')
fit = np.polyfit(points, data, deg=1)
subplot1.plot(points, fit[0] * points + fit[1], color='g')

plt.xlabel('Position')
plt.ylabel('Value')
plt.title('Scatter Plot')
subplot1.legend(['Data points', 'Data line', 'Mean', 'Median', 'Regression line'])

# Subplot 2 - Distribution
subplot2 = fig.add_subplot(212)

subplot2.plot(fq.keys(), fq.values(), 'bo')
#subplot2.plot(fq.keys(), fq.values(), 'b-')

subplot2.plot(mode, fq[mode], 'ro')
mean_fq = np.mean(list(fq.values()))
subplot2.axhline(y = mean_fq, color='r', linestyle='--')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution')
subplot2.legend(['Frequencies', 'Frequency line', 'Mode', 'Mean frequency'])

print('Mean: ', mean)
print('Median: ', median)
print('Mode: ', mode)

fig.tight_layout()
plt.show()
