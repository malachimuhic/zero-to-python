"""
How to use clear() and pop() to interact with lists
"""

def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            history.pop()
        elif action == "Restart":
            print("Restarting Game")
            history.clear()
        else:
            history.append(action)
        print(history)

main()