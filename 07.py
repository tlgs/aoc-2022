import sys
from collections import defaultdict
from itertools import accumulate


def parse_input(puzzle_input):
    pwd = ["/"]
    sizes = defaultdict(int)
    for line in puzzle_input.splitlines():
        match line.split():
            case ("$", "cd", "/"):
                pwd = ["/"]
            case ("$", "cd", ".."):
                pwd.pop()
            case ("$", "cd", x):
                pwd.append(f"{x}/")
            case ("$", "ls"):
                ...
            case ("dir", _):
                ...
            case (x, _):
                for path in accumulate(pwd):
                    sizes[path] += int(x)
            case _:
                raise ValueError("unknown terminal output")

    return (sizes,)


def part_one(sizes):
    return sum(v for _, v in sizes.items() if v <= 100_000)


def part_two(sizes):
    used = sizes["/"]
    return min(v for _, v in sizes.items() if v >= used - 40_000_000)


class Test:
    example = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 95437

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 24933642


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
