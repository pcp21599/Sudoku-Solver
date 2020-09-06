# find an empty place to fill
# make validity cehcker
# printing the soduko
# Make a solved sudoku borad and reomve multiple elements from it to make a random sudoku board

board=[ [7, 8, 0, 4, 0, 0, 1, 2, 0], 
        [6, 0, 0, 0, 7, 5, 0, 0, 9], 
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0], 
        [0, 0, 1, 0, 5, 0, 9, 3, 0], 
        [9, 0, 4, 0, 6, 0, 0, 0, 5], 
        [0, 7, 0, 3, 0, 0, 0, 1, 2], 
        [1, 2, 0, 0, 0, 7, 4, 0, 0], 
        [0, 4, 9, 2, 0, 6, 0, 0, 7] ]


def print_board(board):
    # printing the soduko
    for i in range(len(board)):
        if i % 3 == 0 and i!= 0:
            print("--------------------------",end='\n')
        for j in range(len(board[0])):
            if j % 3 == 0 and j!=0:
                print(" | ",end=" ")
            if j == 8:
                print(board[i][j],end="\n")
                continue
        
            print(board[i][j],end=" ")
    print("\n")

def validity_checker(board,num,place):
    # Horizontal Check
    row,col = place
    for c in range(len(board[0])):
         if board[row][c]==num and c != col:
                return False 
    # Vertical Check
    for r in range(len(board[0])):
            if board[r][col]==num and r !=row:
                return False   

    # Block Check
    b_x = col // 3
    b_y = row // 3

    for r in range( b_y*3, (b_y*3) + 3 ):
        for c in range(b_x*3, (b_x*3) + 3 ):
            if (board[r][c] == num) & ((r,c) != (row,col)):
                return False   
    
    return True

def empty_check(board):
    # Checking for empty spaces
    for r_index,row in enumerate(board):
        for c_index , col in enumerate(row):
            if col == 0 :
                return (r_index,c_index)
    return None

def solve(board):
    print("Solving in process")
    place = empty_check(board)
    if not place:
        print("Sudoku Solved",end="\n")
        return True
    else:
        row,col = empty_check(board)
    for i in range(1,10):
            if validity_checker(board,i,(row,col)):
                board[row][col] = i
                if solve(board):
                    return True
                board[row][col]=0
    return False

print_board(board)
solve(board)
print_board(board)