import unittest
from loto_game_magic_methods import Card, Player, Game


class TestMagicMethods(unittest.TestCase):
    def test_card_str(self):
        card = Card()
        self.assertIsInstance(str(card), str)

    def test_card_comparison(self):
        card1 = Card()
        card2 = Card()
        self.assertNotEqual(card1, card2)

    def test_player_str(self):
        player = Player("Test Player")
        self.assertIsInstance(str(player), str)

    def test_player_comparison(self):
        player1 = Player("Test Player")
        player2 = Player("Test Player")
        self.assertEqual(player1, player2)

    def test_game_len(self):
        game = Game([Player("Player 1"), Player("Player 2")])
        self.assertEqual(len(game), 90)


if __name__ == "__main__":
    unittest.main()
