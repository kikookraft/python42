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
        """Initialize a tournament card.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            attack: Attack power.
            defense: Defense / block value.
        """
        super().__init__(name, cost, rarity)
        self.attack_power: int = attack
        self.defense: int = defense
        self._wins: int = 0
        self._losses: int = 0
        self._rating: int = (
            self._BASE_RATING + (attack * 10) + (defense * 5)
        )

    def get_card_info(self) -> dict[str, str | int]:
        """Return full card information.
        returns:
        - type: Tournament
        - attack: The card's attack power
        - defense: The card's defense value
        """
        info: dict[str, str | int] = super().get_card_info()
        info["type"] = "Tournament"
        info["attack"] = self.attack_power
        info["defense"] = self.defense
        return info

    def play(self, game_state: dict[str, int]) -> dict[str, str | int]:
        """Deploy the tournament card onto the battlefield.
        returns:
        - card_played: The name of the card played
        - mana_used: The mana cost of the card
        - effect: A description of the effect applied
        """
        if game_state.get("mana", 0) < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play the card",
            }
        if self.attack_power > 5:
            effect_desc: str = "Powerful attack boosts morale!"
        elif self.defense > 5:
            effect_desc = "Sturdy defense inspires confidence!"
        else:
            effect_desc = "A balanced card enters the arena."
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_desc,
        }

    # --- Combatable ---

    def attack(self, target: "Combatable") -> dict[str, str | int]:
        """Attack a target using melee combat.
        returns:
        - attacker: The name of the attacking card
        - target: The name of the target
        - damage: The amount of damage dealt
        """
        target_name: str = str(getattr(target, "name", target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict[str, str | int]:
        """Defend against incoming damage.
        returns:
        - defender: The name of the defending card
        - damage_taken: The amount of damage taken after blocking
        - damage_blocked: The amount of damage blocked
        """
        blocked: int = min(self.defense, incoming_damage)
        taken: int = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
        }

    def get_combat_stats(self) -> dict[str, str | int]:
        """Return combat statistics."""
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense,
        }

    # --- Rankable ---

    def calculate_rating(self) -> int:
        """Calculate the current ELO-style rating."""
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Add wins and increase rating."""
        self._wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        """Add losses and decrease rating."""
        self._losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict[str, str | int]:
        """Return current rank information.
        returns:
        - name: The card's name
        - wins: Total wins
        - losses: Total losses
        - rating: Current rating
        """
        return {
            "name": self.name,
            "wins": self._wins,
            "losses": self._losses,
            "rating": self._rating,
        }

    def get_tournament_stats(self) -> dict[str, str | int]:
        """Return comprehensive tournament statistics."""
        stats: dict[str, str | int] = self.get_card_info()
        stats.update(self.get_rank_info())
        return stats
