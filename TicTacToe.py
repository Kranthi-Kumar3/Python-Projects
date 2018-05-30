def create_board() :
    print("\n     |---------------------------------------|")
    for i in range(1,9,3):
        print(f"     |    {i}\t||\t{i+1}\t||\t{i+2}    |")
        print("     |---------------------------------------|")

def display_board(board) :
    print("\n     |---------------------------------------|")
    for i in range(0,8,3):
        print(f"     |    {board[i]}\t||\t{board[i+1]}\t||\t{board[i+2]}    |")
        print("     |---------------------------------------|")

def check_rows(board,pos) :
     if pos in (0,3,6) :
         return board[pos] == board[pos+1] == board[pos+2]
     elif pos in (1,4,7) :
         return board[pos-1] == board[pos] == board[pos+1]
     else:
         return board[pos] == board[pos-1] == board[pos-2]
     
def check_cols(board,pos) :
     if pos in (0,1,2) :
         return board[pos] == board[pos+3] == board[pos+6]
     elif pos in (3,4,5) :
         return board[pos-3] == board[pos] == board[pos+3]
     else:
         return board[pos] == board[pos-3] == board[pos-6]
     
def check_diag(board,pos) :
     if pos == 0 :
         return board[pos] == board[pos+4] == board[pos+8]
     elif pos == 2:
         return board[pos] == board[pos+2] == board[pos+4]
     elif pos == 6:
         return board[pos] == board[pos-2] == board[pos-4]
     elif pos == 8:
         return board[pos] == board[pos-4] == board[pos-8]
     elif pos == 4:
         return (board[pos] == board[pos-2] == board[pos+2]) or (board[pos] == board[pos-4] == board[pos+4]) 


     
def replay() :
    play = ""
    while play != '1' and play != '0' :
        play = input("Wanna Play Again(1(Yes)/0(No)) : ")
        if play == '0' :
            return False
        elif play == '1' :
            return True
        else :
            print("\nINVALID CHOICE")
                    


#main program
loop = True    
while loop : 
    print("\n\n\t\tWelcome to Tic Tac Toe Game")
    print("\t\t---------------------------\n")
    p1_sym = ""  

    #Assign Player Symbols      
    while p1_sym.upper() !='X' and p1_sym.upper() !='O' :
        print("\nPlayer 1:")
        print("--------")
        p1_sym = input("Choose Symbol('X' or 'O') : ").upper()
        if p1_sym == 'X' :
            p2_sym = 'O'
        elif p1_sym == 'O' :
            p2_sym = 'X'
        else :
            print("\n----Invalid Choice----")
            print("Select Again :)")
          
    print(f"\nPlayer 1 Symbol : {p1_sym}")
    print(f"Player 2 Symbol : {p2_sym}")
    
    create_board()
    
    p1_moves = p2_moves = 0
    board = [" "]*9
    valid = 1
    
    #play game
    while p1_moves < 5 :
        if valid == 1 :         #check for player2 invalid choice
            pos = -1
            while pos == -1 :
                print("\nPlayer 1:")
                print("--------")
                try :
                    pos = int(input("Select Position(1-9) : "))-1
                except ValueError :
                    print('Entered Non-numeric data.')
                    pos = -1
                    
            if pos in range(0,9) and board[pos] == " " :
                board[pos] = p1_sym
                p1_moves += 1
                display_board(board)
                if p1_moves > 2 and (check_rows(board,pos) or check_cols(board,pos) or check_diag(board,pos)) :
                    print(f"Player 1 Won with {p1_moves} Moves")
                    valid = 0           
                    break
            else :
                print("Invalid Choice")
                continue
        
        if p1_moves < 5 :
            pos = -1
            while pos == -1 :
                print("\nPlayer 2:")
                print("--------")
                try :
                    pos = int(input("Select Position(1-9) : "))-1
                except ValueError :
                    print('Entered Non-numeric data.')
                    pos = -1
            
            if pos in range(0,9) and board[pos] == " " :
                board[pos] = p2_sym
                p2_moves += 1
                display_board(board)
                if p2_moves > 2 and (check_rows(board,pos) or check_cols(board,pos) or check_diag(board,pos)) :
                        print(f"Player 2 Won with {p2_moves} Moves")
                        valid = 0
                        break
                valid = 1
            else :
                print("Invalid Choice")
                valid = 0
        
    if valid == 1 :
        print("\nGame Tied")    
        loop = replay()
    else :
        loop = replay()
        
print("\n\t\tTHANK YOU _/\_")        
    
    