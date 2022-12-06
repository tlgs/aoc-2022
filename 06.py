import collections
import sys


def parse_input(puzzle_input):
    return (puzzle_input,)


def part_one(datastream):
    queue = collections.deque(datastream[:4], maxlen=4)
    if len(set(queue)) == 4:
        return 4

    for i, c in enumerate(datastream[4:], start=5):
        queue.append(c)
        if len(set(queue)) == 4:
            return i

    raise RuntimeError("unreachable")


def part_two(datastream):
    queue = collections.deque(datastream[:14], maxlen=14)
    if len(set(queue)) == 14:
        return 14

    for i, c in enumerate(datastream[14:], start=15):
        queue.append(c)
        if len(set(queue)) == 14:
            return i

    raise RuntimeError("unreachable")


class Test:
    example1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    example2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    example3 = "nppdvjthqldpwncqszvftbrmjlhg"
    example4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    example5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 7
        assert part_one(*parse_input(self.example2)) == 5
        assert part_one(*parse_input(self.example3)) == 6
        assert part_one(*parse_input(self.example4)) == 10
        assert part_one(*parse_input(self.example5)) == 11

    def test_two(self):
        assert part_two(*parse_input(self.example1)) == 19
        assert part_two(*parse_input(self.example2)) == 23
        assert part_two(*parse_input(self.example3)) == 23
        assert part_two(*parse_input(self.example4)) == 29
        assert part_two(*parse_input(self.example5)) == 26


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
