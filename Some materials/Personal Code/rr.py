import random

class RussianRoulette:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.bullet_chamber = random.randint(1, 6)
        self.current_player = 0

        for i in range(num_players):
            self.players.append({
                'name': f'Player {i + 1}',
                'alive': True,
                'bullets': 0
            })

    def load_bullet(self, player_idx):
        if not self.players[player_idx]['alive']:
            print(f"{self.players[player_idx]['name']} is already out of the game.")
            return

        if self.players[player_idx]['bullets'] >= 6:
            print(f"{self.players[player_idx]['name']} cannot load more than 6 bullets.")
            return

        self.players[player_idx]['bullets'] += 1
        print(f"{self.players[player_idx]['name']} loads a bullet into the gun.")

    def spin_chamber(self):
        self.bullet_chamber = random.randint(1, 6)
        print("The chamber is spun.")

    def pull_trigger(self, player_idx):
        if not self.players[player_idx]['alive']:
            print(f"{self.players[player_idx]['name']} is already out of the game.")
            return

        if random.randint(1, 6) == self.bullet_chamber:
            self.players[player_idx]['alive'] = False
            print(f"{self.players[player_idx]['name']} shoots themselves and is out of the game.")
        else:
            print(f"{self.players[player_idx]['name']} pulls the trigger and survives this round.")

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def play_game(self):
        print("Welcome to Russian Roulette!")
        print("Each player will take turns loading bullets, spinning the chamber, and pulling the trigger.")
        print("The game continues until only one player remains.")

        while sum(player['alive'] for player in self.players) > 1:
            player = self.players[self.current_player]
            print(f"\n{player['name']}'s turn:")

            action = input("Choose an action (load/spin/pull): ").lower()
            if action == 'load':
                self.load_bullet(self.current_player)
            elif action == 'spin':
                self.spin_chamber()
            elif action == 'pull':
                self.pull_trigger(self.current_player)
                self.next_player()
            else:
                print("Invalid action. Please choose 'load', 'spin', or 'pull'.")

        winner = next(player for player in self.players if player['alive'])
        print(f"\nCongratulations, {winner['name']}! You survived Russian Roulette.")

# Example usage:
num_players = 3
game = RussianRoulette(num_players)
game.play_game()
