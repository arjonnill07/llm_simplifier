# core/models.py
from dataclasses import dataclass # Or use regular class
from typing import Union, List, Dict, Optional

@dataclass
class InputText:
    """Represents the raw input text."""
    text: str

@dataclass
class AnalysisResult:
    """Holds the results of the analysis."""
    original_text: str
    simplified_text: Optional[str] = None
    key_concepts: Optional[List[str]] = None
    explanations: Optional[Dict[str, str]] = None # Concept -> Explanation