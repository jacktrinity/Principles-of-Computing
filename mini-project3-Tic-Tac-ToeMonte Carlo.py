"""
Week 3 Mini-Project of Principles of Computing

CodeSkulptor: http://www.codeskulptor.org/#user48_pzsvfxI60XecfW5.py
Written in Python 2
"""

# Monte Carlo Tic-Tac-Toe Player

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. The function should play a 
    game starting with the given player by making random moves, alternating between players. 
    The function should return when the game is over. The modified board will contain the state of the game, 
    so the function does not return anything. In other words, the function should modify the board input.
    """
    # Check if the game is still in progress.
    if board.check_win() != None:
        # If PLAYERX wins, returns PLAYERX.
        # If PLAYERO wins, returns PLAYERO.
        # If game is drawn, returns DRAW.
        # If game is in progress, returns None.
        return
    
    # Return a list of (row, col) tuples for all empty squares
    empty_squares = board.get_empty_squares()
    
    # Pick a random available square 
    square = empty_squares[random.randrange(len(empty_squares))]
    board.move(square[0], square[1], player)
    
    mc_trial(board, provided.switch_player(player))
    
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe 
    board, a board from a completed game, and which player the machine player is. The function should 
    score the completed board and update the scores grid. As the function updates the scores grid 
    directly, it does not return anything,
    """
    winner = board.check_win()
    current_player_win = winner == player
    
    # Check for Draw, no points
    if winner == provided.DRAW:
        return
    
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            position = board.square(row, col)
            current_player_pos = position == player
            
            # Square is empty, continue.
            if position == provided.EMPTY:
                continue

            # Calculate the score
            if current_player_win and current_player_pos:
                scores[row][col] += SCORE_CURRENT
            elif current_player_win and not current_player_pos:
                scores[row][col] -= SCORE_OTHER
            elif not current_player_win and current_player_pos:
                scores[row][col] -= SCORE_CURRENT
            else:
                scores[row][col] += SCORE_OTHER

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function should find all of the 
    empty squares with the maximum score and randomly return one of them as a (row, column) tuple. 
    
    It is an error to call this function with a board that has no empty squares 
    (there is no possible next move), so your function may do whatever it wants in that case. 
    """
    empty_squares = board.get_empty_squares()
    
    # Check if the board if full. No empty square.
    if len(empty_squares) == 0:
        return
    
    best_move = None
    best_score = None
    
    # Get the best move, provided by the best score available.
    for square in empty_squares:
        if best_move == None or (scores[square[0]][square[1]] > best_score):
            best_move = square
            best_score = scores[square[0]][square[1]]
            
    return best_move

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials 
    to run. The function should use the Monte Carlo simulation described above to return a move for 
    the machine player in the form of a (row, column) tuple.
    """
    scores = []
    for dummy_i in range(board.get_dim()):
        row = []
        for dummy_j in range(board.get_dim()):
            row.append(0)
        scores.append(row)
    
    for dummy_num in range(trials):
        board_clone = board.clone()
        mc_trial(board_clone, player)
        mc_update_scores(scores, board_clone, player)
        
    return get_best_move(board, scores)

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
