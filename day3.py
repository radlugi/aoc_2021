import numpy as np

input = []
for line in open("input/day3"):
    list = []
    for number in line:
        if not number == "\n":
            list.append(int(number))
    input.append(list)
input = np.array(input).T


def part1(input):
    gammaRate = []
    epsilonRate = []
    for bits in input:
        count1 = np.count_nonzero(bits)
        count0 = len(bits) - count1
        if count0 > count1:
            gammaRate.append(0)
            epsilonRate.append(1)
        else:
            gammaRate.append(1)
            epsilonRate.append(0)
    gammaRate = int("".join(map(str, gammaRate)), 2)
    epsilonRate = int("".join(map(str, epsilonRate)), 2)
    print(gammaRate * epsilonRate)


def part2(input):
    cinput = input
    ogr = []
    crs = []
    for i in range(len(input)):
        r, c = input.shape
        if r == 1:
            ogr = input.T
            ogr = ogr[0].tolist()
            break
        count1 = np.count_nonzero(input[i])
        count0 = input[i].size - count1
        if count1 >= count0:
            ogr.append(1)
            input = np.delete(input, np.where(input[i] == 0), 1)
        else:
            ogr.append(0)
            input = np.delete(input, np.where(input[i] == 1), 1)
    input = cinput
    for i in range(len(input)):
        c, r = input.shape
        if r == 1:
            crs = input.T
            crs = crs[0].tolist()
            break
        count1 = np.count_nonzero(input[i])
        count0 = input[i].size - count1
        if count1 >= count0:
            crs.append(0)
            input = np.delete(input, np.where(input[i] == 1), 1)
        else:
            crs.append(1)
            input = np.delete(input, np.where(input[i] == 0), 1)
    ogr = int("".join(map(str, ogr)), 2)
    crs = int("".join(map(str, crs)), 2)
    print(ogr * crs)


part1(input)
part2(input)
