numbers = list(map(int, open("input/day1")))


def part1(numbers):
    res = 0
    for i in range(len(numbers)):
        if i == 0:
            continue
        if numbers[i] > numbers[i - 1]:
            res += 1
    print(res)


def part2(numbers):
    res = 0
    for i in range(len(numbers)):
        if i <= 2:
            continue
        a = sum(numbers[i - 2:i + 1])
        b = sum(numbers[i - 3:i])
        if a > b:
            res += 1
    print(res)


part1(numbers)
part2(numbers)
