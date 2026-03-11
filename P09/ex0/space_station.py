from datetime import datetime
from pydantic import BaseModel, Field


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=0, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)  # datetime field
    is_operational: bool = True  # default to True
    notes: str = Field(default="", max_length=200)  # optional, max 200 char

    def show(self) -> str:
        op: str = (
                    f"{Color.GREEN}Yes{Color.RESET}"
                    if self.is_operational
                    else f"{Color.RED}No{Color.RESET}")
        return (f"Station ID: {Color.GREEN}"
                f"{self.station_id}{Color.RESET}\n"
                f"Name: {Color.BLUE}{self.name}{Color.RESET}\n"
                f"Crew Size: {Color.YELLOW}{self.crew_size}{Color.RESET}\n"
                f"Power Level: {Color.GREEN}{self.power_level}%{Color.RESET}\n"
                f"Oxygen Level: {Color.CYAN}{self.oxygen_level}%"
                f"{Color.RESET}\n"
                f"Last Maintenance: {Color.MAGENTA}"
                f"{self.last_maintenance.strftime('%Y-%m-%d %H:%M')}"
                f"{Color.RESET}\n"
                f"Operational: {op}\n"
                f"Notes: {self.notes}")


def main() -> None:
    good_station = SpaceStation(
        station_id="CRU-L5",
        name="Crusader L5 Ambitious DreamStation",
        crew_size=5,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-05-20T14:30:00",
        is_operational=True,
        notes="Refinery Job completed."
    )
    print(good_station.show())
    try:
        bad_station = SpaceStation(
            station_id="SERAPHIM STATION",  # too long
            name="",  # too short
            crew_size=500,  # too high
            power_level=150.0,  # too high
            oxygen_level=-10.0,  # too low
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=True,
            notes="Party at space shulter tonight!"
        )
        print(bad_station.show())
    except Exception as e:
        print(f"Error creating bad station: {Color.RED}{e}{Color.RESET}")


if __name__ == "__main__":
    main()
