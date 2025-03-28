"""
how to use len(), clear(), keys(), and pop() to interact with dictionaries
"""

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")
       
        # TODO: Check id guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've guessed mega-word... INSTA WIN")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points")

    print("That's the game!")

main()