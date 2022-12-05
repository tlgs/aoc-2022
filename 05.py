import re
import sys


def parse_input(puzzle_input):
    raw_crates, raw_procedure = puzzle_input.split("\n\n")

    *raw_crates, legend = raw_crates.splitlines()
    n = int(legend.split()[-1])

    stacks = [[] for _ in range(n)]
    for raw_row in raw_crates[::-1]:
        row = raw_row.ljust(4 * n - 1)
        for i in range(n):
            x = i * 4 + 1
            if row[x] != " ":
                stacks[i].append(row[x])

    procedure = []
    pat = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    for line in raw_procedure.splitlines():
        m = pat.match(line)
        procedure.append(tuple(int(x) for x in m.groups()))

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
    raise SystemExit(main())
