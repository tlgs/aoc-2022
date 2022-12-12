import collections
import sys


def neighbors(x, y):
    yield x, y - 1
    yield x + 1, y
    yield x, y + 1
    yield x - 1, y


def parse_input(puzzle_input):
    start, end = None, None
    heightmap = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case "S":
                    start = (x, y)
                    heightmap[x, y] = 0
                case "E":
                    end = (x, y)
                    heightmap[x, y] = 25
                case v:
                    heightmap[x, y] = ord(v) - 97

    assert (start is not None) and (end is not None)
    return (heightmap, start, end)


def part_one(heightmap, start, end):
    q = collections.deque([(end, 0)])
    seen = {end}
    while q:
        position, steps = q.popleft()
        if position == start:
            return steps

        for neighbor in neighbors(*position):
            if neighbor in seen or neighbor not in heightmap:
                continue

            if heightmap[neighbor] >= heightmap[position] - 1:
                q.append((neighbor, steps + 1))
                seen.add(neighbor)

    raise RuntimeError("unreachable")


def part_two(heightmap, _, end):
    q = collections.deque([(end, 0)])
    seen = {end}
    while q:
        position, steps = q.popleft()
        if heightmap[position] == 0:
            return steps

        for neighbor in neighbors(*position):
            if neighbor in seen or neighbor not in heightmap:
                continue

            if heightmap[neighbor] >= heightmap[position] - 1:
                q.append((neighbor, steps + 1))
                seen.add(neighbor)

    raise RuntimeError("unreachable")


class Test:
    example = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 31

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 29


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
