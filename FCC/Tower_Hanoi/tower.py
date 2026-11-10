def hanoi_solver(n):
    tower_a = list(range(n, 0, -1))
    tower_b = []
    tower_c = []
    moves = [f"{tower_a} {tower_b} {tower_c}"]

    def move(n, source, auxiliary, destination):
        if n == 0:
            return
        move(n - 1, source, destination, auxiliary)
        disk = source.pop()
        destination.append(disk)
        moves.append(f"{tower_a} {tower_b} {tower_c}")
        move(n - 1, auxiliary, source, destination)

    move(n, tower_a, tower_b, tower_c)
    return "\n".join(moves)


if __name__ == "__main__":
    print(hanoi_solver(3))
