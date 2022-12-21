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

    start, stack = len(cave), [(500, 0)]
    while stack and stack[-1][1] < threshold:
        x, y = stack[-1]

        if (x, y + 1) not in cave:
            stack.append((x, y + 1))
        elif (x - 1, y + 1) not in cave:
            stack.append((x - 1, y + 1))
        elif (x + 1, y + 1) not in cave:
            stack.append((x + 1, y + 1))
        else:
            cave.add((x, y))
            stack.pop()

    return len(cave) - start


def part_two(cave):
    cave = copy.copy(cave)
    threshold = max(y for _, y in cave) + 2

    def covered(x, y):
        return (x - 1, y - 1) in cave and (x, y - 1) in cave and (x + 1, y - 1) in cave

    no_sand = 0
    for y in range(threshold):
        for x in range(500 - y, 501 + y):
            if (x, y) not in cave and not covered(x, y):
                continue

            cave.add((x, y))
            no_sand += 1

    return threshold**2 - no_sand


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
    sys.exit(main())
