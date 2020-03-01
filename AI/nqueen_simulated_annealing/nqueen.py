import math
import random

def get_random_board(n):
    board = []
    for i in range(0,n):
        board.append(random.randint(0,n-1))
    return board

def count_conflicts(board):
    n = len(board)
    row_conflicts = 0
    diag_conflicts = 0
    inv_diag_conflicts = 0

    row_freq = [0 for x in range(0,n)]
    diag_freq = [0 for x in range(0,n*2)]
    inv_diag_freq = [0 for x in range(0,n*2)]

    for i in range(0, n):
        c=i
        r=board[i]
        #counting row conflicts
        row_freq[board[i]] += 1
        row_conflicts += (row_freq[board[i]] - 1)
        #counting diagonal conflicts
        diag_num = c-r+n
        diag_freq[diag_num] += 1
        diag_conflicts += (diag_freq[diag_num] - 1)
        #counting inv. diagonal conflicts
        inv_diag_num = c+r
        inv_diag_freq[inv_diag_num] += 1
        inv_diag_conflicts += (inv_diag_freq[inv_diag_num] - 1)

    total_conflicts =inv_diag_conflicts+row_conflicts+diag_conflicts
    return total_conflicts


def get_next_random_step(board):
    next_board = list(board)
    c = random.randint(0,len(board)-1)
    r = random.randint(0,len(board)-1)
    next_board[c] = r;
    conflicts = count_conflicts(next_board)
    return  next_board,conflicts



def get_better_board(board):
    better_board = board
    least_conflicts = count_conflicts(board)
    for c in range(0, len(board)):
        current_row = board[c]
        for r in range(0, len(board)):
            board[c] = r
            new_conflicts = count_conflicts(board)
            if new_conflicts < least_conflicts:
                least_conflicts = new_conflicts
                better_board = list(board)
                return better_board,least_conflicts
            #print("Col: ", c, "Row: ", r, "Conflicts: ", new_conflicts)
        board[c] = current_row
        #print('\n')
    #print(better_board, least_conflicts)
    return better_board,least_conflicts



def probability(E1,E2,T):
    k = E1 - E2
    div = min(1,k/T)
    val = math.exp(div)
    rnd = random.uniform(0,1)
    if rnd < val:
        #print("True ")
        return True
    else:
        #print("False ")
        return False



print("Enter The Number of Queen : ")
n = eval(input(""))
print("Enter Initial Temperatue : ")
T = eval(input(""))
print("Enter The Cooling Rate : ")
cooling_rate = eval(input(""))

board = get_random_board(n)
best_board = list(board)
E1 = count_conflicts(best_board)
print("Initial board: ", board, " Conflicts: ", E1)


while E1>0 and T>=1:
    next_board, E2 = get_next_random_step(best_board)
    #print("Next board:", next_board, " Conflicts: ", E2)
    if E2 <= E1:
        E1 = E2
        best_board = list(next_board)
    elif probability(E1,E2,T):
        E1 = E2
        best_board = list(next_board)
    else:
        best_board,E1 = get_better_board(best_board)
    T-=cooling_rate

    #printing progress 
    print(T)
    print("Best board:", best_board, " Conflicts: ", E1)




if E1==0:
    print("\nSolution Found with 0 conflict")
else:
    print("\nsolution Not Found ",E1," conflict(s)")


print("Best board: ", best_board)
