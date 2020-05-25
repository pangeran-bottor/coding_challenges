def solve(board):
    result = []
    for row in board:
        row = row.replace("2", "1")
        result.append(row)
    return result
    
t = int(input())
for _ in range(t):
    board = []
    for _ in range(9):
        board.append(input())
    result = solve(board)
    for row in result:
        print(row)