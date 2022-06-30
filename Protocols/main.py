"""
Protocols are the essence of how duck typing works:
when two classes have the same batch of methods,
they both adhere to a common protocol.

Any time we see classes with similar methods,
there's a common protocol; this may be formalized
with a type hint.
"""


from dataclasses import dataclass
from enum import Enum
from typing import Any
from typing import Protocol


class Direction(Enum):
    N = "n"
    E = "e"
    S = "s"
    W = "w"


@dataclass
class Movement:
    obj: Any
    distance_meters: int
    direction: Direction


class Runner(Protocol):
    def run(self, actions_spent: int, direction: Direction) -> Movement:
        """A Runner can run"""


class Waiter(Protocol):
    def wait(self, actions_spent: int, direction: Direction) -> Movement:
        """A Waiter can wait"""


class BaseHero:
    @property
    def max_speed(self) -> int:
        return 1

    def wait(self, actions_spent: int, direction: Direction) -> Movement:
        return Movement(obj=self, distance_meters=0, direction=direction)


class RunningHero(BaseHero):
    @property
    def run_speed(self) -> int:
        return self.max_speed * 2

    def run(self, actions_spent: int, direction: Direction) -> Movement:
        return Movement(
            obj=self,
            distance_meters=self.run_speed * actions_spent,
            direction=direction,
        )


class Board:
    def make_wait(
        self, obj: Waiter, direction: Direction, actions_spent: int
    ) -> Movement:
        return obj.wait(actions_spent, direction)

    def make_run(
        self, obj: Runner, direction: Direction, actions_spent: int
    ) -> Movement:
        return obj.run(actions_spent, direction)


def main() -> None:
    board = Board()
    waiter_move = board.make_wait(BaseHero(), Direction.N, 2)
    runner_move = board.make_run(RunningHero(), Direction.W, 3)
    runner_move2 = board.make_wait(RunningHero(), Direction.W, 3)
    heroes = (
        ("Hero", "Total spaces moved (M)"),
        ("a waiting hero", waiter_move.distance_meters),
        ("a running hero", runner_move.distance_meters),
        ("a running hero 2", runner_move2.distance_meters),
    )
    print("\n")
    for description, movement in heroes:
        print("\t{:<22} {:>25}".format(description, movement))


if __name__ == "__main__":
    main()
