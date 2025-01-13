import pytest
from loto_game import Card, Player, Game

def test_card_generate():
    card = Card()
    assert len(card.grid) == 3  # Должно быть 3 строки
    assert all(len(row) == 9 for row in card.grid)  # В каждой строке 9 ячеек

def test_mark_number():
    card = Card()
    number = card.grid[0][0]  # Берем первое число из карты
    assert card.mark_number(number)  # Число должно быть отмечено
    assert card.grid[0][0] == 'X'  # Проверяем, что число заменилось на 'X'

def test_game():
    player1 = Player("Player 1")
    player2 = Player("Computer")
    game = Game([player1, player2])
    assert len(game.bag) == 90  # В мешке должно быть 90 бочонков
