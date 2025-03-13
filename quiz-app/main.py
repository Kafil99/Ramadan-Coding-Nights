import streamlit as st
import random
import time
from datetime import datetime

# Constants
QUIZ_TIME_LIMIT = 30  # seconds per question
TOTAL_QUESTIONS = 5    # questions per complete quiz

# Initialize session state 
if 'quiz_active' not in st.session_state:
    st.session_state.update({
        'quiz_active': True,
        'questions': None,
        'current_question': 0,  # Initialize to 0 instead of None
        'score': {'correct': 0, 'incorrect': 0},
        'start_time': None,
        'answered_questions': []
    })

# Configure page
st.set_page_config(page_title="🧠 General Knowledge Quiz", page_icon="📚")
st.title("🧠 Test Your General Knowledge")
st.markdown("---")

def initialize_quiz():
    """Reset quiz to initial state"""
    all_questions = [
        {
            "question": "What is the capital of Pakistan?",
            "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
            "answer": "Islamabad",
        },
        {
            "question": "Who is the founder of Pakistan?",
            "options": ["Allama Iqbal", "Liaquat Ali Khan", 
                       "Muhammad Ali Jinnah", "Benazir Bhutto"],
            "answer": "Muhammad Ali Jinnah",
        },
        {
            "question": "Which is the national language of Pakistan?",
            "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
            "answer": "Urdu",
        },
        {
            "question": "What is the currency of Pakistan?",
            "options": ["Rupee", "Dollar", "Taka", "Riyal"],
            "answer": "Rupee",
        },
        {
            "question": "Which city is known as the City of Lights in Pakistan?",
            "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
            "answer": "Karachi",
        },
    ]
    st.session_state.questions = random.sample(all_questions, TOTAL_QUESTIONS)
    st.session_state.current_question = 0
    st.session_state.score = {'correct': 0, 'incorrect': 0}
    st.session_state.answered_questions = []
    st.session_state.start_time = time.time()
    st.session_state.quiz_active = True

def handle_answer(selected_option):
    """Process user answer and update state"""
    question = st.session_state.questions[st.session_state.current_question]
    elapsed_time = time.time() - st.session_state.start_time
    
    result = {
        'question': question['question'],
        'user_answer': selected_option,
        'correct_answer': question['answer'],
        'time_taken': elapsed_time,
        'is_correct': selected_option == question['answer']
    }
    
    if result['is_correct']:
        st.session_state.score['correct'] += 1
    else:
        st.session_state.score['incorrect'] += 1
    
    st.session_state.answered_questions.append(result)
    
    if st.session_state.current_question < TOTAL_QUESTIONS - 1:
        st.session_state.current_question += 1
        st.session_state.start_time = time.time()
    else:
        st.session_state.quiz_active = False

# Ensure quiz is initialized on first run
if st.session_state.questions is None:
    initialize_quiz()

# Sidebar for controls and statistics
with st.sidebar:
    st.header("Quiz Controls")
    if st.button("🔄 Restart Quiz"):
        initialize_quiz()
    
    st.markdown("---")
    st.header("Statistics")
    if st.session_state.quiz_active:
        st.metric("Current Question", 
                 f"{st.session_state.current_question + 1}/{TOTAL_QUESTIONS}")
    st.metric("✅ Correct Answers", st.session_state.score['correct'])
    st.metric("❌ Incorrect Answers", st.session_state.score['incorrect'])

# Main quiz interface
if not st.session_state.quiz_active:
    # Show final results
    st.balloons()
    st.header("🎉 Quiz Complete!")
    st.subheader("Final Score")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Correct", st.session_state.score['correct'])
    with col2:
        st.metric("Total Incorrect", st.session_state.score['incorrect'])
    
    st.markdown("---")
    st.subheader("Question Review")
    for idx, result in enumerate(st.session_state.answered_questions):
        with st.expander(f"Question {idx + 1}: {result['question']}"):
            st.markdown(f"**Your Answer:** {'✅' if result['is_correct'] else '❌'} {result['user_answer']}")
            st.markdown(f"**Correct Answer:** {result['correct_answer']}")
            st.caption(f"Time taken: {result['time_taken']:.1f} seconds")
    
    if st.button("🏁 Play Again"):
        initialize_quiz()
else:
    # Show current question
    question = st.session_state.questions[st.session_state.current_question]
    
    # Timer display
    elapsed_time = time.time() - st.session_state.start_time
    time_remaining = max(QUIZ_TIME_LIMIT - elapsed_time, 0)
    progress = time_remaining / QUIZ_TIME_LIMIT
    
    time_col, score_col = st.columns([2, 1])
    with time_col:
        st.markdown(f"⏳ Time Remaining: **{time_remaining:.1f}s**")
        st.progress(progress)
    
    with score_col:
        st.markdown(f"🏅 **Score:** {st.session_state.score['correct'] * 10} points")
    
    st.markdown("---")
    st.subheader(f"Question {st.session_state.current_question + 1}")
    st.markdown(f"### {question['question']}")
    
    selected = st.radio("Select your answer:", 
                        question['options'], 
                        key=f"q{st.session_state.current_question}")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🚩 Submit Answer"):
            handle_answer(selected)
            st.rerun()
    
    # Automatic timeout handling
    if elapsed_time >= QUIZ_TIME_LIMIT:
        handle_answer("")
        st.rerun()

st.markdown("---")
st.caption("Developed with ❤️ by [Your Name] | 📧 contact@example.com")