import random

class Dice:
    def __init__(self):
        # Dice has 6 faces
        self.faces = [1, 2, 3, 4, 5, 6]
    
    def roll(self):
        # Randomly selects a face from the dice
        return random.choice(self.faces)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0
    
    def roll(self, dice):
        # Roll the dice
        roll_result = dice.roll()
        return roll_result
    
    def hold(self):
        # Add turn total to player score
        self.score += self.turn_total
        self.turn_total = 0

class Game:
    def __init__(self, player1_name, player2_name):
        self.dice = Dice()
        self.players = [Player(player1_name), Player(player2_name)]
        self.current_player = self.players[0]
    
    def play_turn(self):
        action = input(f"{self.current_player.name}'s turn:\n"
                       f"Current score: {self.current_player.score}, "
                       f"Turn score: {self.current_player.turn_total}\n"
                       "Enter 'r' to roll or 'h' to hold: ")
        
        if action == 'r':
            roll_result = self.current_player.roll(self.dice)
            print(f"Rolled a {roll_result}")
            if roll_result == 1:
                self.current_player.turn_total = 0  # End the turn with no points
            else:
                self.current_player.turn_total += roll_result
        elif action == 'h':
            self.current_player.hold()
            self.switch_player()

    def switch_player(self):
        # Switch to the next player
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
    
    def is_game_over(self):
        # Check if either player has reached or exceeded 100 points
        return self.players[0].score >= 100 or self.players[1].score >= 100
    
    def get_winner(self):
        # Get the winner of the game
        if self.players[0].score >= 100:
            return self.players[0]
        else:
            return self.players[1]

def main():
    game = Game("Player 1", "Player 2")
    while not game.is_game_over():
        game.play_turn()

    winner = game.get_winner()
    print(f"Game over! {winner.name} wins with {winner.score} points!")

if __name__ == "__main__":
    main()
