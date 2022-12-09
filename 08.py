import sys
from collections import defaultdict


def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()
    grid = [[int(x) for x in line] for line in lines]

    assert len(grid) == len(grid[0])  # assuming square matrix from now on

    return (grid, len(lines))


def part_one(grid, n):
    visible = set()

    # up / down
    for x in range(n):
        for traversal in [range(n), range(n - 1, -1, -1)]:
            v = -1
            for y in traversal:
                if grid[y][x] > v:
                    visible.add((x, y))
                    v = grid[y][x]

    # left / right
    for y in range(n):
        for traversal in [range(n), range(n - 1, -1, -1)]:
            v = -1
            for x in traversal:
                if grid[y][x] > v:
                    visible.add((x, y))
                    v = grid[y][x]

    return len(visible)


def part_two(grid, n):
    scores = defaultdict(lambda: 1)

    # up / down
    for x in range(n):
        stack_a, stack_b = [], []
        for ya, yb in zip(range(n), range(n - 1, -1, -1)):
            while stack_a and stack_a[-1][1] < grid[ya][x]:
                stack_a.pop()

            while stack_b and stack_b[-1][1] < grid[yb][x]:
                stack_b.pop()

            scores[x, ya] *= (ya - stack_a[-1][0]) if stack_a else ya
            scores[x, yb] *= (stack_b[-1][0] - yb) if stack_b else n - 1 - yb

            stack_a.append((ya, grid[ya][x]))
            stack_b.append((yb, grid[yb][x]))

    # left / right
    for y in range(n):
        stack_a, stack_b = [], []
        for xa, xb in zip(range(n), range(n - 1, -1, -1)):
            while stack_a and stack_a[-1][1] < grid[y][xa]:
                stack_a.pop()

            while stack_b and stack_b[-1][1] < grid[y][xb]:
                stack_b.pop()

            scores[xa, y] *= (xa - stack_a[-1][0]) if stack_a else xa
            scores[xb, y] *= (stack_b[-1][0] - xb) if stack_b else n - 1 - xb

            stack_a.append((xa, grid[y][xa]))
            stack_b.append((xb, grid[y][xb]))

    return max(scores.values())


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
