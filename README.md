# Othello AI Project

This project is an implementation of the game Othello (also known as Reversi) with several AI agents, including human interaction. It features different strategies for choosing moves, such as Random, Minimax, Alpha-Beta Pruning, and Monte Carlo Tree Search (MCTS).

## Features
- **Human vs AI**: Play as a human against any AI agent.
- **AI vs AI**: Watch two AI agents compete against each other.
- **Custom AI Depth**: Adjust the depth or iterations for AI computations.
- **Multiple AI Agents**:
  - **RandomAgent**: Makes random moves.
  - **MinimaxAgent**: Implements the Minimax algorithm with a heuristic evaluation.
  - **AlphaBetaAgent**: Extends Minimax with Alpha-Beta pruning for efficiency.
  - **MCTSAgent**: Uses Monte Carlo Tree Search for decision-making.

## Files
- **`agent.py`**: Contains implementations of the AI agents and the human player.
- **`game.py`**: Manages the game loop and interactions between players and the game state.
- **`main.py`**: Entry point for running the game.
- **`mcts.py`**: Implements the Monte Carlo Tree Search agent.
- **`othello.py`**: Contains the game logic, including the board representation and valid move generation.

## How to Run
### Prerequisites
- Python 3.8 or above.

### Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Run the game with specified agents:
   ```bash
   python main.py <player1> <player2> [depth_or_iterations]
   ```
   - `<player1>` and `<player2>` can be one of: `human`, `random`, `minimax`, `alphabeta`, or `mcts`.
   - `[depth_or_iterations]` is optional and specifies the depth for `minimax` and `alphabeta`, or iterations for `mcts`.

### Examples
- Human vs RandomAgent:
  ```bash
  python main.py human random
  ```
- Minimax vs AlphaBeta with depth 4:
  ```bash
  python main.py minimax alphabeta 4
  ```

## Gameplay
- The game starts with the standard Othello board setup.
- Players alternate turns, flipping opponent pieces by placing their own in valid positions.
- The game ends when no valid moves remain for either player.

## AI Descriptions
- **RandomAgent**: Picks a move randomly from the list of valid moves.
- **MinimaxAgent**: Uses the Minimax algorithm with a heuristic that evaluates board control and mobility.
- **AlphaBetaAgent**: Optimized Minimax algorithm that prunes unnecessary branches.
- **MCTSAgent**: Uses simulations to estimate the best move, balancing exploration and exploitation.

## Customization
You can create custom agents by extending the `game.Player` class and implementing the `choose_move` method.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
