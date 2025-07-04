import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_MODEL = None 

if not GOOGLE_API_KEY:
    st.error("Google Gemini API key not found. Please check the .env file or Streamlit secrets.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    st.write(" ") 
    try:
        GEMINI_MODEL = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Failed to initialize gemini-1.5-flash model: {e}. AI functionalities will be disabled.")
        GEMINI_MODEL = None 




st.sidebar.title("Knowledge Navigator")
menu = st.sidebar.selectbox(
    "Choose a Feature",
    ["Home", "MCQ Generator", "PDF Q&A System", "CSV Visualization", "Research Bot", "Q&A Evaluator",
     "Study Plan Generator", "Interactive Quiz", "Concept Map Generator", "Topic Summary Generator"]
)

# Home page function
def home_page():
    st.title("Welcome to Knowledge Navigator")
    st.write("""
    Knowledge Navigator is your AI-powered educational assistant! It provides a range of tools for both students and teachers, 
    including MCQ generation, PDF-based Q&A generation, CSV data visualization, and personalized study plans.
    Here’s what you can do with Knowledge Navigator:
    - Generate MCQs from any text for effective revision.
    - Upload PDFs and get automated Q&A.
    - Visualize CSV data files easily.
    - Use the Research Bot to get answers to your academic queries.
    - Create personalized study plans and take interactive quizzes.
    """)
    st.write("Navigate to different features using the sidebar to explore the various functionalities.")

# Function to generate MCQs
def generate_mcqs(text, num_mcqs, subject):
    if not GEMINI_MODEL: 
        st.error("AI model not available. Please check API key configuration.")
        return None
    try:
        response = GEMINI_MODEL.generate_content(
            f"You are an expert MCQ maker. Generate {num_mcqs} MCQs on {subject} based on the following text: {text}"
        )
        return response.text
    except Exception as e:
        st.error(f"Error generating MCQs: {e}")
        return None

# Function to handle PDF Q&A
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text

def generate_qa_from_pdf(text):
    if not GEMINI_MODEL:
        st.error("AI model not available.")
        return None
    try:
        response = GEMINI_MODEL.generate_content(
            f"You are an expert question generator. Generate Q&A based on the following text: {text}"
        )
        return response.text
    except Exception as e:
        st.error(f"Error generating Q&A from PDF: {e}")
        return None

# Function to handle CSV Visualization
def visualize_csv(csv_file):
    df = pd.read_csv(csv_file)
    st.write(df)
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns.tolist()
    if numeric_columns:
        selected_columns = st.multiselect("Select columns to visualize", numeric_columns, default=numeric_columns)
        if selected_columns:
            st.line_chart(df[selected_columns])
        else:
            st.warning("Please select at least one numerical column.")
    else:
        st.error("No numerical columns found for visualization.")

# Function to simulate Research Bot
def research_bot_query(query):
    if not GEMINI_MODEL:
        st.error("AI model not available.")
        return None
    try:
        response = GEMINI_MODEL.generate_content(
            f"You are a research assistant. Answer this research question: {query}"
        )
        return response.text
    except Exception as e:
        st.error(f"Error with Research Bot: {e}")
        return None

# Function for Q&A Evaluator (Placeholder)
def qa_evaluator(file):
    st.write("Q&A Evaluator is under construction.")

# Function to generate personalized study plan
def study_plan_generator():
    st.title("Personalized Study Plan Generator")
    name = st.text_input("Name")
    study_hours = st.slider("How many hours can you study per day?", 1, 12, 3)
    subjects = st.multiselect("Select the subjects you want to study", 
                             ["Math", "Science", "History", "Language", "Arts"])
    deadline = st.date_input("Select the date of your next exam")

    if st.button("Generate Study Plan"):
        if not name or not subjects:
            st.error("Please enter all the details!")
        else:
            st.write(f"Study plan for {name} generated!")
            st.write(f"Study {study_hours} hours every day:")
            if not GEMINI_MODEL:
                st.error("AI model not available for detailed plan.")
                for subject in subjects:
                    st.write(f"- {subject}: {study_hours / len(subjects):.2f} hours per day (basic allocation)")
                return
            try:
                plan_prompt = f"Create a detailed study plan for {name} for the next few weeks, considering they can study {study_hours} hours per day, focusing on these subjects: {', '.join(subjects)}. The exam is on {deadline}. Allocate time wisely per subject."
                detailed_plan_response = GEMINI_MODEL.generate_content(plan_prompt)
                st.markdown(detailed_plan_response.text)
            except Exception as e:
                st.error(f"Could not generate detailed study plan: {e}")
                for subject in subjects:
                    st.write(f"- {subject}: {study_hours / len(subjects):.2f} hours per day (basic allocation)")


# Function for interactive quiz
def interactive_quiz():
    st.title("Interactive Quiz")

    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "correct": "Paris"},
        {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Tolkien", "Austen"], "correct": "Shakespeare"}
    ]
    
    score = 0
    if 'current_question_idx' not in st.session_state:
        st.session_state.current_question_idx = 0
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    current_idx = st.session_state.current_question_idx
    
    if current_idx < len(questions):
        q = questions[current_idx]
        st.subheader(f"Question {current_idx + 1}: {q['question']}")
        
        answer = st.radio(f"Options for question {current_idx + 1}", q["options"], key=f"q_{current_idx}_options")
        
        if st.button(f"Submit Answer for Question {current_idx + 1}", key=f"submit_q_{current_idx}"):
            if answer == q['correct']:
                st.success("Correct!")
                st.session_state.quiz_score += 1
            else:
                st.error(f"Wrong! Correct answer is {q['correct']}")
            st.session_state.current_question_idx += 1
            st.rerun() 
    else:
        st.write("Quiz completed!")
        st.write(f"Your total score: {st.session_state.quiz_score}/{len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.current_question_idx = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_submitted = False
            st.rerun()


# Function for concept map generation
def concept_map_generator():
    st.title("Concept Map Generator")
    concept = st.text_input("Enter a Topic (e.g., Photosynthesis)")
    
    generate_subtopics = st.checkbox("Let AI suggest subtopics?")
    
    subtopics_input = ""
    if generate_subtopics and concept:
        if not GEMINI_MODEL:
            st.error("AI model not available for subtopic suggestion.")
            subtopics_input = st.text_area("Enter Subtopics (comma-separated):", key="manual_subtopics_input")
        else:
            try:
                subtopic_prompt = f"Generate 5-7 key subtopics for the concept: '{concept}'. List them as a comma-separated string."
                subtopic_response = GEMINI_MODEL.generate_content(subtopic_prompt)
                subtopics_input = subtopic_response.text.strip()
                st.text_area("Suggested Subtopics (edit if needed):", value=subtopics_input, key="suggested_subtopics")
            except Exception as e:
                st.warning(f"Could not generate subtopics: {e}. Please enter manually.")
                subtopics_input = st.text_area("Enter Subtopics (comma-separated):", key="manual_subtopics_input")
    else:
        subtopics_input = st.text_area("Enter Subtopics (comma-separated):", key="manual_subtopics_input_no_ai")

    if st.button("Generate Concept Map"):
        if not concept or not subtopics_input:
            st.error("Please enter both topic and subtopics.")
        else:
            G = nx.Graph()
            subtopics_list = [s.strip() for s in subtopics_input.split(',') if s.strip()] # Clean and split
            
            G.add_node(concept)
            for sub in subtopics_list:
                G.add_edge(concept, sub)
            
            fig, ax = plt.subplots(figsize=(8, 6)) 
            pos = nx.spring_layout(G, k=0.8, iterations=50) 
            nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, node_size=2000, font_weight='bold', ax=ax)
            st.pyplot(fig) 

