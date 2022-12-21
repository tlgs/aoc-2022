import sys


def parse_input(puzzle_input):
    m = {"R": 1, "L": -1, "U": 1j, "D": -1j}
    motions = []
    for line in puzzle_input.splitlines():
        d, raw_n = line.split()
        v = m[d]
        motions.extend([v] * int(raw_n))

    updates = {
        2 + 0j: 1,
        -2 + 0j: -1,
        2j: 1j,
        -2j: -1j,
        2 + 2j: 1 + 1j,
        2 + 1j: 1 + 1j,
        1 + 2j: 1 + 1j,
        1 - 2j: 1 - 1j,
        2 - 2j: 1 - 1j,
        2 - 1j: 1 - 1j,
        -1 - 2j: -1 - 1j,
        -2 - 1j: -1 - 1j,
        -2 - 2j: -1 - 1j,
        -1 + 2j: -1 + 1j,
        -2 + 2j: -1 + 1j,
        -2 + 1j: -1 + 1j,
    }

    return (motions, updates)


def part_one(motions, updates):
    head = tail = 0j
    positions = {tail}
    for motion in motions:
        head += motion
        tail += updates.get(head - tail, 0)
        positions.add(tail)

    return len(positions)


def part_two(motions, updates):
    knots = [0j] * 10
    positions = {knots[-1]}
    for motion in motions:
        knots[0] += motion
        for i in range(1, 10):
            change = updates.get(knots[i - 1] - knots[i], 0)
            if change == 0:
                break
            knots[i] += change
        else:
            positions.add(knots[-1])

    return len(positions)


class Test:
    example1 = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

    example2 = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 13

    def test_two(self):
        assert part_two(*parse_input(self.example1)) == 1
        assert part_two(*parse_input(self.example2)) == 36


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
