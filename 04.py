import sys


def parse_input(puzzle_input):
    pairs = []
    for line in puzzle_input.splitlines():
        raw_fst, raw_snd = line.split(",")
        fst = tuple(int(x) for x in raw_fst.split("-"))
        snd = tuple(int(x) for x in raw_snd.split("-"))

        pairs.append((fst, snd))

    return (pairs,)


def part_one(pairs):
    total = 0
    for (a, b), (c, d) in pairs:
        total += (a <= c <= d <= b) or (c <= a <= b <= d)

    return total


def part_two(pairs):
    total = 0
    for (a, b), (c, d) in pairs:
        total += (a <= c <= b) or (c <= a <= d)

    return total


class Test:
    example = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 2

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 4


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
