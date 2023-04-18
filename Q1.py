import csv
import matplotlib.pyplot as plt

file = open('Image1.csv')
csvreader = csv.reader(file)
data1_x = []
data1_y = []
data2_x = []
data2_y = []
data3_x = []
data3_y = []
for i in range(200):
    nxtln = next(csvreader)
    data1_x.append(int(nxtln[0]))
    data1_y.append(int(nxtln[1]))
for i in range(200):
    nxtln = next(csvreader)
    data2_x.append(int(nxtln[0]))
    data2_y.append(int(nxtln[1]))
for i in range(200):
    nxtln = next(csvreader)
    data3_x.append(int(nxtln[0]))
    data3_y.append(int(nxtln[1]))
file.close()

plt.scatter(data1_x, data1_y, color='r', label='Data 1')
plt.scatter(data2_x, data2_y, color='g', label='Data 2')
plt.scatter(data3_x, data3_y, color='b', label='Data 3')
plt.legend()
plt.show()