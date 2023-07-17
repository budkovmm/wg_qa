import random
from collections import deque


def generate_pangea(M, N, land_ratio):
    field = [['вода' for _ in range(N)] for _ in range(M)]

    num_land_cells = int(M * N * land_ratio)

    land_coordinates = set()
    while len(land_coordinates) < num_land_cells:
        x, y = random.randint(0, M - 1), random.randint(0, N - 1)
        land_coordinates.add((x, y))
        field[x][y] = 'суша'

    return field


def bfs(field, start, end):
    M, N = len(field), len(field[0])
    visited = [[False for _ in range(N)] for _ in range(M)]
    queue = deque([(start, 0)])
    visited[start[0]][start[1]] = True

    while queue:
        curr_pos, distance = queue.popleft()

        if curr_pos == end:
            return distance

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = curr_pos[0] + dx, curr_pos[1] + dy
            if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 'вода' and not visited[nx][ny]:
                queue.append(((nx, ny), distance + 1))
                visited[nx][ny] = True

    return -1


if __name__ == "__main__":
    M = int(input("Введите количество строк (M): "))
    N = int(input("Введите количество столбцов (N): "))
    land_ratio = float(input("Введите долю суши от площади поля (от 0 до 1): "))

    field = generate_pangea(M, N, land_ratio)
    print("Сгенерированная карта:")
    for row in field:
        print(' '.join(row))

    start_x = int(input("Введите координату x точки A: "))
    start_y = int(input("Введите координату y точки A: "))
    end_x = int(input("Введите координату x точки B: "))
    end_y = int(input("Введите координату y точки B: "))

    distance = bfs(field, (start_x, start_y), (end_x, end_x))
    print("Кратчайшее расстояние:", distance)
