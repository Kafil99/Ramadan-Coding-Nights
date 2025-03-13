import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date" , "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date , mood):
    with open(MOOD_FILE , "a") as file:
        writer = csv.writer(file)
        writer.writerow([date , mood])

st.title("Mood Tracker")
today = datetime.date.today()
st.subheader("How are you feeling today?")
mood = st.select("Select your mood" , ["Happy" , "Sad" , "Angry" , "Neutral"])

if st.button("Log Mood"):
    save_mood_data(today , mood ,)
    st.success("Mood Logged Successfully")