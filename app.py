# app.py
import streamlit as st
# Import your classes later
# from core.models import InputText
# from core.processing import TextProcessor, SimpleConceptExtractor # Example name
from core.models import InputText, AnalysisResult
from core.processing import TextProcessor, SimpleConceptExtractor, LLMProcessor # Add LLMProcessor
# --- Page Configuration (Optional but Recommended) ---
st.set_page_config(
    page_title="Content Simplifier & Explainer",
    page_icon="🧠",
    layout="wide"
)

# --- Sidebar (Optional - for settings later) ---
# st.sidebar.header("Settings")
# target_level = st.sidebar.selectbox("Target Reading Level:", ["High School", "Middle School", "Elementary"])

# --- Main Application Area ---
st.title("Personalized Educational Content Simplifier & Explainer 📚✨")
st.markdown("Enter text below to get a simplified version, key concepts, and explanations.")

# --- Input Area ---
input_text_area = st.text_area("Paste your text here:", height=250, placeholder="Enter the text you want to process...")

# --- Action Button ---
analyze_button = st.button("Analyze Text", type="primary")

# --- Output Area ---
st.divider() # Visual separator

col1, col2 = st.columns(2) # Create two columns for side-by-side display

with col1:
    st.subheader("Simplified Text")
    simplified_output_area = st.container(border=True) # Use container for visual grouping
    simplified_output_area.markdown("*(Simplified text will appear here after analysis...)*")


with col2:
    st.subheader("Key Concepts")
    concepts_output_area = st.container(border=True)
    concepts_output_area.markdown("*(Key concepts will be listed here...)*")

    st.subheader("Explanations")
    explanations_output_area = st.container(border=True)
    explanations_output_area.markdown("*(Explanations for key concepts will appear here...)*")


# --- Processing Logic ---
if analyze_button:
    if input_text_area:
        # 1. Instantiate InputText
        input_data = InputText(text=input_text_area)
        st.toast(f"Processing text ({len(input_data.text)} characters)...", icon="⏳")
        print(f"Received text: {input_data.text[:100]}...") # For debugging in console

        # 2. Instantiate Processors
        text_processor = TextProcessor()
        # Use the simple baseline extractor for now
        concept_extractor = SimpleConceptExtractor(method="split") # Or "nltk"/"spacy" if implemented
        llm_processor = LLMProcessor() # Instantiate the placeholder LLM processor

        # 3. Perform Processing Steps
        processed_text = text_processor.preprocess(input_data.text)
        key_concepts = concept_extractor.extract(processed_text, num_concepts=5)

        # --- Simulate LLM Actions (Replace with real calls later) ---
        simplified_text_result = llm_processor.simplify(processed_text)
        explanations_result = {}
        if key_concepts:
            # Explain only the first concept for now to avoid too many simulated calls
            first_concept = key_concepts[0]
            explanations_result[first_concept] = llm_processor.explain_concept(
                concept=first_concept,
                context=processed_text # Pass context to the explainer
            )

        # 4. Store results (optional but good practice)
        results = AnalysisResult(
            original_text=input_data.text,
            simplified_text=simplified_text_result,
            key_concepts=key_concepts,
            explanations=explanations_result
        )

        # --- Update Output Areas (Using results object) ---
        simplified_output_area.markdown(results.simplified_text if results.simplified_text else "_Not available_")

        if results.key_concepts:
            concepts_output_area.markdown("Found concepts:")
            for concept in results.key_concepts:
                 concepts_output_area.markdown(f"- `{concept}`")
        else:
             concepts_output_area.markdown("_No key concepts extracted._")

        if results.explanations:
            explanations_output_area.markdown("Explanations:")
            for concept, explanation in results.explanations.items():
                explanations_output_area.markdown(f"**{concept}:** {explanation}")
        else:
             explanations_output_area.markdown("_No explanations generated._")


        st.toast("Analysis complete!", icon="✅")

    else:
        st.warning("Please enter some text to analyze.")

# --- Footer (Optional) ---
st.markdown("---")
st.caption("Built with Streamlit and 🧠 by [Your Name]")