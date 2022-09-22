from grid import Grid

def main():
    grid = Grid()
    there_is_a_winner = False
    #Player 1's moves
    while there_is_a_winner == False:
        if there_is_a_winner == False:
            grid.display()
            x = input("Player 1, please type in the cell number for your x: ")
            if x in grid.grid:
                grid.grid[f'{str(x)}'] = 'x'
                winner = "Player 1"
                there_is_a_winner = grid.check_for_winner()
            else:
                print("This is not a valid field. Try again")
                return 1

        #Player 2's moves
        if there_is_a_winner == False:
            grid.display()
            x = input("Player 2, please type in the cell number for your o: ")
            if x in grid.grid:
                grid.grid[f'{str(x)}'] = 'o'
                winner = "Player 2"
                there_is_a_winner = grid.check_for_winner()
            else:
                print("This is not a valid field. Try again")
                return 1
    
    print(f"The winner is {winner}")




if __name__ == "__main__":
    main()