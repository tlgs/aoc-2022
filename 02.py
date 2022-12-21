import sys


def parse_input(puzzle_input):
    return (puzzle_input.splitlines(),)


def part_one(strategy_guide):
    score = {
        "A X": 1 + 3,
        "A Y": 2 + 6,
        "A Z": 3 + 0,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 1 + 6,
        "C Y": 2 + 0,
        "C Z": 3 + 3,
    }

    return sum(score[line] for line in strategy_guide)


def part_two(strategy_guide):
    score = {
        "A X": 3 + 0,
        "A Y": 1 + 3,
        "A Z": 2 + 6,
        "B X": 1 + 0,
        "B Y": 2 + 3,
        "B Z": 3 + 6,
        "C X": 2 + 0,
        "C Y": 3 + 3,
        "C Z": 1 + 6,
    }

    return sum(score[line] for line in strategy_guide)


class Test:
    example = """\
A Y
B X
C Z
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 15

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 12


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
