global prefers, watch, types

# class Content:
#     def __init__(self, row, col, genre, watch):
#         self.row = row
#         self.col = col
#         self.genre = genre
#         self.prefer = prefers[genre]
#         self.watch = watch

def watch_converter(watch):
    if watch == 'Y': return 2
    if watch == 'O': return 1
    return 0

def create_content(row, col):
    watch = watch_converter(watchs[row][col])
    genre =types[row][col]
    return [row, col, genre, prefers[genre], watch]
    # return Content(row, col, types[row][col], watch)

def print_result(results):
    for result in results:
        if result[WATCH] > 0:
            print(result[GENRE], result[PREFER], result[ROW], result[COL])

prefers = dict()
results = []
# init prefer
prefer_info = input()
prefer_info = prefer_info.split(" ")
for idx, prefer in enumerate(prefer_info):
    genre = chr(65 + idx)
    prefers[genre] = float(prefer)

# init size
size_info = input()
size_info = size_info.split(" ")
N, M = int(size_info[0]), int(size_info[1])

# init watch and types
watchs = [list(input()) for row in range(N)]
types = [list(input()) for row in range(N)]

for row in range(N):
    for col in range(M):
        results.append(create_content(row, col))

ROW, COL, GENRE, PREFER, WATCH = 0, 1, 2, 3, 4
results.sort(key= lambda x: (-x[WATCH], -x[PREFER], x[ROW], x[COL]))

print_result(results)





