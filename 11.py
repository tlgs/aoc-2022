import copy
import functools
import math
import sys
from typing import Callable, NamedTuple


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def square(x):
    return x * x


class Monkey(NamedTuple):
    items: list[int]
    fn: Callable[[int], int]
    divisor: int
    targets: tuple[int, int]


def parse_input(puzzle_input):
    raw_monkeys = puzzle_input.split("\n\n")

    monkeys = []
    for raw_monkey in raw_monkeys:
        lines = raw_monkey.splitlines()

        _, raw_items = lines[1].split(":")
        items = [int(x) for x in raw_items.split(",")]

        _, raw_operation = lines[2].split("old", maxsplit=1)
        match raw_operation.split():
            case "+", rv:
                fn = functools.partial(add, int(rv))
            case "*", "old":
                fn = square
            case "*", rv:
                fn = functools.partial(mult, int(rv))
            case _:
                raise NotImplementedError

        *_, raw_throw_divisor = lines[3].split()
        throw_divisor = int(raw_throw_divisor)

        *_, raw_throw_true = lines[4].split()
        throw_true = int(raw_throw_true)

        *_, raw_throw_false = lines[5].split()
        throw_false = int(raw_throw_false)

        m = Monkey(items, fn, throw_divisor, (throw_true, throw_false))
        monkeys.append(m)

    return (monkeys,)


def part_one(monkeys):
    monkeys = copy.deepcopy(monkeys)

    counts = [0] * len(monkeys)
    for _ in range(20):
        for i, m in enumerate(monkeys):
            counts[i] += len(m.items)
            for item in m.items:
                item = m.fn(item) // 3

                to = m.targets[item % m.divisor != 0]
                monkeys[to].items.append(item)

            m.items.clear()

    a, b, *_ = sorted(counts, reverse=True)
    return a * b


def part_two(monkeys):
    monkeys = copy.deepcopy(monkeys)

    clock = math.prod(m.divisor for m in monkeys)
    counts = [0] * len(monkeys)
    for _ in range(10_000):
        for i, m in enumerate(monkeys):
            counts[i] += len(m.items)
            for item in m.items:
                item = m.fn(item) % clock

                to = m.targets[item % m.divisor != 0]
                monkeys[to].items.append(item)

            m.items.clear()

    a, b, *_ = sorted(counts, reverse=True)
    return a * b


class Test:
    example = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 10605

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 2713310158


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    raise SystemExit(main())
