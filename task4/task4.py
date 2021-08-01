import sys
def difference(arr, ind):
    s = 0
    for i in range(len(arr)):
        if (i != ind):
            d = abs(arr[i] - arr[ind])
            s += d
    return s
nums = []
file = sys.argv[1]
with open(file) as f:
    for line in f:
        nums.append(int(line.split()[0]))
differences = list()
for i in range(len(nums)):
    differences.append(difference(nums, i))
print(min(differences))
