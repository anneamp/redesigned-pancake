from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
class Turn(BaseModel):
    role: str
    content: str
class Trace(BaseModel):
    trace_id: str
    agent_type: str
    task_id: str
    context: Optional[str] = None
    turns: List[Turn]
    metadata: Dict[str, Any] = Field(default_factory=dict)
class Grade(BaseModel):
    grader: str
    score: float
    label: str
    rationale: str
    signals: Dict[str, Any] = Field(default_factory=dict)
class EvalResult(BaseModel):
    trace_id: str
    task_id: str
    agent_type: str
    grades: List[Grade]
    overall: float
    failure_modes: List[str]
