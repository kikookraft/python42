"""Data Processor Foundation."""
from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid numeric data"
        s: float = sum(data)
        n: int = len(data)
        return f"Processed {n} numeric values, sum={s}, avg={s/n:.2f}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or not data:
            return False
        items: List[Any] = data  # type: ignore[assignment]
        for x in items:
            if not isinstance(x, (int, float)):
                return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid text data"
        c: int = len(data)
        w: int = len(data.split())
        return f"Processed text: {c} characters, {w} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid log data"
        if ":" in data:
            level: str = data.split(":")[0].strip()
            msg: str = ":".join(data.split(":")[1:]).strip()
            if level.upper() == "ERROR":
                return f"[ALERT] {level} level detected: {msg}"
            return f"[{level}] {level} level detected: {msg}"
        return f"[INFO] Log entry: {data}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    print("Initializing Numeric Processor...")
    np: DataProcessor = NumericProcessor()
    nd: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {nd}")
    if np.validate(nd):
        print("Validation: Numeric data verified")
    print(np.format_output(np.process(nd)))
    print()

    print("Initializing Text Processor...")
    tp: DataProcessor = TextProcessor()
    td: str = "Hello Nexus World"
    print(f'Processing data: "{td}"')
    if tp.validate(td):
        print("Validation: Text data verified")
    print(tp.format_output(tp.process(td)))
    print()

    print("Initializing Log Processor...")
    lp: DataProcessor = LogProcessor()
    ld: str = "ERROR: Connection timeout"
    print(f'Processing data: "{ld}"')
    if lp.validate(ld):
        print("Validation: Log entry verified")
    print(lp.format_output(lp.process(ld)))
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    procs: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
        NumericProcessor()
    ]
    data: List[Any] = [[1, 2, 3, 4],
                       "Test Message",
                       "INFO: System ready",
                       "bananaaaanaaana"
                       ]

    for i, (p, d) in enumerate(zip(procs, data), 1):
        print(f"Result {i}: {p.process(d)}")
    # all shit passing yay

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
