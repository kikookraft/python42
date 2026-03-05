"""TournamentCard: Card + Combatable + Rankable."""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card with full combat and ranking capabilities for tournaments."""

    _BASE_RATING = 1000

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
    ) -> None:
        """Initialise a tournament card.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            attack: Attack power.
            defense: Defense / block value.
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense = defense
        self._wins = 0
        self._losses = 0
        self._rating = self._BASE_RATING + (attack * 10) + (defense * 5)

    def get_card_info(self) -> dict:
        """Return full card information."""
        info = super().get_card_info()
        info["type"] = "Tournament"
        info["attack"] = self.attack_power
        info["defense"] = self.defense
        return info

    def play(self, game_state: dict) -> dict:
        """Deploy the tournament card onto the battlefield.

        Args:
            game_state: Current game state dictionary.

        Returns:
            A dict describing the play result.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered the arena",
        }

    # --- Combatable ---

    def attack(self, target) -> dict:
        """Attack a target using melee combat.

        Args:
            target: The target being attacked.

        Returns:
            A dict describing the attack result.
        """
        target_name = (
            target.name if hasattr(target, "name") else str(target)
        )
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage.

        Args:
            incoming_damage: The damage coming in.

        Returns:
            A dict describing the defense result.
        """
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
        }

    def get_combat_stats(self) -> dict:
        """Return combat statistics."""
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense,
        }

    # --- Rankable ---

    def calculate_rating(self) -> int:
        """Calculate the current ELO-style rating.

        Returns:
            The current rating as an integer.
        """
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Add wins and increase rating.

        Args:
            wins: Number of wins to add.
        """
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        """Add losses and decrease rating.

        Args:
            losses: Number of losses to add.
        """
        self._losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        """Return current rank information.

        Returns:
            A dict with wins, losses, and rating.
        """
        return {
            "name": self.name,
            "wins": self._wins,
            "losses": self._losses,
            "rating": self._rating,
        }

    def get_tournament_stats(self) -> dict:
        """Return comprehensive tournament statistics.

        Returns:
            A dict combining card info and rank info.
        """
        stats = self.get_card_info()
        stats.update(self.get_rank_info())
        return stats
