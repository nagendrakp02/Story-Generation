import streamlit as st
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Story Generator", layout="centered")
st.title("📖 AI Story Generator")

topic = st.text_input("Enter Story Topic")
language = st.text_input("Enter Language (optional)", value="english")

if st.button("Generate Story"):
    if not topic:
        st.warning("Please enter a topic!")
    else:
        try:
            llm = GroqLLM(groq_api_key).get_llm()
            graph_builder = GraphBuilder(llm)

            if language and language.lower() != "english":
                graph = graph_builder.setup_graph("language")
                state = graph.invoke({"topic": topic, "current_language": language.lower()})
            else:
                graph = graph_builder.setup_graph("topic")
                state = graph.invoke({"topic": topic})

            st.success("✅ Story generated!")
            st.subheader(state["story"].title)
            st.markdown(state["story"].content)

        except Exception as e:
            st.error(f"❌ Error: {e}")
