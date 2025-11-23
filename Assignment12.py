def _start_game(self):
    """Start a new game from Play button or pressing P."""
    # Reset game settings
    self.settings.initialize_dynamic_settings()

    # Reset statistics
    self.stats.reset_stats()
    self.stats.game_active = True

    # Reset scoreboard images
    self.sb.prep_score()
    self.sb.prep_high_score()
    self.sb.prep_level()
    self.sb.prep_ships()

    # Empty aliens and bullets
    self.aliens.empty()
    self.bullets.empty()

    # Create new fleet and center ship
    self._create_fleet()
    self.ship.center_ship()

    # Hide mouse
    pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
    """Start a new game when clicking Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        self._start_game()

def __init__(self, ai_game):
    """Initialize statistics."""
    self.settings = ai_game.settings

    # Load high score from file
    try:
        with open("high_score.txt", "r") as f:
            self.high_score = int(f.read())
    except FileNotFoundError:
        self.high_score = 0

    self.reset_stats()
    self.game_active = False
