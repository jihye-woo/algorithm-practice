def brute_force(n):
    cnt = 0
    for x in range(N - n):
        for y in range(N - n):
            if spaces[y][x]:
                cnt += fillN(x, y, n)
    return cnt


def fillN(x, y, n):
    for i in range(n):
        for j in range(n):
            if not spaces[y + i][x + j]:
                return 0
    return 1


def print_result(result, total):
    print('total:', total)
    for key in result:
        print('size[' + str(key) + ']: ' + str(result[key]))


global N, spaces
N = int(input())

spaces = [[] for i in range(N)]
result = dict()
total = 0

for i in range(N):
    for j in input():
        spaces[i].append(int(j))

for n in range(1, N):
    num = brute_force(n)
    if num > 0:
        result[n] = num
        total += num

print_result(result, total)
