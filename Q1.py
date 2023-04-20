import csv
import matplotlib.pyplot as plt

file = open('Image1.csv')
csvreader = csv.reader(file)
data1_y1 = []
data1_y2 = []
data2_y1 = []
data2_y2 = []
data3_y1 = []
data3_y2 = []
for i in range(200):
    nxtln = next(csvreader)
    data1_y1.append(float(nxtln[1]))
    data1_y2.append(float(nxtln[2]))
for i in range(200):
    nxtln = next(csvreader)
    data2_y1.append(float(nxtln[1]))
    data2_y2.append(float(nxtln[2]))
for i in range(200):
    nxtln = next(csvreader)
    data3_y1.append(float(nxtln[1]))
    data3_y2.append(float(nxtln[2]))
file.close()

plt.scatter(data1_y1, data1_y2, color='r', label='Data 1')
plt.scatter(data2_y1, data2_y2, color='g', label='Data 2')
plt.scatter(data3_y1, data3_y2, color='b', label='Data 3')
plt.legend()
plt.show()