import functools
import json
import sys


def compare(left, right):
    match left, right:
        case int(), int():
            return left - right

        case list(), list():
            for a, b in zip(left, right):
                if result := compare(a, b):
                    return result

            return len(left) - len(right)

        case int(), list():
            return compare([left], right)

        case list(), int():
            return compare(left, [right])

        case _:
            raise ValueError


def parse_input(puzzle_input):
    result = []
    for raw_pair in puzzle_input.split("\n\n"):
        packets = []
        for raw_packet in raw_pair.splitlines():
            packet = json.loads(raw_packet)
            packets.append(packet)

        result.append(tuple(packets))

    return (result,)


def part_one(pairs):
    total = 0
    for i, (a, b) in enumerate(pairs, start=1):
        if compare(a, b) < 0:
            total += i

    return total


def part_two(pairs):
    packets = [[[2]], [[6]]]
    for a, b in pairs:
        packets.append(a)
        packets.append(b)

    packets.sort(key=functools.cmp_to_key(compare))

    key_a = packets.index([[2]]) + 1
    key_b = packets.index([[6]]) + 1

    return key_a * key_b


class Test:
    example = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 13

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 140


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
