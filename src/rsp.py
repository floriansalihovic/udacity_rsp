import random


NAME_ROCK = 'rock'
NAME_SCISSORS = 'scissors'
NAME_PAPER = 'paper'


class Game:
    """
    A Game lets players compete in rounds. Each player can play a move per
    round. A move is represented by one of the values: 'ROCK', 'SCISSOR' or
    'PAPER'. The game uses rules, to define which move beats another. It
    records all rounds so a winner can be chosen, depending on the numbers
    of rounds won.
    """

    def __init__(self):
        pass


class Rules:
    rules = {
        NAME_ROCK: NAME_SCISSORS,
        NAME_SCISSORS: NAME_PAPER,
        NAME_PAPER: NAME_ROCK
    }

    """
    Rules define which move beats another.
    """

    def __init__(self):
        pass

    def compare(self, move_1, move_2):
        """
        Simple comparison of two values. If the first value is a key, which
        reference the value which equals move_2, the player making move_1
        wins.
        If the second value is the key, which
        :param move_1: A move done by the first player of a game.
        :type move_1: basestring
        :param move_2: A move done by the second player of a game.
        :type move_2: basestring
        :returns: an integer value in the set of {-1, 0, 1}, as every
        comparator does.
        :rtype: int
        """
        # https://docs.python.org/3.6/reference/simple_stmts.html#the-assert-statement
        assert move_1 in self.rules, "move_1 is not a valid value"
        assert move_2 in self.rules, "move_2 is not a valid value"

        if self.rules[move_1] == move_2:
            return -1
        elif self.rules[move_2] == move_1:
            return 1
        else:
            return 0


class Round:
    """
    A round is the exchange of moves of two players. It can be won by a
    player or end in a draw, if both players chose to play the same move.
    """

    def __init__(self):
        pass


class Player:
    """
    A player can play one move per round.
    """

    def __init__(self):
        pass

    def play(self):
        """
        Providing a value which is evaluated in a game to determine a winner.
        :return: A value from the set of {'rock', 'scissors', 'paper'}.
        :rtype: basestring
        """
        # https://docs.python.org/2/library/exceptions.html#exceptions.NotImplementedError
        raise NotImplementedError('implement this method in '
                                  'an appropriate base class')


class StaticMovePlayer(Player):
    """
    StaticMovePlayer instance will always return the same value, which is
    passed to the instance when created.
    """

    def __init__(self, value=NAME_ROCK):
        super().__init__()
        self.value = value

    def play(self):
        return self.value


class RandomMovePlayer(Player):
    """
    RandomMovePlayer instances randomly which choose the next move to play.
    """

    def __init__(self):
        super().__init__()

    def play(self):
        return random.choice([NAME_ROCK, NAME_SCISSORS, NAME_ROCK])


if __name__ == '__main__':
    print("let's play a game")
    assert NAME_ROCK is StaticMovePlayer().play()
