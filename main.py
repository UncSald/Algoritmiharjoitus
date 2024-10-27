import src.game
from src.demo import Demo

"""Contains the main function for the project.
"""

def main():
    """Main function for the project.
    Calls the wanted function through user input.
    """

    decision = str(input('Type "demo" to see demo, "game" to play the game, anything else exits: '))

    if decision == 'demo':
        demo = Demo(1500,900,1)
        demo.run()

    elif decision == 'game':
        new_game = src.game.Game()
        new_game.run()

    else:
        print("bye bye")


if __name__ == "__main__":
    main()
