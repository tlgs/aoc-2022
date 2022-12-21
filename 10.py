import sys


def parse_input(puzzle_input):
    program = puzzle_input.splitlines()
    return (program,)


def part_one(program):
    d, X = [], 1
    for instruction in program:
        match instruction.split():
            case ["noop"]:
                d.append(X)

            case "addx", v:
                d.append(X)
                d.append(X)
                X += int(v)

    return sum(i * d[i - 1] for i in range(20, 221, 40))


def part_two(program):
    d, X = [], 1
    for instruction in program:
        match instruction.split():
            case ["noop"]:
                d.append(X)

            case "addx", v:
                d.append(X)
                d.append(X)
                X += int(v)

    crt = "".join(["#" if abs(d[i] - (i % 40)) <= 1 else "." for i in range(240)])
    return "\n".join([crt[i : i + 40] for i in range(0, 240, 40)]) + "\n"


class Test:
    example = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 13140

    def test_two(self):
        expected = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

        assert part_two(*parse_input(self.example)) == expected


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle), sep="\n")


if __name__ == "__main__":
    sys.exit(main())
