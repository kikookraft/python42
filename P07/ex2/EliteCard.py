"""EliteCard: multiple inheritance from Card, Combatable, and Magical."""

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
        self.attack_power = attack
        self.defense = defense
        self.mana_pool = mana_pool

    def get_card_info(self) -> dict:
        """Return full info for the elite card."""
        info = super().get_card_info()
        info["type"] = "Elite"
        info["attack"] = self.attack_power
        info["defense"] = self.defense
        info["mana_pool"] = self.mana_pool
        return info

    def play(self, game_state: dict) -> dict:
        """Play the elite card onto the battlefield.

        Args:
            game_state: Current game state dictionary.

        Returns:
            A dict describing the result of playing the card.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed - combat and magic ready",
        }

    # --- Combatable interface ---

    def attack(self, target) -> dict:
        """Attack a target using melee combat.

        Args:
            target: The target being attacked.

        Returns:
            A dict describing the attack result.
        """
        target_name = target.name if hasattr(target, "name") else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        """Block incoming damage using defense value.

        Args:
            incoming_damage: The amount of damage coming in.

        Returns:
            A dict describing the defense result.
        """
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": taken < 10,
        }

    def get_combat_stats(self) -> dict:
        """Return the card's combat statistics."""
        return {
            "name": self.name,
            "attack": self.attack_power,
            "defense": self.defense,
        }

    # --- Magical interface ---

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a named spell at the given targets.

        Args:
            spell_name: The name of the spell to cast.
            targets: A list of target names.

        Returns:
            A dict describing the cast result.
        """
        mana_cost = max(1, len(targets) + 1)
        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel additional mana into the pool.

        Args:
            amount: The amount of mana to channel.

        Returns:
            A dict describing the channeling result.
        """
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        """Return the card's magic statistics."""
        return {
            "name": self.name,
            "mana_pool": self.mana_pool,
        }