# Function to summarize text
def topic_summary_generator():
    st.title("Topic Summary Generator")
    text = st.text_area("Enter text for summary")
    if st.button("Generate Summary"):
        if text:
            if not GEMINI_MODEL:
                st.error("AI model not available.")
                return
            try:
                response = GEMINI_MODEL.generate_content(
                    f"You are an expert summarizer. Summarize the following text concisely: {text}"
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"Error generating summary: {e}")


# Choose feature based on sidebar menu
if menu == "Home":
    home_page()
elif menu == "MCQ Generator":
    st.header("Generate MCQs")
    text_input = st.text_area("Enter text for MCQ generation:")
    num_mcqs = st.slider("Number of MCQs", 1, 10, 5)
    subject = st.text_input("Subject")
    if st.button("Generate MCQs"):
        if text_input and subject:
            mcqs = generate_mcqs(text_input, num_mcqs, subject)
            if mcqs:
                st.subheader("Generated MCQs")
                st.write(mcqs)
        else:
            st.warning("Please enter text and subject.")
elif menu == "PDF Q&A System":
    st.header("Upload PDF for Q&A Generation")
    pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])
    if pdf_file:
        text = extract_text_from_pdf(pdf_file)
        if text:
            st.subheader("Generated Questions and Answers")
            qa = generate_qa_from_pdf(text)
            if qa:
                st.write(qa)
        else:
            st.error("Could not extract text from PDF.")
elif menu == "CSV Visualization":
    st.header("Upload CSV for Data Visualization")
    csv_file = st.file_uploader("Upload CSV file", type=["csv"])
    if csv_file:
        st.subheader("Data Visualization")
        try:
            visualize_csv(csv_file)
        except Exception as e:
            st.error(f"Error visualizing CSV: {e}")
elif menu == "Research Bot":
    st.header("Research Bot")
    query = st.text_input("Enter your research question:")
    if st.button("Get Research Answer"):
        if query:
            answer = research_bot_query(query)
            if answer:
                st.subheader("Research Bot Answer")
                st.write(answer)
        else:
            st.warning("Please enter a research question.")
elif menu == "Q&A Evaluator":
    st.header("Upload a file for Q&A Evaluation (PDF or Image)")
    file = st.file_uploader("Upload PDF or Image", type=["pdf", "jpg", "png"])
    if file:
        st.subheader("Evaluation Results")
        qa_evaluator(file)
elif menu == "Study Plan Generator":
    study_plan_generator()
elif menu == "Interactive Quiz":
    interactive_quiz()
elif menu == "Concept Map Generator":
    concept_map_generator()
elif menu == "Topic Summary Generator":
    topic_summary_generator()