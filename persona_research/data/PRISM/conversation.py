from datasets import load_dataset
from dataclasses import dataclass, field
from typing import List

@dataclass
class Conversation:
    conversation_id: int
    user_id: int
    conversation_type: str
    opening_prompt: str
    conversation_turns: str
    conversation_history: str
    performance_attributes: str
    choice_attributes: str
    open_feedback: str
    generated_datetime: str
    timing_duration_s: int
    timing_duration_mins: float
    included_in_balanced_subset: bool