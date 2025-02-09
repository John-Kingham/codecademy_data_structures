import unittest
from wilderness_escape import StoryNode, Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.story_root = StoryNode(
            """
        You are in a forest clearing. There is a path to the left. A bear emerges from the trees and roars!
        Do you: 
        1 ) Roar back!
        2 ) Run to the left...
        """
        )
        self.choice_a = StoryNode(
            """
        The bear is startled and runs away.
        Do you:
        1 ) Shout 'Sorry bear!'
        2 ) Yell 'Hooray!'
        """
        )
        self.choice_b = StoryNode(
            """
        You come across a clearing full of flowers. 
        The bear follows you and asks 'what gives?'
        Do you:
        1 ) Gasp 'A talking bear!'
        2 ) Explain that the bear scared you.
        """
        )
        self.choice_a_1 = StoryNode(
            """
        The bear returns and tells you it's been a rough week. After making peace with a talking bear, he shows you the way out of the forest.

        YOU HAVE ESCAPED THE WILDERNESS.
        """
        )
        self.choice_a_2 = StoryNode(
            """
        The bear returns and tells you that bullying is not okay before leaving you alone
        in the wilderness.

        YOU REMAIN LOST.
        """
        )
        self.choice_b_1 = StoryNode(
            """
        The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

        YOU REMAIN LOST.
        """
        )
        self.choice_b_2 = StoryNode(
            """
        The bear understands and apologizes for startling you. Your new friend shows you a path leading out of the forest.

        YOU HAVE ESCAPED THE WILDERNESS.
        """
        )
        self.choice_a.add_child(self.choice_a_1)
        self.choice_a.add_child(self.choice_a_2)
        self.choice_b.add_child(self.choice_b_1)
        self.choice_b.add_child(self.choice_b_2)
        self.story_root.add_child(self.choice_a)
        self.story_root.add_child(self.choice_b)
        self.game = Game(self.story_root)

    def test_game(self):
        self.assertFalse(self.game.is_over())
        self.assertEqual(self.game.story_text(), self.story_root.story)
        self.game.choose(1)
        self.assertEqual(self.game.story_text(), self.choice_a.story)
        self.game.choose(2)
        self.assertEqual(self.game.story_text(), self.choice_a_2.story)
        self.assertTrue(self.game.is_over())
