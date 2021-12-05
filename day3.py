import numpy as np

arr = []
for line in open("input/day3"):
    row = [int(number) for number in line if not number == "\n"]
    arr.append(row)
arr = np.array(arr).T


def part1(arr):
    gammaRate, epsilonRate = [], []
    for row in arr:
        ones = np.count_nonzero(row)
        zeros = len(row) - ones
        if zeros > ones:
            gammaRate.append(0)
            epsilonRate.append(1)
        else:
            gammaRate.append(1)
            epsilonRate.append(0)
    gammaRate = int("".join(map(str, gammaRate)), 2)
    epsilonRate = int("".join(map(str, epsilonRate)), 2)
    print(gammaRate * epsilonRate)


def part2(arr):
    ogr, crs = [], []
    arr_copy = arr
    for i in range(len(arr)):
        if arr.shape[-1] == 1:
            ogr = arr.T
            ogr = ogr[0].tolist()
            break
        ones = np.count_nonzero(arr[i])
        zeros = arr[i].size - ones
        if ones >= zeros:
            ogr.append(1)
            arr = np.delete(arr, np.where(arr[i] == 0), 1)
        else:
            ogr.append(0)
            arr = np.delete(arr, np.where(arr[i] == 1), 1)
    for i in range(len(arr_copy)):
        if arr_copy.shape[-1] == 1:
            crs = arr_copy.T
            crs = crs[0].tolist()
            break
        ones = np.count_nonzero(arr_copy[i])
        zeros = arr_copy[i].size - ones
        if ones >= zeros:
            crs.append(0)
            arr_copy = np.delete(arr_copy, np.where(arr_copy[i] == 1), 1)
        else:
            crs.append(1)
            arr_copy = np.delete(arr_copy, np.where(arr_copy[i] == 0), 1)
    ogr = int("".join(map(str, ogr)), 2)
    crs = int("".join(map(str, crs)), 2)
    print(ogr * crs)


part1(arr)
part2(arr)
