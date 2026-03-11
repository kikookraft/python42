from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional, List
from pydantic import BaseModel, Field, ValidationError, model_validator
import random as rand


class Color:
    """ANSI color codes for terminal output."""
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    @staticmethod
    def red(text: str) -> str:
        return f"{Color.RED}{text}{Color.RESET}"

    @staticmethod
    def green(text: str) -> str:
        return f"{Color.GREEN}{text}{Color.RESET}"

    @staticmethod
    def yellow(text: str) -> str:
        return f"{Color.YELLOW}{text}{Color.RESET}"

    @staticmethod
    def blue(text: str) -> str:
        return f"{Color.BLUE}{text}{Color.RESET}"

    @staticmethod
    def magenta(text: str) -> str:
        return f"{Color.MAGENTA}{text}{Color.RESET}"

    @staticmethod
    def cyan(text: str) -> str:
        return f"{Color.CYAN}{text}{Color.RESET}"


class ContactType(str, Enum):
    """Enumeration for types of alien contact."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Data model for logging alien contact reports with
    complex validation rules."""
    contact_id: str = Field(...,
                            min_length=5,
                            max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(...,
                          min_length=3,
                          max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(...,
                                   ge=0.0,
                                   le=10.0)
    duration_minutes: int = Field(...,
                                  ge=1,
                                  le=1440)
    witness_count: int = Field(...,
                               ge=1,
                               le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> 'AlienContact':
        """Custom validation rules for AlienContact."""
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                f"Contact ID must start with 'AC': {self.contact_id}")
        if self.contact_type == ContactType.PHYSICAL \
                and self.is_verified is False:
            raise ValueError(
                "Physical contacts must be verified.")
        if self.contact_type == ContactType.TELEPATHIC \
                and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 \
                and not self.message_received:
            raise ValueError(
                "Strong signals must have a message received.")
        return self

    def tostr(self) -> str:
        """Represent Alien Contact with colors."""
        return (f"{Color.green('AlienContact:  ')}{self.contact_id} - \n"
                f"  Timestamp: {Color.cyan(self.timestamp.isoformat())}\n"
                f"  Location: {Color.blue(self.location)}\n"
                f"  Contact Type: {Color.yellow(self.contact_type.value)}\n"
                "  Signal Strength: "
                f"{Color.magenta(str(self.signal_strength))}\n"
                "  Duration: "
                f"{Color.green(str(self.duration_minutes) + ' min')}\n"
                f"  Witnesses: {Color.red(str(self.witness_count))}\n"
                f"  Verified: {Color.green(str(self.is_verified))}\n"
                f"  Message: {Color.cyan(self.message_received or 'None')}\n")


def demonstrate() -> None:
    print("="*40)
    try:
        from data_generator import AlienContactGenerator, DataConfig
    except ImportError as e:
        print(
            f"{Color.YELLOW}Error importing AlienContactGenerator: \n"
            f"{Color.RED}{e}{Color.RESET}\n"
            "Please ensure data_generator is in the same directory"
            " as this script.")
        exit(1)  # Exit with error code to indicate failure
        return

    contact_list: List[AlienContact] = []
    generator = AlienContactGenerator(DataConfig(seed=rand.randint(1, 1000)))
    generated_contacts: List[Dict[str, Any]] = \
        generator.generate_contact_data()
    for contact in generated_contacts:
        try:
            alien_contact = AlienContact(**contact)
            contact_list.append(alien_contact)
        except ValidationError as e:
            print(
                f"{Color.YELLOW}Validation error for contact: "
                f"{contact.get('contact_id', 'unknown')}: "
                f"{Color.RED}{e}{Color.RESET}")
    for contact in contact_list:
        print(contact.tostr())


if __name__ == "__main__":
    demonstrate()
