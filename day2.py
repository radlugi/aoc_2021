def part1():
    depth, hori = 0, 0
    for line in open("input/day2"):
        com, num = line.split(" ")
        num = int(num)
        if com == "forward":
            hori += num
        elif com == "down":
            depth += num
        else:
            depth -= num
    print(depth * hori)


def part2():
    depth, hori, aim = 0, 0, 0
    for line in open("input/day2"):
        com, num = line.split(" ")
        num = int(num)
        if com == "forward":
            hori += num
            depth += aim * num
        elif com == "down":
            aim += num
        else:
            aim -= num
    print(depth * hori)


part1()
part2()
