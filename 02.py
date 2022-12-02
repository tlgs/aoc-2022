import sys


def parse_input(puzzle_input):
    return [tuple(line.split()) for line in puzzle_input.splitlines()]


def part_one(strategy_guide):
    outcome_score = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,
        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }

    total = 0
    for a, b in strategy_guide:
        total += ord(b) - 87
        total += outcome_score[(a, b)]

    return total


def part_two(strategy_guide):
    shape_score = {
        ("A", "X"): 3,
        ("A", "Y"): 1,
        ("A", "Z"): 2,
        ("B", "X"): 1,
        ("B", "Y"): 2,
        ("B", "Z"): 3,
        ("C", "X"): 2,
        ("C", "Y"): 3,
        ("C", "Z"): 1,
    }

    total = 0
    for a, b in strategy_guide:
        total += shape_score[(a, b)]
        total += (ord(b) - 88) * 3

    return total


class Test:
    example = """\
A Y
B X
C Z
"""

    def test_one(self):
        assert part_one(parse_input(self.example)) == 15

    def test_two(self):
        assert part_two(parse_input(self.example)) == 12


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
