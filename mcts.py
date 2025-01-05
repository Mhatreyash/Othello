import math
import random
import game
from othello import OthelloMove

class mcts(game.Player):
    def __init__(self, iterations):
        super().__init__()
        self.iterations = iterations

    def choose_move(self, state):
        class Node:
            def __init__(self, state, move=None, parent=None):
                self.state = state
                self.move = move
                self.parent = parent
                self.visits = 0
                self.value = 0
                self.children = []

            def expand(self):
                moves = self.state.generateMoves()
                self.children = [Node(self.state.applyMoveCloning(move), move, self) for move in moves]

            def is_fully_expanded(self):
                return len(self.children) == len(self.state.generateMoves())

            def best_child(self, exploration_weight=1.0):
                return max(
                    self.children,
                    key=lambda child: child.value / (child.visits + 1e-6) +
                                      exploration_weight * math.sqrt(math.log(max(1, self.visits)) / max(1, child.visits))
                )

        def simulate(state):
            while not state.game_over():
                moves = state.generateMoves()
                if not moves:
                    break
                state = state.applyMoveCloning(random.choice(moves))
            return state.score()

        def backpropagate(node, reward):
            while node is not None:
                node.visits += 1
                node.value += reward
                reward = -reward  # Switch perspective for the opponent
                node = node.parent

        root = Node(state)
        root.expand()

        for _ in range(self.iterations):
            node = root
            while node.is_fully_expanded() and node.children:
                node = node.best_child()

            if not node.is_fully_expanded() and not node.state.game_over():
                node.expand()
                node = random.choice(node.children)

            reward = simulate(node.state)
            backpropagate(node, reward)

        if root.children:
            return root.best_child(exploration_weight=0).move
        return None
