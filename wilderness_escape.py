"""
Wilderness Escape: A text adventure implemented with a tree data structure.
"""


class StoryNode:
    """
    A tree node to store one piece of the text adventure.
    """

    def __init__(self, story):
        self.story = story
        self.children = []

    def add_child(self, child):
        """
        Adds another step in the adventure as a child node.

        Parameters
        ----------
        option : StoryNode
            An optional path for the player to go down
        """
        self.children.append(child)


class Game:
    """
    The Wilderness Escape game.

    Keeps track of the player's current location in the story tree.
    Allows the player to move forwards along a path of their own choosing.
    Separates the game from the details of the terminal interface.
    """

    def __init__(self, root_node):
        """
        Parameters
        ----------
        root_node : StoryNode
            The root node of the adventure story.
        """
        self.current_node = root_node

    def story_text(self):
        """
        Returns the text for the current point in the adventure.

        Returns
        -------
        string
            The text for the current point in the adventure.
        """
        return self.current_node.story

    def is_over(self):
        """
        Is the game over?

        Returns
        -------
        bool
            True if the game is over, false if it isn't.
        """
        return self.num_choices() == 0

    def num_choices(self):
        """
        Returns the number of choices available to the player.

        Returns
        -------
        int
            The number of choices available to the player.
        """
        return len(self.current_node.children)

    def choose(self, choice):
        """
        Updates the state of the game based on the player's choice.

        Parameters
        ----------
        choice : int
            The player's choice from the list of next move options.
            Must fall within the range of 1 up to the number of choices.

        Returns
        -------
        None
            If the choice was valid.
        int
            Returns 1 if the choice was invalid.
        """
        index = int(choice) - 1
        if index not in range(len(self.current_node.children)):
            return 1
        self.current_node = self.current_node.children[index]


def main():
    """
    Runs the game using the terminal as the interface.
    """
    story_root = StoryNode(
        """
    You are in a forest clearing. There is a path to the left. A bear emerges from the trees and roars!
    Do you: 
    1 ) Roar back!
    2 ) Run to the left...
    """
    )
    choice_a = StoryNode(
        """
    The bear is startled and runs away.
    Do you:
    1 ) Shout 'Sorry bear!'
    2 ) Yell 'Hooray!'
    """
    )
    choice_b = StoryNode(
        """
    You come across a clearing full of flowers. 
    The bear follows you and asks 'what gives?'
    Do you:
    1 ) Gasp 'A talking bear!'
    2 ) Explain that the bear scared you.
    """
    )
    choice_a_1 = StoryNode(
        """
    The bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
    """
    )
    choice_a_2 = StoryNode(
        """
    The bear returns and tells you that bullying is not okay before leaving you alone
    in the wilderness.

    YOU REMAIN LOST.
    """
    )
    choice_b_1 = StoryNode(
        """
    The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

    YOU REMAIN LOST.
    """
    )
    choice_b_2 = StoryNode(
        """
    The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.

    YOU HAVE ESCAPED THE WILDERNESS.
    """
    )
    choice_a.add_child(choice_a_1)
    choice_a.add_child(choice_a_2)
    choice_b.add_child(choice_b_1)
    choice_b.add_child(choice_b_2)
    story_root.add_child(choice_a)
    story_root.add_child(choice_b)
    game = Game(story_root)
    print("Once upon a time...")
    while True:
        print(game.story_text())
        if game.is_over():
            break
        players_choice = None
        while True:
            players_choice = input("Please choose an option: ")
            if players_choice.isnumeric() and (int(players_choice) - 1) in range(
                game.num_choices()
            ):
                break
            print("Invalid choice. Please try again.")
        game.choose(int(players_choice))


if __name__ == "__main__":
    main()
