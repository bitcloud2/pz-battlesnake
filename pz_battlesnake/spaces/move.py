from typing import List
from gymnasium.spaces import Discrete
import random


class Move(Discrete):
    """
    This class represents the move action in BattleSnake, which is documented under response property of the /move endpoint. Refer to the battlesnake docs: https://docs.battlesnake.com/references/api#post-move

    There's 4 possible moves:
        - "up"
        - "down"
        - "left"
        - "right"
    """

    #possible_moves: List[str] = ["up", "down", "left", "right"]
    possible_moves: List[int] = [0,1,2,3]
    def __init__(self):
        self.moves: List[int] = self.possible_moves
        super().__init__(len(self.moves))

    def sample(self) -> int:
        """
        Returns a random move from the list of possible moves.

        Returns:
            int: representing the move

        Example:
            >>> move = Move()
            >>> move.sample()
            "up"
        """
        return super().sample()

    def contains(self, x) -> bool:
        """
        Check if the input is one of the 4 possible moves.


        Returns:
            bool: True if the input is one of the 4 possible moves, otherwise False.
        """
        return super().contains(x)

    def __repr__(self) -> str:
        """Gives a string representation of this space."""
        return "Move()"

    def __eq__(self, other) -> bool:
        return isinstance(other, Move)
