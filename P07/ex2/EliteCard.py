from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """A powerful card combining card, combat, and magic interfaces."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
        mana_pool: int,
    ) -> None:
        """Initialize an elite card.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            attack: Base attack power.
            defense: Base defense / block value.
            mana_pool: Starting mana pool for spells.
        """
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError(f"Attack power of {attack} is invalid."
                             "Must be non-negative.")
        if defense < 0:
            raise ValueError(f"Defense value of {defense} is invalid."
                             "Must be non-negative.")
        if mana_pool < 0:
            raise ValueError(f"Mana pool value of {mana_pool} is invalid."
                             "Must be non-negative.")
        self.attack_power: int = attack
        self.defense: int = defense
        self.mana_pool: int = mana_pool

    def get_card_info(self) -> dict[str, str | int]:
        """Return full info for the elite card.
        returns:
        - type: Elite
        - attack: The card's attack power
        - defense: The card's defense value
        - mana_pool: The card's mana pool
        """
        info: dict[str, Any] = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["defense"] = self.defense
        info["mana_pool"] = self.mana_pool
        return info

    def play(self, game_state: dict[str, Any]) -> dict[str, str | int]:
        """Play the elite card onto the battlefield.
        returns:
        - card_played: The name of the card played
        - mana_used: The mana cost of the card
        - effect: A description of the effect applied (based on card type)"""
        if game_state.get("mana", 0) < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play this card.",
            }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed - combat and magic ready",
        }

    # --- Combatable interface ---

    def attack(self, target: Any) -> dict[str, str | int]:
        """Attack a target using melee combat.
        returns:
        - attacker: The name of the attacking card
        - target: The name of the target being attacked
        - damage: The amount of damage dealt (based on attack power)
        - combat_type: The type of combat used (e.g. "melee")
        """
        target_name: Any | str = target.name \
            if hasattr(target, "name") else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, str | int | bool]:
        """Block incoming damage using defense value.

        returns:
        - defender: The name of the defending card
        - damage_taken: The amount of damage taken after blocking
        - damage_blocked: The amount of damage blocked by defense
        - still_alive: Whether the card is still alive
        """
        blocked: int = min(self.defense, incoming_damage)
        taken: int = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < self.defense
        }

    def get_combat_stats(self) -> dict[str, str | int]:
        """Return the card's combat statistics."""
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense,
        }

    # --- Magical interface ---

    def cast_spell(self,
                   spell_name: str,
                   targets: list[str]) -> dict[str, str | int | list[str]]:
        """Cast a named spell at the given targets.
        returns:
        - caster: The name of the card casting the spell
        - spell: The name of the spell being cast
        - targets: The list of targets the spell is cast on
        - mana_used: The amount of mana consumed (based on number of targets)
        """
        mana_cost: int = max(1, len(targets) + 1)
        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict[str, str | int]:
        """Channel additional mana into the pool.
        returns:
        - card: The name of the card channeling mana
        - mana_channeled: The amount of mana added to the pool
        - total_mana: The new total mana pool after channeling
        """
        self.mana_pool += amount
        return {
            "card": self.name,
            "mana_channeled": amount,
            "total_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict[str, str | int]:
        """Return the card's magic statistics."""
        return {
            "name": self.name,
            "mana_pool": self.mana_pool,
        }
