import unittest
from loto_game import Card, Player, Game


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card()

    def test_card_generate(self):
        self.assertEqual(len(self.card.grid), 3, "Card should have 3 rows")
        for row in self.card.grid:
            self.assertEqual(len(row), 9, "Each row should have 9 cells")

    def test_mark_number(self):
        number = self.card.grid[0][0]  # Берем первое число из карты
        self.assertTrue(self.card.mark_number(number), "Number should be marked")
        self.assertEqual(self.card.grid[0][0], 'X', "Number should be replaced with 'X'")

    def test_is_complete(self):
        # Заменяем все числа на 'X' и проверяем, что карта завершена
        for row in self.card.grid:
            for i in range(9):
                if row[i] != ' ':
                    row[i] = 'X'
        self.assertTrue(self.card.is_complete(), "Card should be complete")


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")

    def test_take_turn(self):
        number = self.player.card.grid[0][0]
        self.player.take_turn(number)
        self.assertEqual(self.player.card.grid[0][0], 'X', "Player should mark the number on the card")

    def test_has_won(self):
        self.assertFalse(self.player.has_won(), "Player should not have won initially")
        for row in self.player.card.grid:
            for i in range(9):
                if row[i] != ' ':
                    row[i] = 'X'
        self.assertTrue(self.player.has_won(), "Player should win after marking all numbers")


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Computer")
        self.game = Game([self.player1, self.player2])

    def test_game_setup(self):
        self.assertEqual(len(self.game.bag), 90, "Bag should have 90 numbers")
        self.assertEqual(len(self.game.players), 2, "Game should have 2 players")

    def test_draw_number(self):
        number = self.game.bag[-1]
        self.game.bag.pop()
        self.assertNotIn(number, self.game.bag, "Number should be removed from the bag")


if __name__ == "__main__":
    unittest.main()

