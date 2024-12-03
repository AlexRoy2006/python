print("Welcome to Stick gament The Rule sfor stick game is : \n"
      " Two players take turns to play the game. \n "
      " Each player picks one set of sticks (needn’t be adjacent) during his turn. A set contains 1, 2, or 3 sticks. \n"
      " The player who takes the last stick is the loser")

# Who all are playing
player1 = input("enter the name of player 1:")
player2 = input("Enter the name of palyer 2:")
def playing():
    no_of_sticks = 16
    while no_of_sticks>0:

        print(f"The total no of sticks remaining = {no_of_sticks}")
        play=int(input(f"{player1}Take 1,2 or 3 sticks "))
        no_of_sticks-=play
        playe1=no_of_sticks
        play2=int(input(f"{player2} Take 1,2 or 3 sticks "))
        no_of_sticks-=play2
        playe2=no_of_sticks

        if playe1<=0:
            print(f"{player1}picks the last stick and looses the game")
        else:
            print(f"{player2}picks the last stick and looses the game")
playing()


