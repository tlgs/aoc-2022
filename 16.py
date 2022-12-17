import collections
import itertools
import sys


def parse_input(puzzle_input):
    rates = {}
    connections = {}
    for line in puzzle_input.splitlines():
        parts = line.split(maxsplit=9)
        valve = parts[1]

        rates[valve] = int(parts[4][5:-1])
        connections[valve] = tuple(parts[-1].split(", "))

    assert rates["AA"] == 0

    # build a distance matrix for the interesting locations, i.e. rate > 0
    rates = {k: v for k, v in rates.items() if v}
    distances = {}
    for start, end in itertools.combinations(rates.keys() | {"AA"}, 2):
        seen = {start}
        q = collections.deque([(0, start)])
        while q:
            steps, curr = q.popleft()
            if curr == end:
                distances[start, end] = steps
                distances[end, start] = steps
                break

            for valve in connections[curr]:
                if valve not in seen:
                    q.append((steps + 1, valve))
                    seen.add(valve)

    return (distances, rates)


def part_one(distances, rates):
    best = 0
    q = collections.deque([(0, 30, "AA", set())])
    while q:
        pressure, left, curr, visited = q.popleft()
        best = max(pressure, best)

        for valve in rates.keys() - visited:
            next_left = left - distances[curr, valve] - 1
            if next_left < 1:
                continue

            next_pressure = pressure + rates[valve] * next_left

            t = (next_pressure, next_left, valve, visited | {valve})
            q.append(t)

    return best


def part_two(distances, rates):
    paths = []
    q = collections.deque([(0, 26, "AA", set())])
    while q:
        pressure, left, curr, visited = q.popleft()
        paths.append((pressure, visited))

        for valve in rates.keys() - visited:
            next_left = left - distances[curr, valve] - 1
            if next_left < 1:
                continue

            next_pressure = pressure + rates[valve] * next_left

            t = (next_pressure, next_left, valve, visited | {valve})
            q.append(t)

    paths.sort(reverse=True)

    best = 0
    for i, (pa, va) in enumerate(paths, start=1):
        if pa * 2 <= best:
            break

        for pb, vb in paths[i:]:
            if pa + pb <= best:
                break

            if not va & vb:
                best = max(best, pa + pb)
                break

    return best


class Test:
    example = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 1651

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 1707


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
