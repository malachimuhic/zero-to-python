def main():
    difficulty = input("Do you like 'difficult' or 'casual' games? ")
    player_amount = input("Do you like 'multiplayer' or 'single-player' ? ")
    
    if difficulty == "difficult":
        if player_amount == "multiplayer":
            recommend("Poker")
        elif player_amount == "single-player":
            recommend("Soliatre")
        else:
            print("Enter a valid number of players")
    elif difficulty == "casual":
        if player_amount == "multiplayer":
            recommend("Ten-thousand")
        elif player_amount == "single-player":
            recommend("52-pickup")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")
    

def recommend(game):
    print("You might like", game)

main()