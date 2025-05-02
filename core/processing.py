# core/processing.py
# import nltk # Uncomment if using NLTK
# import spacy # Uncomment if using spaCy
# from collections import Counter # Uncomment if using simple frequency
import time # Required for the sleep function
from typing import List

class TextProcessor:
    """Handles basic text processing tasks."""
    def preprocess(self, text: str) -> str:
        # Placeholder: Add cleaning steps later (e.g., remove extra whitespace)
        print("Preprocessing text...")
        return text.strip()

class SimpleConceptExtractor:
    """Extracts key concepts using basic methods (non-LLM baseline)."""
    def __init__(self, method: str = "split"):
         self.method = method
         # if method == "spacy":
         #    self.nlp = spacy.load("en_core_web_sm") # Load model if needed
         print(f"Initializing SimpleConceptExtractor with method: {method}")


    def extract(self, text: str, num_concepts: int = 5) -> List[str]:
        print(f"Extracting concepts using method: {self.method}...")
        if not text:
            return []

        if self.method == "split":
            # Very naive baseline
            words = [word.strip('.,!?;:"()[]') for word in text.lower().split() if len(word) > 3]
            # Add stopword removal if using nltk/spacy
            # Example: Filter common words
            stopwords_basic = {"the", "a", "an", "is", "are", "in", "on", "it", "of", "and", "to", "for"}
            meaningful_words = [word for word in words if word not in stopwords_basic]
            # Get most frequent
            # word_counts = Counter(meaningful_words)
            # common_concepts = [word for word, count in word_counts.most_common(num_concepts)]
            # Just return first few unique for simplicity now
            unique_words = list(dict.fromkeys(meaningful_words))
            return unique_words[:num_concepts]

        elif self.method == "nltk":
             # TODO: Implement NLTK noun phrase chunking or keyword extraction
             pass
             return ["NLTK_concept_1", "NLTK_concept_2"] # Placeholder

        elif self.method == "spacy":
             # TODO: Implement spaCy noun chunk or named entity extraction
             # doc = self.nlp(text)
             # concepts = [chunk.text for chunk in doc.noun_chunks]
             # return concepts[:num_concepts]
             return ["spaCy_concept_1", "spaCy_concept_2"] # Placeholder

        else:
            return []

# --- Placeholder for future LLM integration ---
class LLMProcessor: # Replace with more specific classes later
    def simplify(self, text:str) -> str:
         # This will eventually call the fine-tuned model
         print("SIMULATING LLM Simplification...")
         time.sleep(0.5) # Simulate network/compute time
         return f"LLM Simplified: {text[:70]}..."

    def explain_concept(self, concept: str, context: str) -> str:
        # This will call the fine-tuned model
        print(f"SIMULATING LLM Explanation for '{concept}'...")
        time.sleep(0.3)
        return f"LLM Explanation: '{concept}' is an important topic within the context..."