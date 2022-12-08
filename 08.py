import sys
from itertools import count, cycle


def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()
    grid = {(x, y): int(v) for y, line in enumerate(lines) for x, v in enumerate(line)}
    return (grid, len(lines))


def part_one(grid, n):
    visible = set()

    # up / down
    for x in range(n):
        for traversal in [range(n), range(n - 1, -1, -1)]:
            v = -1
            for y in traversal:
                if grid[x, y] > v:
                    visible.add((x, y))
                    v = grid[x, y]

    # left / right
    for y in range(n):
        for traversal in [range(n), range(n - 1, -1, -1)]:
            v = -1
            for x in traversal:
                if grid[x, y] > v:
                    visible.add((x, y))
                    v = grid[x, y]

    return len(visible)


def spiral(x=0, y=0):
    directions = cycle([(-1, 0), (0, -1), (1, 0), (0, 1)])
    yield x, y

    for i in count(1):
        for _ in range(2):
            dx, dy = next(directions)
            for _ in range(i):
                x, y = x + dx, y + dy
                yield x, y


def countwhile(predicate, iterable):
    count = 0
    for x in iterable:
        if predicate(x):
            count += 1
        else:
            break

    return count


def part_two(grid, n):
    maximums = {
        (x, y): y * (n - 1 - y) * x * (n - 1 - x) for y in range(n) for x in range(n)
    }

    best = 0
    for x, y in spiral(n // 2, n // 2):
        if best > maximums[x, y]:
            break

        h = grid[x, y]
        up___ = countwhile(lambda v: v < h, (grid[x, yy] for yy in range(y - 1, 0, -1)))
        down_ = countwhile(lambda v: v < h, (grid[x, yy] for yy in range(y + 1, n - 1)))
        left_ = countwhile(lambda v: v < h, (grid[xx, y] for xx in range(x - 1, 0, -1)))
        right = countwhile(lambda v: v < h, (grid[xx, y] for xx in range(x + 1, n - 1)))

        score = (1 + up___) * (1 + down_) * (1 + left_) * (1 + right)
        best = score if score > best else best

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
