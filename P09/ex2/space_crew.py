from datetime import datetime
from enum import Enum
from typing import Any, Dict, List
import random as rand
from pydantic import BaseModel, Field, ValidationError, model_validator


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
        """Wrap text in color codes."""
        return f"{Color.RED}{text}{Color.RESET}"

    @staticmethod
    def green(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.GREEN}{text}{Color.RESET}"

    @staticmethod
    def yellow(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.YELLOW}{text}{Color.RESET}"

    @staticmethod
    def blue(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.BLUE}{text}{Color.RESET}"

    @staticmethod
    def magenta(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.MAGENTA}{text}{Color.RESET}"

    @staticmethod
    def cyan(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.CYAN}{text}{Color.RESET}"


class Rank(str, Enum):
    """Enumeration for crew member ranks."""
    CADET = "cadet"
    LIEUTENANT = "lieutenant"
    COMMANDER = "commander"
    CAPTAIN = "captain"
    OFFICER = "officer"


class CrewMember(BaseModel):
    """Data model for an individual crew member."""
    member_id: str = Field(...,
                           min_length=3,
                           max_length=10)
    name: str = Field(...,
                      min_length=2,
                      max_length=50)
    rank: Rank = Field(...)
    age: int = Field(...,
                     ge=18,
                     le=80)
    specialization: str = Field(...,
                                min_length=3,
                                max_length=30)
    years_experience: int = Field(...,
                                  ge=0,
                                  le=50)
    is_active: bool = True

    def tostr(self) -> str:
        """Represent CrewMember with colors."""
        active: str = (
            Color.green("Yes") if self.is_active else Color.red("No"))
        return (
            f"  {Color.green(self.member_id)} | "
            f"{Color.blue(self.name)} | "
            f"Rank: {Color.yellow(self.rank.value)} | "
            f"Age: {Color.cyan(str(self.age))} | "
            f"Spec: {Color.magenta(self.specialization)} | "
            f"Exp: {Color.cyan(str(self.years_experience))} yrs | "
            f"Active: {active}")


class SpaceMission(BaseModel):
    """Data model for a space mission with crew validation."""
    mission_id: str = Field(...,
                            min_length=5,
                            max_length=15)
    mission_name: str = Field(...,
                              min_length=3,
                              max_length=100)
    destination: str = Field(...,
                             min_length=3,
                             max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(...,
                               ge=1,
                               le=3650)
    crew: List[CrewMember] = Field(...,
                                   min_length=1,
                                   max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(...,
                                   ge=1.0,
                                   le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> 'SpaceMission':
        """Cross-field validation for SpaceMission."""
        if not self.mission_id.startswith("M"):
            raise ValueError(
                f"Mission ID must start with 'M': {self.mission_id}")
        ids: List[str] = [m.member_id for m in self.crew]
        if len(ids) != len(set(ids)):
            raise ValueError(
                "Duplicate member_id values found in crew.")
        inactive: List[str] = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                "All crew members must be active. "
                f"Inactive: {', '.join(inactive)}")
        ranks: List[Rank] = [m.rank for m in self.crew]
        if Rank.CAPTAIN not in ranks and Rank.COMMANDER not in ranks:
            raise ValueError(
                "Mission must have at least one Commander or Captain.")
        if self.duration_days > 365:
            experienced: int = sum(
                1 for m in self.crew if m.years_experience >= 5)
            required: int = max(1, len(self.crew) // 2)
            if experienced < required:
                raise ValueError(
                    f"Long missions (>365 days) need at least {required} "
                    f"crew member(s) with 5+ years experience "
                    f"(found {experienced}).")
        return self

    def tostr(self) -> str:
        """Represent SpaceMission with colors."""
        crew_lines: str = "\n".join(m.tostr() for m in self.crew)
        return (
            f"{Color.green('Mission:')} {self.mission_id} — "
            f"{Color.blue(self.mission_name)}\n"
            f"  Destination: {Color.cyan(self.destination)}\n"
            f"  Launch:      "
            f"{Color.magenta(self.launch_date.strftime('%Y-%m-%d %H:%M'))}\n"
            f"  Duration:    {Color.yellow(str(self.duration_days))} days\n"
            f"  Status:      {Color.yellow(self.mission_status)}\n"
            f"  Budget:      "
            f"{Color.green('$' + str(self.budget_millions) + 'M')}\n"
            f"  Crew ({len(self.crew)}):\n{crew_lines}\n")


def demonstrate() -> None:
    """Generate and validate space mission data using the data generator."""
    sep: str = "=" * 41
    print(f"\n{Color.cyan('Generated Mission Data')}")
    print(sep)
    try:
        from data_generator import CrewMissionGenerator, DataConfig
    except ImportError as e:
        print(
            f"{Color.YELLOW}Error importing CrewMissionGenerator:\n"
            f"{Color.RED}{e}{Color.RESET}\n"
            "Please ensure data_generator.py is in the same directory.")
        exit(1)
        return

    mission_list: List[SpaceMission] = []
    generator = CrewMissionGenerator(
        DataConfig(seed=rand.randint(1, 42)))
    generated_missions: List[Dict[str, Any]] = \
        generator.generate_mission_data()

    for mission_data in generated_missions:
        try:
            mission = SpaceMission(**mission_data)
            mission_list.append(mission)
        except ValidationError as e:
            print(
                f"{Color.yellow('Validation error for mission:')} "
                f"{Color.green(mission_data.get('mission_id', 'unknown'))}: "
                f"{Color.red(str(e))}")

    for mission in mission_list:
        print(mission.tostr())

    print(sep)

    # --- Hardcoded invalid examples ---
    print(f"\n{Color.cyan('Invalid Data Examples')}")
    print(sep)

    # Invalid CrewMember: impossible experience for age, and rank too low exp
    print(Color.yellow(
        "Invalid CrewMember (age 20, 15 yrs exp, captain):"))
    try:
        CrewMember(
            member_id="BAD01",
            name="Young Gun",
            rank=Rank.CAPTAIN,
            age=20,
            specialization="Navigation",
            years_experience=15,
            is_active=True,
        )
    except ValidationError as e:
        for err in e.errors():
            print(Color.red(
                f"  - {err['msg'].replace('Value error, ', '')}"))

    print()

    # Invalid SpaceMission: ID missing "M" prefix, no commander/captain,
    # inactive crew member
    print(Color.yellow(
        "Invalid SpaceMission (bad ID, inactive crew, no commander):"))
    try:
        SpaceMission(
            mission_id="NOMIS001",
            mission_name="Ghost Flight",
            destination="Deep Space",
            launch_date=datetime(2025, 1, 1),
            duration_days=200,
            crew=[
                CrewMember(
                    member_id="CM099",
                    name="Retired Ron",
                    rank=Rank.LIEUTENANT,
                    age=45,
                    specialization="Piloting",
                    years_experience=10,
                    is_active=False,
                ),
                CrewMember(
                    member_id="CM100",
                    name="New Nina",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Science",
                    years_experience=1,
                    is_active=True,
                ),
            ],
            mission_status="planned",
            budget_millions=150.0,
        )
    except ValidationError as e:
        for err in e.errors():
            print(Color.red(f"  - {err['msg'].replace('Value error, ', '')}"))

    print(sep)


if __name__ == "__main__":
    demonstrate()
