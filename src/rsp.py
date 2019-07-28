import random

NAME_ROCK = 'rock'
NAME_SCISSORS = 'scissors'
NAME_PAPER = 'paper'
ALL_VALID_VALUES = [NAME_ROCK, NAME_SCISSORS, NAME_PAPER]


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
    player_data = {}
    player_1 = None
    player_2 = None
    rules = Rules()

    def __init__(self, round_id, player_1, player_2):
        """
        Not only inits the fields, but also determines the winner and
        saves required data for later analysis.
        :param round_id: The id of the current round.
        :type round_id: int
        :param player_1: The first player.
        :type player_1: Player
        :param player_2: The second player.
        :type player_2: Player
        """
        self.id = round_id
        self.player_1 = player_1
        self.player_2 = player_2

        self.set_player_data(self.player_1)
        self.set_player_data(self.player_2)

        result = self.rules.compare(
            self.player_data[player_1.player_id]['move'],
            self.player_data[player_2.player_id]['move'])

        player_1.learn(self.player_data[player_2.player_id]['move'])
        player_2.learn(self.player_data[player_1.player_id]['move'])

        if result == -1:
            self.winner = self.player_1
        elif result == 0:
            self.winner = None
        else:
            self.winner = self.player_2

    def set_player_data(self, player):
        """
        Set the required player data.
        :param player: A Player instance.
        :type player: Player
        """
        self.player_data[player.player_id] = {
            'move': player.play()
        }
        player.played_round(self)

    def get_opponent(self, player):
        """
        Returns the opponent of a player.
        :param player: A player instance.
        :return: Player 1, if the given player is player 2, player 1 else.
        """
        return self.player_1 if player is self.player_2 else self.player_1


class Player:
    rounds_played = []

    """
    A player can play one move per round.
    """

    def __init__(self, player_id):
        self.player_id = player_id

    def learn(self, value):
        """
        Interface method which could be implemented optionally by subclasses.
        :parameter value: The last played value by the opponent.
        :type value: basestring
        """
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

    def played_round(self, round):
        self.rounds_played.append(round)


class StaticMovePlayer(Player):
    """
    StaticMovePlayer instance will always return the same value, which is
    passed to the instance when created.
    """

    def __init__(self, player_id, value=NAME_ROCK):
        super().__init__(player_id)
        self.value = value

    def play(self):
        return self.value


class RandomMovePlayer(Player):
    """
    RandomMovePlayer instances randomly which choose the next move to play.
    """

    def play(self):
        return random.choice(ALL_VALID_VALUES)


class ImitatingPlayer(Player):
    """
    ImitatingPlayer starts with a random move and will subsequently continue
    returning its opponent's last round's move.
    """

    def __init__(self, player_id):
        super().__init__(player_id)
        self.value = random.choice(ALL_VALID_VALUES)

    def learn(self, value):
        """
        Sets the next value to play.
        :param value: The next value to play.
        """
        assert value in ALL_VALID_VALUES
        self.value = value

    def play(self):
        return self.value


class CyclingMovePlayer(Player):
    """
    Copy of all moves, as this Player subclass mutates the list.
    """
    moves = ALL_VALID_VALUES.copy()

    def play(self):
        return self.next_move()

    def next_move(self):
        """
        Cycles through the list of possible moves.
        :return:
        """
        self.moves.append(self.moves.pop(0))
        return self.moves[0]


class HumanPlayer(Player):
    pass


if __name__ == '__main__':
    print("let's play a game")
    assert NAME_ROCK is StaticMovePlayer(1).play()
    cycling_player = CyclingMovePlayer(2)
    print(cycling_player.play())
    print(cycling_player.play())
    print(cycling_player.play())
    print(cycling_player.play())
