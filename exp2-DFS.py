def water_jug_dfs():
    stack = [(0, 0)]
    visited = set()

    while stack:
        x, y = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == 2:
            return

        # Possible moves
        moves = [
            (4, y),                     # Fill 4L jug
            (x, 3),                     # Fill 3L jug
            (0, y),                     # Empty 4L jug
            (x, 0),                     # Empty 3L jug
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # Pour 4L → 3L
            (x + min(y, 4 - x), y - min(y, 4 - x))   # Pour 3L → 4L
        ]

        for move in moves:
            if move not in visited:
                stack.append(move)
