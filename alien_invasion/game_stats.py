import json
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1 

    def load_high_score(self):
        path = Path("alien_invasion/highscore.json")
        try:
            saved_score = path.read_text()
            high_score = json.loads(saved_score)
            return high_score
        except FileNotFoundError:
            return 0 