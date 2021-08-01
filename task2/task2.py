from math import sqrt
import sys
eps = 0.000001
data = []
file1 = sys.argv[1]
file2 = sys.argv[2]
with open(file1) as f:
    for line in f:
        data.append([float(x) for x in line.split()])
R = data[1][0]
C_x = data[0][0]
C_y = data[0][1]
points = []
with open(file2) as f:
    for line in f:
        points.append([float(x) for x in line.split()])
for p in points:
    d = sqrt((p[0]-C_x)**2 + (p[1]-C_y)**2)
    if (abs(R - d) <= eps):
        print(0)
    if (d < R):
        print(1)
    if (d > R):
        print(2)
