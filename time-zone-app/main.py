import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of valid time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
]

st.title("🕓 Time Zone Tracker App")

# Display current times in selected time zones
st.subheader("Current Times in Selected Timezones")
selected_timezones = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

if selected_timezones:
    for tz in selected_timezones:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.write(f"**{tz}**: {current_time}")
else:
    st.warning("Please select at least one timezone.")

# Time conversion feature
st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    try:
        dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        
        st.success(f"Converted Time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.info("✨ This app helps you track and convert times across different time zones!")
