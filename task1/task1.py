import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
def prints(a, n, ind):
    arr = list()
    i = ind

    while i < n + ind :
        arr.append(a[(i % n)])
        i = i + 1
    return arr

path = list()
a = list()
for j in range(1, n+1):
    a.append(j)
i = m - 1
arr = [-1]
while arr[0] != a[0]:
    arr = prints(a, n, i);
    i += m - 1
    path.append(arr[0])

print(a[0], end = "")
for i in range(len(path)-1):
    print(path[i], end = "")
