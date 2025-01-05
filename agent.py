import math
import random
import game
from othello import OthelloMove, OTHER_PLAYER, PLAYER1, PLAYER2, EMPTY

class RandomAgent(game.Player):
    def choose_move(self, state):
        moves = state.generateMoves()
        return random.choice(moves) if moves else None

class HumanPlayer(game.Player):
    def __init__(self):
        super().__init__()

    def choose_move(self, state):
        moves = state.generateMoves()
        for i, action in enumerate(moves):
            print('{}: {}'.format(i, action))
        response = input('Please choose a move: ')
        return moves[int(response)]

class MinimaxAgent(game.Player):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth

    def evaluate(self, state):
        """
        Improved evaluation function:
        Includes piece difference, mobility, and corner stability.
        """
        score = state.score()  # Difference in pieces
        mobility = len(state.generateMoves(PLAYER1)) - len(state.generateMoves(PLAYER2))
        corner_score = sum(1 for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]
                           if state.get(x, y) == PLAYER1) - \
                       sum(1 for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]
                           if state.get(x, y) == PLAYER2)
        return score + mobility + 5 * corner_score

    def minimax(self, state, depth, maximizing_player):
        if depth == 0 or state.game_over():
            return self.evaluate(state)

        if maximizing_player:
            max_eval = -math.inf
            for move in state.generateMoves():
                eval = self.minimax(state.applyMoveCloning(move), depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for move in state.generateMoves():
                eval = self.minimax(state.applyMoveCloning(move), depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def choose_move(self, state):
        moves = state.generateMoves()
        if not moves:
            print("MinimaxAgent has no legal moves. Passing turn...")
            return None

        best_score = -math.inf
        best_move = None
        for move in moves:
            score = self.minimax(state.applyMoveCloning(move), self.depth, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

class AlphaBeta(game.Player):
    def __init__(self, depth):
        super().__init__()
        self.depth = depth

    def evaluate(self, state):
        """
        Improved evaluation function (same as MinimaxAgent).
        """
        score = state.score()
        mobility = len(state.generateMoves(PLAYER1)) - len(state.generateMoves(PLAYER2))
        corner_score = sum(1 for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]
                           if state.get(x, y) == PLAYER1) - \
                       sum(1 for x, y in [(0, 0), (0, 7), (7, 0), (7, 7)]
                           if state.get(x, y) == PLAYER2)
        return score + mobility + 5 * corner_score

    def alphabeta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or state.game_over():
            return self.evaluate(state)

        if maximizing_player:
            max_eval = -math.inf
            for move in state.generateMoves():
                eval = self.alphabeta(state.applyMoveCloning(move), depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in state.generateMoves():
                eval = self.alphabeta(state.applyMoveCloning(move), depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def choose_move(self, state):
        moves = state.generateMoves()
        if not moves:
            print("AlphaBeta agent has no legal moves. Passing turn...")
            return None

        best_score = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf
        for move in moves:
            score = self.alphabeta(state.applyMoveCloning(move), self.depth, alpha, beta, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
