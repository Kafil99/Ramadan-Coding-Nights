import streamlit as st
import random
import time
import requests

st.title("💸 Money Making Machine")

# Function to generate a random cash amount
def generate_money():
    return random.randint(10, 1000)

# Fallback side hustles and quotes
fallback_hustles = [
    "Freelancing", "Dropshipping", "Affiliate Marketing", "Print-on-Demand Store", "Blogging"
]

fallback_quotes = [
    "Success is not about money, it's about freedom.",
    "Don’t stay in bed unless you can make money in bed.",
    "Opportunities don't happen, you create them.",
    "Money grows on the tree of persistence.",
    "The best investment you can make is in yourself."
]

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", random.choice(fallback_hustles))
        else:
            return f"Failed to fetch hustles. Status code: {response.status_code}"
    except Exception:
        return random.choice(fallback_hustles)

# Function to fetch money quotes
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", random.choice(fallback_quotes))
        else:
            return f"Failed to fetch quote. Status code: {response.status_code}"
    except Exception:
        return random.choice(fallback_quotes)

# Instant Cash Generator
st.subheader("🪙 Instant Cash Generator")
if st.button("Generate Money 💰"):
    with st.spinner("Counting your money..."):
        time.sleep(2)
        amount = generate_money()
    st.success(f"You made ${amount}! 🎉")

# Side Hustle Ideas
st.subheader("📈 Side Hustle Ideas")
if st.button("Generate Hustle 🏃"):
    with st.spinner("Finding your side hustle..."):
        idea = fetch_side_hustle()
    st.success(idea)

# Money-Making Motivation
st.subheader("📚 Money-Making Motivation")
if st.button("Get Inspired ✨"):
    with st.spinner("Fetching inspiration..."):
        quote = fetch_money_quote()
    st.info(quote)

st.markdown("---")
st.markdown(
    "**Tip:** Make sure your backend server is running at `http://127.0.0.1:8000`. If not, fallback side hustles and quotes will be used! 🚀"
)

