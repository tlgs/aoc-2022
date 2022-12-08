import sys
from itertools import product, takewhile


def parse_input(puzzle_input):
    grid = [[int(x) for x in line] for line in puzzle_input.splitlines()]
    return (grid,)


def part_one(grid):
    n_rows, n_cols = len(grid), len(grid[0])

    visible = {
        *product((0, n_cols - 1), range(n_rows)),
        *product(range(n_cols), (0, n_rows - 1)),
    }
    for (x, y) in product(range(1, n_cols - 1), range(1, n_rows - 1)):
        h = grid[y][x]

        up = all((grid[my][x] < h for my in range(0, y)))
        down = all((grid[my][x] < h for my in range(y + 1, n_rows)))
        left = all((grid[y][mx] < h for mx in range(0, x)))
        right = all((grid[y][mx] < h for mx in range(x + 1, n_cols)))

        if any([up, down, left, right]):
            visible.add((x, y))

    return len(visible)


def distance(height, trees):
    n = sum(1 for _ in takewhile(lambda x: x < height, trees))
    return n + 1


def part_two(grid):
    n_rows, n_cols = len(grid), len(grid[0])

    best = 0
    for (x, y) in product(range(1, n_cols - 1), range(1, n_rows - 1)):
        h = grid[y][x]

        up = distance(h, (grid[my][x] for my in range(y - 1, 0, -1)))
        down = distance(h, (grid[my][x] for my in range(y + 1, n_rows - 1)))
        left = distance(h, (grid[y][mx] for mx in range(x - 1, 0, -1)))
        right = distance(h, (grid[y][mx] for mx in range(x + 1, n_cols - 1)))

        best = max(best, up * down * left * right)

    return best


class Test:
    example = """\
30373
25512
65332
33549
35390
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 21

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 8


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
