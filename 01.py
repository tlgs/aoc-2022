import sys


def parse_input(puzzle_input):
    return [[int(x) for x in raw.splitlines()] for raw in puzzle_input.split("\n\n")]


def part_one(inventories):
    return max(sum(i) for i in inventories)


def part_two(inventories):
    return sum(sorted(sum(i) for i in inventories)[-3:])


class Test:
    example = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

    def test_one(self):
        assert part_one(parse_input(self.example)) == 24000

    def test_two(self):
        assert part_two(parse_input(self.example)) == 45000


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
