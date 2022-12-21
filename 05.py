import sys


def parse_input(puzzle_input):
    raw_crates, raw_procedure = puzzle_input.split("\n\n")

    *raw_crates, legend = raw_crates.splitlines()
    *_, n = map(int, legend.split())

    stacks = [[] for _ in range(n)]
    for row in raw_crates[::-1]:
        for i, c in enumerate(row[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    procedure = []
    for line in raw_procedure.splitlines():
        raw = line.split()[1::2]
        procedure.append(tuple(map(int, raw)))

    return stacks, procedure


def part_one(stacks, procedure):
    stacks = [x[:] for x in stacks]
    for n, src, dest in procedure:
        for _ in range(n):
            x = stacks[src - 1].pop()
            stacks[dest - 1].append(x)

    return "".join([stack[-1] for stack in stacks])


def part_two(stacks, procedure):
    stacks = [x[:] for x in stacks]
    for n, src, dest in procedure:
        x = stacks[src - 1][-n:]
        del stacks[src - 1][-n:]

        stacks[dest - 1].extend(x)

    return "".join([stack[-1] for stack in stacks])


class Test:
    example = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == "CMZ"

    def test_two(self):
        assert part_two(*parse_input(self.example)) == "MCD"


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
