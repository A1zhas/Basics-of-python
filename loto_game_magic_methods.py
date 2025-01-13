import random

class Card:
    def __init__(self):
        self.grid = self.generate_card()

    def generate_card(self):
        rows = []
        all_numbers = random.sample(range(1, 91), 15)
        for i in range(3):
            row_numbers = sorted(all_numbers[i * 5:(i + 1) * 5])
            row = [' '] * 9
            for num in row_numbers:
                index = random.randint(0, 8)
                while row[index] != ' ':
                    index = random.randint(0, 8)
                row[index] = num
            rows.append(row)
        return rows

    def mark_number(self, number):
        for row in self.grid:
            if number in row:
                row[row.index(number)] = 'X'
                return True
        return False

    def is_complete(self):
        return all(cell == 'X' or cell == ' ' for row in self.grid for cell in row)

    def __str__(self):
        return "\n".join(" ".join(str(cell).rjust(2) for cell in row) for row in self.grid)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.grid == other.grid


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card()

    def take_turn(self, number):
        if self.card.mark_number(number):
            print(f"{self.name} found {number}!")
        else:
            print(f"{self.name} does not have {number}.")

    def has_won(self):
        return self.card.is_complete()

    def __str__(self):
        return f"Player: {self.name}\nCard:\n{self.card}"

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name == other.name

class Game:
    def __init__(self, players):
        self.players = players
        self.bag = list(range(1, 91))
        random.shuffle(self.bag)

    def draw_number(self):
        return self.bag.pop() if self.bag else None

    def play(self):
        print("Starting the game of Loto!")
        while self.bag:
            number = self.draw_number()
            print(f"\nNumber drawn: {number}")

            for player in self.players:
                player.take_turn(number)
                if player.has_won():
                    print(f"\n{player.name} wins!")
                    return
        print("No one wins, all numbers are drawn.")

    def __str__(self):
        return f"Game with {len(self.players)} players. Numbers remaining in the bag: {len(self.bag)}"

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return self.players == other.players and self.bag == other.bag

    def __len__(self):
        return len(self.bag)


# Setup for the game
if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Computer")
    game = Game([player1, player2])
    game.play()
