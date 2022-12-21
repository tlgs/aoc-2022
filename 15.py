import itertools
import re
import sys


def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def merge_ranges(ranges):
    tmp = sorted(ranges, key=lambda r: (r.start, r.stop), reverse=True)

    merged = [tmp.pop()]
    while tmp:
        prev, curr = merged[-1], tmp.pop()
        if curr.start <= prev.stop:
            merged[-1] = range(prev.start, max(prev.stop, curr.stop))
        else:
            merged.append(curr)

    return merged


def parse_input(puzzle_input):
    pat = re.compile(r"x=(-?\d+), y=(-?\d+)")

    report = {}
    for line in puzzle_input.splitlines():
        sensor, beacon = [tuple(map(int, t)) for t in pat.findall(line)]
        report[sensor] = manhattan(sensor, beacon)

    return (report,)


def part_one(report, target=2_000_000):
    intervals = []
    for (x, y), d in report.items():
        diff = d - abs(y - target)
        if diff >= 0:
            intervals.append(range(x - diff, x + diff))

    return sum(map(len, merge_ranges(intervals)))


def part_two(report, boundary=4_000_000):
    # intercepts of lines with m=1 / m=-1
    ai, bi = set(), set()
    for (x, y), r in report.items():
        ai.add(y - x + r + 1)
        ai.add(y - x - r - 1)
        bi.add(y + x + r + 1)
        bi.add(y + x - r - 1)

    for a, b in itertools.product(ai, bi):
        x, y = (b - a) // 2, (a + b) // 2

        if x < 0 or x > boundary or y < 0 or y > boundary:
            continue

        if all(manhattan((x, y), k) > v for k, v in report.items()):
            return 4_000_000 * x + y

    raise RuntimeError("unreachable")


class Test:
    example = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

    def test_one(self):
        assert part_one(*parse_input(self.example), 10) == 26

    def test_two(self):
        assert part_two(*parse_input(self.example), 20) == 56000011


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
