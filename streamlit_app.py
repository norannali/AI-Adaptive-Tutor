# streamlit_app.py
import streamlit as st
from adaptive_engine import AdaptiveEngine

# ---- Initialize Engine ----
@st.cache_resource
def load_engine():
    return AdaptiveEngine()

engine = load_engine()

# ---- UI Setup ----
st.set_page_config(page_title="AI Adaptive Tutor", layout="wide")
st.title("🎓 AI Adaptive Learning Tutor")
st.write("Interact with the adaptive AI engine powered by OpenRouter + Memory System")

# User Inputs
user_id = st.text_input("👤 User ID", value="student_01")

level = st.selectbox(
    "📚 Select User Level",
    ["beginner", "intermediate", "advanced"],
    index=0
)

# Update user level in memory
engine.memory.set_user_level(user_id, level)

question = st.text_area("💬 Enter your question")

# Generate response
if st.button("Generate Response"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("AI thinking..."):
            result = engine.process(user_id, question, level=level)  # pass selected level

        # AI Response
        st.subheader("🧠 AI Response")
        st.write(result["response"])

        # Metadata
        st.subheader("📊 Metadata")
        st.json(result["metadata"])

st.divider()

# Debug Memory
if st.checkbox("Show User Memory Debug"):
    st.subheader("🗂 User Memory Data")
    st.write(engine.memory.data)

if st.checkbox("Show Struggle Analysis Debug"):
    st.subheader("📊 Struggle Analysis")
    st.json(engine.struggle.data)
