import random


class Domino:
    def __init__(self, num_players=2):
        """
        Initialize the game with a full set of dominoes and number of players.
        """
        self.num_players = num_players
        self.dominoes = self.generate_domino_set()
        self.players = [[] for _ in range(self.num_players)]  # Hands for all players
        self.stock = []  # Remaining dominoes to draw from
        self.board = []  # The domino chain
        self.scores = [0] * self.num_players  # Scores for all players

    def generate_domino_set(self):
        """
        Generate a complete set of 28 dominoes.
        Each domino is a tuple (a, b), where a <= b.
        """
        return [(a, b) for a in range(7) for b in range(a, 7)]

    def shuffle_and_deal(self):
        """
        Shuffle the dominoes and deal tiles to each player.
        The rest goes to the stock (pile).
        """
        random.shuffle(self.dominoes)
        tiles_per_player = 7 if self.num_players <= 2 else 5
        for i in range(self.num_players):
            self.players[i] = self.dominoes[i * tiles_per_player:(i + 1) * tiles_per_player]
        self.stock = self.dominoes[self.num_players * tiles_per_player:]

    def find_starting_player(self):
        """
        Determine which player starts the game.
        The player with the highest double (e.g., 6|6) starts.
        """
        highest_double = -1
        starting_player = -1

        for player_idx, hand in enumerate(self.players):
            for tile in hand:
                if tile[0] == tile[1] and tile[0] > highest_double:
                    highest_double = tile[0]
                    starting_player = player_idx

        return starting_player

    def can_play(self, tile, left_end, right_end):
        """
        Check if a tile can be played on the board.
        A tile can be played if one of its sides matches either end of the board.
        """
        return tile[0] == left_end or tile[1] == left_end or \
               tile[0] == right_end or tile[1] == right_end

    def play_tile(self, tile, left_end, right_end):
        """
        Add a tile to the board, adjusting its orientation if necessary.
        """
        if tile[0] == left_end or tile[1] == left_end:
            # Add tile to the left side
            if tile[1] == left_end:
                tile = (tile[1], tile[0])  # Flip tile
            self.board.insert(0, tile)
        else:
            # Add tile to the right side
            if tile[0] == right_end:
                tile = (tile[1], tile[0])  # Flip tile
            self.board.append(tile)

    def draw_tile(self, player_idx):
        """
        Allow a player to draw a tile from the stock if they cannot play.
        """
        if self.stock:
            tile = self.stock.pop()
            self.players[player_idx].append(tile)
            return tile
        return None

    def calculate_score(self, hand):
        """
        Calculate the score of a player's hand (sum of all remaining tile values).
        """
        return sum(sum(tile) for tile in hand)

    def display_game_state(self):
        """Display the current state of the game."""
        print(f"\nBoard: {self.board}")
        for i, player_hand in enumerate(self.players):
            print(f"Player {i + 1} hand: {player_hand}")
        print(f"Stock: {len(self.stock)} tiles remaining")

    def play_game(self):
        """
        Run the game loop.
        Players take turns to play until one wins or no moves are possible.
        """
        self.shuffle_and_deal()
        starting_player = self.find_starting_player()

        # If no starting player found (no doubles), the first player goes
        current_player = starting_player if starting_player != -1 else 0

        if starting_player != -1:
            # Place the first tile
            first_tile = self.players[current_player].pop(
                self.players[current_player].index((starting_player, starting_player))
            )
            self.board.append(first_tile)
        else:
            print("No double found, starting without it.")

        while True:
            self.display_game_state()

            # Get the ends of the board
            left_end = self.board[0][0] if self.board else None
            right_end = self.board[-1][1] if self.board else None

            # Check if current player can play
            player_hand = self.players[current_player]
            playable_tiles = [tile for tile in player_hand if self.can_play(tile, left_end, right_end)]

            if playable_tiles:
                # Play the first available tile
                chosen_tile = playable_tiles[0]
                self.play_tile(chosen_tile, left_end, right_end)
                player_hand.remove(chosen_tile)
                print(f"Player {current_player + 1} plays {chosen_tile}")
            else:
                # No playable tile, draw from stock
                print(f"Player {current_player + 1} cannot play. Drawing from stock.")
                drawn_tile = self.draw_tile(current_player)
                if drawn_tile:
                    print(f"Player {current_player + 1} draws {drawn_tile}.")
                else:
                    print("Stock is empty. Game may be blocked.")

            # Check if the current player has won
            if not player_hand:
                print(f"Player {current_player + 1} wins!")
                break

            # Check if the game is blocked
            if all(not [tile for tile in hand if self.can_play(tile, left_end, right_end)] for hand in self.players):
                print("Game is blocked!")
                break

            # Switch to the next player
            current_player = (current_player + 1) % self.num_players

        # Calculate scores for a blocked game
        print("\nGame over! Final Scores:")
        for i, hand in enumerate(self.players):
            self.scores[i] = self.calculate_score(hand)
            print(f"Player {i + 1} score: {self.scores[i]}")

        winner = self.scores.index(min(self.scores))
        print(f"\nPlayer {winner + 1} wins with the lowest score!")


# Main execution
if __name__ == "__main__":
    num_players = int(input("Enter the number of players (2-4): "))
    if num_players < 2 or num_players > 4:
        print("Invalid number of players. Defaulting to 2 players.")
        num_players = 2

    game = Domino(num_players)
    game.play_game()
