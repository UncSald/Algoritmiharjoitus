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
        width = 1500
        height = 1000

        new_game = src.game.Game(width,height)

        new_game.run()
    else:
        print("bye bye")


if __name__ == "__main__":
    main()
