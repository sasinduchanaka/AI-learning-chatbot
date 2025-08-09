import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
    temperature=0.5
)

# Functions
def generate_learning_roadmap(topic):
    prompt = f"""
    You're an expert teacher. Generate a learning roadmap for '{topic}'.
    Include 5-7 stages, subtopics, and practical tips.
    """
    return llm.invoke(prompt).content

def search_learning_resources(topic):
    return f"""
    🔗 YouTube: https://www.youtube.com/results?search_query={topic.replace(' ', '+')}
    🔗 GitHub: https://github.com/search?q={topic.replace(' ', '+')}
    """

def generate_quiz(topic, difficulty="medium", num_questions=5):
    prompt = f"""
    Create a {difficulty} quiz on '{topic}' with {num_questions} multiple-choice questions.
    Provide 4 options and mark the correct answer.
    """
    return llm.invoke(prompt).content

# Streamlit UI
st.title("🧠 AI Learning Assistant")
topic = st.text_input("Enter topic:")

if st.button("Generate Roadmap"):
    st.markdown(generate_learning_roadmap(topic))

if st.button("Find Learning Resources"):
    st.markdown(search_learning_resources(topic))

if st.button("Generate Quiz"):
    difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"])
    num_q = st.slider("Number of Questions", 1, 10, 5)
    st.markdown(generate_quiz(topic, difficulty, num_q))
