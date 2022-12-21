import sys
from collections import deque


def parse_input(puzzle_input):
    return (puzzle_input.rstrip(),)


def part_one(datastream):
    queue = deque(maxlen=4)
    for i, c in enumerate(datastream):
        queue.append(c)
        if len(set(queue)) == 4:
            return i + 1

    raise RuntimeError("unreachable")


def part_two(datastream):
    queue = deque(maxlen=14)
    for i, c in enumerate(datastream):
        queue.append(c)
        if len(set(queue)) == 14:
            return i + 1

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
    sys.exit(main())
