import copy
import itertools
import sys


def parse_input(puzzle_input):
    cave = set()
    for raw_path in puzzle_input.splitlines():
        coords = []
        for raw_coord in raw_path.split(" -> "):
            x, y = map(int, raw_coord.split(","))
            coords.append((x, y))

        for (a, b), (c, d) in itertools.pairwise(coords):
            if a == c:
                cave |= {(a, y) for y in range(min(b, d), max(b, d) + 1)}
            else:
                cave |= {(x, b) for x in range(min(a, c), max(a, c) + 1)}

    return (cave,)


def part_one(cave):
    cave = copy.copy(cave)

    threshold = max(y for _, y in cave)
    for i in itertools.count():
        x, y = 500, 0
        while True:
            if y == threshold:
                return i

            if (x, y + 1) not in cave:
                y = y + 1
            elif (x - 1, y + 1) not in cave:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in cave:
                x, y = x + 1, y + 1
            else:
                cave.add((x, y))
                break

    raise RuntimeError("unreachable")


def part_two(cave):
    cave = copy.copy(cave)

    threshold = max(y for _, y in cave) + 2

    count = 0
    while (500, 0) not in cave:
        x, y = 500, 0
        while True:
            if y == threshold - 1:
                cave.add((x, y))
                break
            elif (x, y + 1) not in cave:
                y = y + 1
            elif (x - 1, y + 1) not in cave:
                x, y = x - 1, y + 1
            elif (x + 1, y + 1) not in cave:
                x, y = x + 1, y + 1
            else:
                cave.add((x, y))
                break

        count += 1

    return count


class Test:
    example = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 24

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 93


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
