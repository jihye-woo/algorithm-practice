global results, contents, COL, ROW
import sys

class State:
    def __init__(self, visited, horizontal):
        self.visited = visited
        self.horizontal = horizontal

    def is_visited(self, x, y):
        return (x, y) in self.visited

    def down(self, x, y):
        visited = self.visited.union({(x, y)})
        return State(visited, self.horizontal)

    def left(self, x, y):
        visited = self.visited.union({(x, y)})
        return State(visited, self.horizontal + 1)

    def right(self, x, y):
        visited = self.visited.union({(x, y)})
        return State(visited, self.horizontal + 1)

def DFS(x, y, state):
    go(x, y + 1, state, 'DOWN')
    go(x - 1, y, state, 'LEFT')
    go(x + 1, y, state, 'RIGHT')

def go(x, y, state, dir):
    if x < 0 or x >= COL or y < 0 or y >= ROW:
        return

    if contents[y][x] == '.' and not state.is_visited(x, y):
        if y == ROW - 1:
            results.append(state)
            return

        if dir == 'DOWN':
            DFS(x, y, state.down(x, y))
        elif dir == 'LEFT':
            DFS(x, y, state.left(x, y))
        elif dir == 'RIGHT':
            DFS(x, y, state.right(x, y))


size_info = input().split()
COL, ROW = int(size_info[0]), int(size_info[1])

contents = [list(input()) for row in range(ROW)]
results = []

# find the seeds
for seed in range(COL):
    if contents[0][seed] == 'c':
        visited = set()
        visited.add((0, seed))
        DFS(0, seed, State(visited, 0))

min_horizon = sys.maxsize
for result in results:
    min_horizon = min(result.horizontal, min_horizon)

print(min_horizon)
