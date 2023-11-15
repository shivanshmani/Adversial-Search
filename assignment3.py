def actions(board):
    # Returns a list of available actions (empty blocks) for the current state of the board
    return [i for i, block in enumerate(board) if block == '0']

def result(board, action, player):
    # Returns the resulting board after the action is taken by the player
    new_board = list(board)
    new_board[action] = 'B' if player == 'MAX' else 'W'
    # Implement flipping the adjacent coins if needed based on the game rules
    # Hint: Use the rules provided to update the board state after the move
    return new_board

def terminal_test(board):
    # Checks if the game has reached a terminal state (no empty blocks)
    return '0' not in board

def utility(board):
    # Computes the utility value for Player 1 (number of black coins)
    # and Player 2 (number of white coins) in the terminal state
    black_coins = board.count('B')
    white_coins = board.count('W')
    return black_coins, white_coins

def minimax(board, depth, maximizing_player):
    if depth == 0 or terminal_test(board):
        return utility(board)

    if maximizing_player:
        max_value = float('-inf')
        for action in actions(board):
            new_board = result(board, action, 'MAX')  # 'MAX' represents Player 1
            value = minimax(new_board, depth - 1, False)
            max_value = max(max_value, value[0]) if isinstance(value, tuple) else max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for action in actions(board):
            new_board = result(board, action, 'MIN')  # 'MIN' represents Player 2
            value = minimax(new_board, depth - 1, True)
            min_value = min(min_value, value[1]) if isinstance(value, tuple) else min(min_value, value)
        return min_value

# Example input
input_board = "0000W00BBW0"
# Run minimax algorithm
result_utility = minimax(input_board, depth=3, maximizing_player=True)  # Adjust depth as needed

print("Utility of Player 1 (MAX player):", result_utility)  # Print the utility for Player 1
