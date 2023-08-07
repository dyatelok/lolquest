from dataclasses import dataclass
from dataclasses import field
from typing import List

from omegaconf import MISSING


@dataclass
class TeamConfig:
    name: str = MISSING
    id: str = MISSING
    password: str = MISSING


@dataclass
class TaskScoringConfig:
    completed_before: float = MISSING
    percent: int = MISSING


@dataclass
class TaskConfig:
    id: str = MISSING
    name: str = MISSING
    code: str = MISSING
    max_points: int = MISSING
    scoring: List[TaskScoringConfig] = MISSING
    counts_towards_total_time: bool = True


@dataclass
class HintConfig:
    text: str = MISSING
    timing: float = MISSING


@dataclass
class StageConfig:
    name: str = MISSING
    duration: float = 2700
    tasks: List[TaskConfig] = MISSING
    hints: List[HintConfig] = field(default_factory=list)


@dataclass
class QuestConfig:
    teams: List[TeamConfig] = MISSING
    stages: List[StageConfig] = MISSING
