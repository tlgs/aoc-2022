import collections
import itertools
import sys


def parse_input(puzzle_input):
    rates = {}
    connections = {}
    for line in puzzle_input.splitlines():
        parts = line.split(maxsplit=9)
        valve = parts[1]

        rate = int(parts[4][5:-1])
        if rate > 0 or valve == "AA":
            rates[valve] = rate

        connections[valve] = tuple(parts[-1].split(", "))

    # build a distance matrix for the interesting locations, i.e. rate > 0
    distances = {}
    for start, end in itertools.combinations(rates.keys(), 2):
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

    # assuming AA starts out being open, with a flow rate of 0;
    # this doesn't match the problem description but changes nothing
    # for the example and actual puzzle input
    q = collections.deque([(0, 30, ("AA",))])
    while q:
        pressure, left, opened = q.popleft()
        best = max(pressure, best)

        curr = opened[-1]
        options = rates.keys() - set(opened)
        for valve in options:
            next_left = left - distances[curr, valve] - 1
            if next_left < 1:
                continue

            next_pressure = pressure + rates[valve] * next_left
            q.append((next_pressure, next_left, (*opened, valve)))

    return best


def part_two(distances, rates):
    best = 0

    # assuming AA starts out being open, with a flow rate of 0;
    # this doesn't match the problem description but changes nothing
    # for the example and actual puzzle input
    q = collections.deque([(0, (26, 26), ("AA", "AA"))])
    while q:
        pressure, (left_a, left_b), opened = q.popleft()
        best = max(pressure, best)

        *_, curr_a, curr_b = opened
        options = rates.keys() - set(opened)
        for valve_a, valve_b in itertools.permutations(options, 2):
            next_left_a = left_a - distances[curr_a, valve_a] - 1
            if next_left_a < 1:
                continue

            next_left_b = left_b - distances[curr_b, valve_b] - 1
            if next_left_b < 1:
                continue

            next_pressure = (
                pressure + rates[valve_a] * next_left_a + rates[valve_b] * next_left_b
            )
            q.append(
                (next_pressure, (next_left_a, next_left_b), (*opened, valve_a, valve_b))
            )

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
