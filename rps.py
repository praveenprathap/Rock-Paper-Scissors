import random
print("\nRock Paper Sissors\n================\n")

#reading the player name
user_name=input("Player name : ").lower()
print("\nBot vs "+user_name+"\nReady to PLay\n")

#accessing the input from the user
while True:
    user_in = input("Type your Move :").lower()
    in_values = ['rock', 'paper', 'scissors']

    print(user_name+" Choice is :"+ user_in)

    #random selection from preset values in[in_values]
    pc_in = random.choice(in_values)
    print("Bot choice is", pc_in)

    #comparing the user nd bot values, executing the operation
    if user_in in in_values:
        if user_in == pc_in:
            print("Draw")
        if user_in =="rock":
            if pc_in == "paper":
                print('Sry '+user_name+" Better luck 4 nxt tym ")
            elif pc_in == 'scissors':
                print(user_name + " congrats, you win")
        if user_in == 'paper':
            if pc_in == "scissors":
                print('Sry '+user_name+" Better luck 4 nxt tym ")
            elif pc_in == "rock":
                print(user_name + " congrats, you win")
        if user_in == 'scissors':
            if pc_in == 'rock':
                print('Sry '+user_name+" Better luck 4 nxt tym ")
            elif pc_in == 'paper':
                print(user_name + " congrats, you win")
    else:
        print('\ninvalid command from '+ user_name+ '\nTry [Rock, Paper, Scissors]')
    print()

    user_in = input("Do you want to play again? (y/n)")
    if user_in in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_in in ["N", "n", "no", "No"]:
        break
    else:
        break

