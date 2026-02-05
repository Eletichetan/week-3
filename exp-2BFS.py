from collections import deque

def water_jug_bfs():
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == 2:
            return

        moves = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x - min(x, 3 - y), y + min(x, 3 - y)),
            (x + min(y, 4 - x), y - min(y, 4 - x))
        ]

        for move in moves:
            if move not in visited:
                queue.append(move)
