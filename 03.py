import sys
from string import ascii_letters


def parse_input(puzzle_input):
    return (puzzle_input.splitlines(),)


def part_one(rucksacks):
    total = 0
    for rucksack in rucksacks:
        m = len(rucksack) // 2
        a, b = rucksack[:m], rucksack[m:]

        item, *_ = set(a) & set(b)
        total += ascii_letters.index(item) + 1

    return total


def part_two(rucksacks):
    total = 0
    it = iter(rucksacks)
    while True:
        try:
            a, b, c = next(it), next(it), next(it)
        except StopIteration:
            break

        item, *_ = set(a) & set(b) & set(c)
        total += ascii_letters.index(item) + 1

    return total


class Test:
    example = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 157

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 70


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
