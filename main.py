import chess
import random
board = chess.Board()
print(board)
print(list(board.legal_moves))

def random_playout(board :chess.Board, max_tot_moves= 300):
    board = board.copy()
    for i in range(max_tot_moves):
        if board.is_game_over():
            break
        move = random.choice(list(board.legal_moves))
        #print(move)
        board.push(move)
    return board.result()

def main():

    board = chess.Board()
    results = {}

    for move in board.legal_moves:
        board.push(move)
        res = random_playout(board, 1000)
        results[move.uci] = res
        board.pop()
    
    for move, res in results.items():
        print(f'move: {move}, Results: {res}')

        



if __name__=="__main__":
    main()