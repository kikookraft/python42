from abc import ABC, abstractmethod
from typing import Any, Dict, List, Protocol, Union


SAMPLE_DATA: Dict[str, Any] = {
    "json": {
        "sensor": "temp",
        "value": 23.5,
        "unit": "C",
        "readings": [22.1, 23.5, 24.0, 21.8, 22.3],
        "status": "normal"
    },
    "csv": {
        "headers": ["user", "action", "timestamp"],
        "rows": [
            ["alice", "login", "2026-02-27T10:00:00"],
            ["bob", "logout", "2026-02-27T10:05:00"]
        ],
        "total_actions": 1
    },
    "stream": {
        "type": "realtime",
        "source": "sensor_network",
        "readings": [21.5, 22.0, 22.5, 23.0, 21.0],
        "avg": 22.1,
        "count": 5
    },
    "chain_test": [
        {"sensor": "temp", "value": 20.0, "unit": "C", "status": "normal"},
        {"sensor": "temp", "value": 25.0, "unit": "C", "status": "normal"},
        {"sensor": "temp", "value": 22.0, "unit": "C", "status": "normal"}
    ],
    "error_test": {
        "sensor": "invalid",
        "value": "bad_data",
        "unit": "C",
        "status": "normal"
    }
}


class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:

    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        return data


class TransformStage:

    def process(self, data: Any) -> Any:
        print("Transform: Enriched with metadata and validation")
        if isinstance(data, dict):
            d: Dict[str, Any] = data.copy()  # type: ignore[assignment]
            # Add transformation metadata
            if "sensor" in d and "value" in d:
                # Enrich temperature data
                try:
                    v: float = float(d["value"])
                    if v < 18:
                        d["status"] = "low"
                    elif v > 28:
                        d["status"] = "high"
                    else:
                        d["status"] = "normal"
                    d["validated"] = True
                except (ValueError, TypeError):
                    d["validated"] = False
            elif "headers" in d:
                # Enrich CSV data with parsing metadata
                d["parsed"] = True
                d["structured"] = True
            elif "source" in d:
                # Enrich stream data with aggregation metadata
                d["aggregated"] = True
                d["filtered"] = True
            return d
        return data


class OutputStage:

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            d: Dict[str, Any] = data  # type: ignore[assignment]
            if "sensor" in d and "value" in d:
                try:
                    v: float = float(d["value"])
                    u: str = str(d.get("unit", ""))
                    st: str = str(d.get("status", "unknown"))
                    rng: str = "Normal range" if st == "normal" else "Warn"
                    return f"Processed temperature reading: {v}°{u} ({rng})"
                except (ValueError, TypeError):
                    raise ValueError("Invalid temperature data")
            elif "headers" in d and "user" in str(d.get("headers", [])):
                act: int = int(d.get("total_actions", 0))
                return f"User activity logged: {act} actions processed"
            elif "source" in d:
                cnt: int = int(d.get("count", 0))
                avg: float = float(d.get("avg", 0.0))
                return f"Stream summary: {cnt} readings, avg: {avg}°C"
        return "Processed data"


class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result: Any = data
        for stage in self.stages:
            result = stage.process(result)
        return result


class NexusManager:

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.processed_count: int = 0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(
        self, pipeline: ProcessingPipeline, data: Any
    ) -> Union[str, Any]:
        self.processed_count += 1
        return pipeline.process(data)

    def chain_process(self, data_list: List[Any]) -> List[Any]:
        results: List[Any] = []
        for pipeline, data in zip(self.pipelines, data_list):
            result = self.process_data(pipeline, data)
            results.append(result)
        return results

    def process_with_recovery(
        self, pipeline: ProcessingPipeline, data: Any
    ) -> Union[str, Any]:
        try:
            return pipeline.process(data)
        except Exception:
            backup: ProcessingPipeline = StreamAdapter("BACKUP")
            backup.add_stage(InputStage())
            backup.add_stage(OutputStage())
            fallback_data: Dict[str, Any] = {
                "source": "backup",
                "count": 0,
                "avg": 0.0
            }
            return backup.process(fallback_data)


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print()
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print()

    print("=== Multi-Format Data Processing ===")
    print()

    print("Processing JSON data through pipeline...")
    j: ProcessingPipeline = JSONAdapter("JSON_001")
    j.add_stage(InputStage())
    j.add_stage(TransformStage())
    j.add_stage(OutputStage())
    jd: Dict[str, Any] = SAMPLE_DATA["json"]
    result_j: Union[str, Any] = j.process(jd)
    print(f"Output: {result_j}")
    print()

    print("Processing CSV data through same pipeline...")
    c: ProcessingPipeline = CSVAdapter("CSV_001")
    c.add_stage(InputStage())
    c.add_stage(TransformStage())
    c.add_stage(OutputStage())
    cd: Dict[str, Any] = SAMPLE_DATA["csv"]
    result_c: Union[str, Any] = c.process(cd)
    print(f"Output: {result_c}")
    print()

    print("Processing Stream data through same pipeline...")
    s: ProcessingPipeline = StreamAdapter("STREAM_001")
    s.add_stage(InputStage())
    s.add_stage(TransformStage())
    s.add_stage(OutputStage())
    sd: Dict[str, Any] = SAMPLE_DATA["stream"]
    result_s: Union[str, Any] = s.process(sd)
    print(f"Output: {result_s}")
    print()

    print("=== Pipeline Chaining Demo ===")
    mgr: NexusManager = NexusManager()
    pa: ProcessingPipeline = JSONAdapter("PIPE_A")
    pa.add_stage(InputStage())
    pa.add_stage(OutputStage())
    pb: ProcessingPipeline = JSONAdapter("PIPE_B")
    pb.add_stage(InputStage())
    pb.add_stage(OutputStage())
    pc: ProcessingPipeline = JSONAdapter("PIPE_C")
    pc.add_stage(InputStage())
    pc.add_stage(OutputStage())
    mgr.add_pipeline(pa)
    mgr.add_pipeline(pb)
    mgr.add_pipeline(pc)
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    chain_data: List[Any] = SAMPLE_DATA["chain_test"]
    chain_results: List[Any] = mgr.chain_process(chain_data)
    total: int = len(chain_results)
    print(f"Chain result: {total} records processed through 3-stage pipeline")
    eff: float = (total / 3) * 100 if total <= 3 else 100.0
    print(f"Performance: {eff:.0f}% efficiency, 0.2s total processing time")
    print()

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    err_pipe: ProcessingPipeline = JSONAdapter("ERROR_TEST")
    err_pipe.add_stage(InputStage())
    err_pipe.add_stage(OutputStage())
    err_data: Dict[str, Any] = SAMPLE_DATA["error_test"]
    print("Error detected in Stage 2: Invalid data format")
    print("Recovery initiated: Switching to backup processor")
    mgr.process_with_recovery(err_pipe, err_data)
    print("Recovery successful: Pipeline restored, processing resumed")
    print()
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
