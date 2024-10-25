import src.game
from src.demo import demo


def main():
    """Main function for the project.
    Calls the wanted function through user input.
    """

    decision = str(input('Type "demo" to see demo, "game" to play the game, anything else exits: '))

    if decision == 'demo':
        demo()

    elif decision == 'game':

        new_game = src.game.Game()

        new_game.run()
    else:
        print("bye bye")


if __name__ == "__main__":
    main()
