from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [d for d in data_batch if criteria in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "processed": self.processed}


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed += len(data_batch)
        temps: List[float] = []
        for d in data_batch:
            if isinstance(d, str) and d.startswith("temp:"):
                try:
                    temps.append(float(d.split(":")[1]))
                except ValueError:
                    pass
        avg: float = sum(temps) / len(temps) if temps else 0.0
        return f"{len(data_batch)} readings processed, avg temp: {avg}.C"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [d for d in data_batch if "temp:" in str(d)]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, str | int | float] = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed += len(data_batch)
        net: int = 0
        for d in data_batch:
            if isinstance(d, str):
                if d.startswith("buy:"):
                    try:
                        net += int(d.split(":")[1])
                    except ValueError:
                        pass
                elif d.startswith("sell:"):
                    try:
                        net -= int(d.split(":")[1])
                    except ValueError:
                        pass
        sign: str = "+" if net >= 0 else ""
        return f"{len(data_batch)} operations, net flow: {sign}{net} units"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            result: List[Any] = []
            for d in data_batch:
                if isinstance(d, str) and ":" in d:
                    try:
                        val = int(d.split(":")[1])
                        if val >= 100:
                            result.append(d)
                    except ValueError:
                        pass
            return result
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed += len(data_batch)
        errors: int = sum(1 for d in data_batch if d == "error")
        return f"{len(data_batch)} events, {errors} error detected"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "errors":
            return [d for d in data_batch if d == "error"]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = self.stream_type
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            try:
                results.append(stream.process_batch(batch))
            except Exception:
                results.append("Processing error")
        return results

    def filter_all(
        self, batches: List[List[Any]], criteria: Optional[str] = None
    ) -> List[List[Any]]:
        results: List[List[Any]] = []
        for stream, batch in zip(self.streams, batches):
            results.append(stream.filter_data(batch, criteria))
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    ss: DataStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {ss.stream_id}, Type: Environmental Data")
    sb: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sb}")
    print(f"Sensor analysis: {ss.process_batch(sb)}")
    print()

    print("Initializing Transaction Stream...")
    ts: DataStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {ts.stream_id}, Type: Financial Data")
    tb: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {tb}")
    print(f"Transaction analysis: {ts.process_batch(tb)}")
    print()

    print("Initializing Event Stream...")
    es: DataStream = EventStream("EVENT_001")
    print(f"Stream ID: {es.stream_id}, Type: System Events")
    eb: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {eb}")
    print(f"Event analysis: {es.process_batch(eb)}")
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    proc: StreamProcessor = StreamProcessor()
    proc.add_stream(SensorStream("S1"))
    proc.add_stream(TransactionStream("T1"))
    proc.add_stream(EventStream("E1"))

    batches: List[List[str]] = [
        ["temp:25", "temp:30"],
        ["buy:50", "sell:200", "buy:10", "sell:40"],
        ["login", "error", "logout"]
    ]

    print("Batch 1 Results:")
    results: List[str] = proc.process_all(batches)
    print(f"- Sensor data: {results[0]}")
    print(f"- Transaction data: {results[1]}")
    print(f"- Event data: {results[2]}")
    print()

    print("Stream filtering active: High-priority data only")
    sensor_f: List[Any] = proc.streams[0].filter_data(
        ["temp:99", "humidity:50", "temp:100"], "critical"
    )
    trans_f: List[Any] = proc.streams[1].filter_data(
        ["buy:150", "sell:50", "buy:200"], "large"
    )
    print(f"Filtered results: {len(sensor_f)} critical sensor alerts, "
          f"{len(trans_f)} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
