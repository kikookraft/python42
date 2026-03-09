import os
import sys
import importlib
import urllib.request
import json
import re
from datetime import datetime, timezone
from typing import Any
import datetime as _dt

# ========== Dependency check ==========

REQUIRED: dict[str, str] = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "requests": "requests",
}

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")
_missing: list[str] = []
for _pkg, _import_name in REQUIRED.items():
    try:
        _mod = importlib.import_module(_import_name)
        _ver = getattr(_mod, "__version__", "unknown")
        print(f"  [OK] {_pkg} ({_ver}) - ", end="")
        if _pkg == "pandas":
            print("Data manipulation ready")
        elif _pkg == "numpy":
            print("Numerical computation ready")
        elif _pkg == "matplotlib":
            print("Visualization ready")
        elif _pkg == "requests":
            print("Network access ready")
    except ImportError:
        print(f"  [MISSING] {_pkg}")
        _missing.append(_pkg)

if _missing:
    print("\nMissing dependencies detected!")
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print("Install with Poetry:")
    print("  poetry install")
    sys.exit(1)
else:
    print("All dependencies are satisfied. Proceeding with execution...\n")
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

BASE_URL: str = "https://api.raraph.fr/intra-metrics/sessions"


# ---------- SESSION CLASS ----------

class Session:
    """Represents a single user session."""

    def __init__(
        self, host: str, start_ms: int, end_ms: int | None
    ) -> None:
        self.host: str = host
        self._start_ms: int = start_ms
        self._end_ms: int | None = end_ms

    def is_complete(self) -> bool:
        """Return True if session has end time."""
        return self._end_ms is not None

    def start_time(self) -> datetime:
        """Return session start time as UTC datetime."""
        return datetime.fromtimestamp(
            self._start_ms / 1000, tz=timezone.utc
        )

    def end_time(self) -> datetime | None:
        """Return session end time, or None if still active."""
        if self._end_ms is None:
            return None
        return datetime.fromtimestamp(
            self._end_ms / 1000, tz=timezone.utc
        )

    def duration_minutes(self) -> float | None:
        """Return session duration in minutes, or None
        if still active."""
        if self._end_ms is None:
            return None
        return (self._end_ms - self._start_ms) / 1000 / 60

    def __repr__(self) -> str:
        end: datetime | None = self.end_time()
        dur: float | None = self.duration_minutes()
        return (
            f"Session(host={self.host!r}, "
            f"start={self.start_time().strftime('%H:%M:%S UTC')}, "
            f"end={end.strftime('%H:%M:%S UTC') if end else 'active'}, "
            f"duration={f'{dur:.1f} min' if dur is not None else 'N/A'})"
        )

    @classmethod
    def fetch_all(cls, url: str = BASE_URL) -> list["Session"]:
        """Fetch all sessions from URL."""
        with urllib.request.urlopen(url) as response:
            data: Any = json.loads(response.read())
        return [
            cls(s["host"], s["startTime"], s["endTime"])
            for s in data["sessions"]
        ]

    @staticmethod
    def avg_by_interval(
        sessions: list["Session"],
        interval_minutes: int = 1,
    ) -> pd.DataFrame:
        """
        calculate the average number of sessions each minute
        """

        # get only complete sesions
        complete: list[Session] = [s for s in sessions if s.is_complete()]
        if not complete:
            return pd.DataFrame(columns=["interval", "avg_count"])

        # prepare rows for counting
        rows: list[dict[str, object]] = []
        for s in complete:
            start: datetime = s.start_time().replace(tzinfo=None)
            end: datetime | None = s.end_time()
            assert end is not None  # should be complete sessions only
            end = end.replace(tzinfo=None)

            start_day: datetime = start.replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            start_min = int((start - start_day).total_seconds() // 60)
            end_min_abs = int((end - start_day).total_seconds() // 60)

            # align to interval
            first_slot: int = (
                start_min // interval_minutes) * interval_minutes
            for slot_abs in np.arange(
                first_slot, end_min_abs, interval_minutes, dtype=int
            ):
                # dark magic this is copy pasted
                day_offset: int = int(slot_abs) // 1440
                slot_in_day: int = int(slot_abs) % 1440
                day: _dt.date = (
                    start_day + _dt.timedelta(days=day_offset)
                ).date()
                rows.append({"date": day, "slot": slot_in_day})

        df = pd.DataFrame(rows)

        counts = (
            df.groupby(["date", "slot"])  # type: ignore[call-overload]
            .size()
            .reset_index(name="count")
        )

        # calculate average per slot
        num_days: int = counts["date"].nunique()
        agg = (
            counts.groupby("slot")["count"]  # type: ignore[call-overload]
            .sum()
            .reset_index(name="total")
        )
        agg["avg_count"] = agg["total"] / num_days

        all_slots = pd.DataFrame(
            {"slot": range(0, 1440, interval_minutes)}
        )
        agg = (
            all_slots.merge(  # type: ignore[call-overload]
                agg[["slot", "avg_count"]], on="slot", how="left"
            ).fillna(0)  # type: ignore[call-overload]
        )

        base: datetime = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        def _slot_to_datetime(minutes: int) -> datetime:
            return base.replace(hour=minutes // 60, minute=minutes % 60)

        agg["interval"] = pd.to_datetime(
            agg["slot"].apply(_slot_to_datetime)  # type: ignore[call-overload]
        )
        return agg[["interval", "avg_count"]]


# ---------- PLOTS ----------

def plot_average_concurrent(
    sessions: list[Session], output_path: str = "matrix_analysis.png"
) -> None:
    """Plot average concurrent sessions and save to file."""
    df = Session.avg_by_interval(
        sessions, interval_minutes=1)

    fig, ax = plt.subplots(figsize=(14, 5))  # type: ignore[call-overload]

    ax.plot(  # type: ignore[call-overload]
        df["interval"],
        df["avg_count"],
        color="#4c9be8",
        linewidth=1.2,
    )

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    fig.autofmt_xdate(rotation=45)

    ax.set_xlabel(  # type: ignore[call-overload]
        "Time of day (1-min intervals)", fontsize=12
    )
    ax.set_ylabel(  # type: ignore[call-overload]
        "Avg concurrent sessions", fontsize=12
    )
    ax.set_title(  # type: ignore[call-overload]
        "Average Session Count over a day",
        fontsize=14,
    )
    ax.grid(axis="y", linestyle="--", alpha=0.5)  # type: ignore[call-overload]

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)  # type: ignore[call-overload]
    print(f"Results saved to: {output_path}")
    plt.show()  # type: ignore[call-overload]
    plt.close()


# ---------- PACKAGE MANAGER COMPARISON ----------

def _parse_requirements_txt(path: str) -> dict[str, str]:
    """Parse requirements.txt into {package: pinned_version}."""
    result: dict[str, str] = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                # get only packages versions
                m = re.match(r"^([A-Za-z0-9_\-]+)==(.+)$", line)
                if m:
                    result[m.group(1).lower()] = m.group(2)
    except FileNotFoundError:
        pass
    return result


def _parse_pyproject_toml(path: str) -> dict[str, str]:
    """Parse [tool.poetry.dependencies] from pyproject.toml."""
    result: dict[str, str] = {}
    try:
        with open(path) as f:
            in_deps = False
            for line in f:
                line: str = line.strip()
                if line == "[tool.poetry.dependencies]":
                    in_deps = True
                    continue
                if in_deps:
                    if line.startswith("["):
                        break
                    m = re.match(r'^([A-Za-z0-9_\-]+)\s*=\s*"(.+)"$', line)
                    if m and m.group(1).lower() != "python":
                        result[m.group(1).lower()] = m.group(2)
    except FileNotFoundError:
        pass
    return result


def compare_package_managers(base_dir: str = ".") -> None:
    """Print a comparison of pip vs Poetry"""
    pip_deps: dict[str, str] = _parse_requirements_txt(
        os.path.join(base_dir, "requirements.txt")
    )
    poetry_deps: dict[str, str] = _parse_pyproject_toml(
        os.path.join(base_dir, "pyproject.toml")
    )
    all_pkgs: list[str] = sorted(set(pip_deps) | set(poetry_deps))

    print("\n--- Package Manager Comparison ---")
    print(f"  {'Package':<14} {'Installed':<12}"
          f" {'pip (pinned)':<16} {'Poetry (range)'}")
    print(f"  {'-'*14} {'-'*12} {'-'*16} {'-'*16}")
    for pkg in all_pkgs:
        try:
            mod = importlib.import_module(pkg)
            installed: Any | str = getattr(mod, "__version__", "unknown")
        except ImportError:
            installed = "NOT INSTALLED"
        pip_ver: str = pip_deps.get(pkg, "—")
        poetry_ver: str = poetry_deps.get(pkg, "—")
        print(
            f"  {pkg:<14} {installed:<12} {pip_ver:<16} {poetry_ver}"
        )


if __name__ == "__main__":
    venv: str | None = os.environ.get("VIRTUAL_ENV")

    if venv:
        print(f"Running in virtual environment: {venv}")
    else:
        print(
            "WARNING: Not running in a virtual environment. "
            "It's recommended to use one to manage dependencies.\n"
        )
        print(
            "To create and activate a virtual environment, run:\n"
            "\033[95m  py -m venv .venv\n"
            "\033[95m  source .venv/bin/activate.fish\033[00m\n"
            "then :\n"
            "\033[93m  poetry install && poetry run python loading.py\033[00m"
            "\nor\n"
            "\033[93m  pip install -r requirements.txt && "
            "py loading.py\033[00m"
        )

    _script_dir: str = os.path.dirname(os.path.abspath(__file__))
    compare_package_managers(_script_dir)

    OUTPUT = "matrix_analysis.png"

    print("\nAnalyzing Matrix data...")
    sessions: list[Session] = Session.fetch_all()
    total: int = len(sessions)
    complete: int = sum(1 for s in sessions if s.is_complete())
    print(f"Processing {total} data points...")
    print(
        f"  {complete} complete sessions, "
        f"{total - complete} still active (excluded from analysis)"
    )

    print("Generating visualization...")

    plot_average_concurrent(sessions, output_path=OUTPUT)
    print("Analysis complete!")
