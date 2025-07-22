import streamlit as st
import pandas as pd
from datetime import timedelta, date
import calendar
import plotly.express as px

# -------------------------------
# HEADER IMAGE & TITLE
# -------------------------------
st.title("🌸 Your Very Own Period Tracker")
st.image("https://i.pinimg.com/1200x/de/13/f2/de13f2f288026ff34cc19c7078adf37d.jpg",
         caption="Period Peace Begins Now 💖", width=300)

st.write("Do you remember when your last period started?")

# -------------------------------
# USER INPUTS
# -------------------------------
st.header("Enter Your Period Details")
last_period = st.date_input("When did your last period start?", value=date.today())
cycle_length = st.number_input("Average Cycle Length (days)", min_value=21, max_value=35, value=28)
period_duration = st.number_input("How many days does your period last?", min_value=1, max_value=10, value=5)

# -------------------------------
# CALCULATIONS
# -------------------------------
next_period_start = last_period + timedelta(days=cycle_length)
next_period_end = next_period_start + timedelta(days=period_duration)
fertile_start = next_period_start - timedelta(days=14)
fertile_end = fertile_start + timedelta(days=6)

# -------------------------------
# PREDICTIONS
# -------------------------------
st.subheader("🔮 Your Predictions")
st.success(f"**Next Period Start:** {next_period_start.strftime('%B %d, %Y')} 🩸")
st.info(f"**Next Period End:** {next_period_end.strftime('%B %d, %Y')} 🌸")
st.warning(f"**Fertile Window:** {fertile_start.strftime('%B %d, %Y')} - {fertile_end.strftime('%B %d, %Y')} 🌱")

# -------------------------------
# CALENDAR HEATMAP
# -------------------------------
st.subheader("📅 Monthly Calendar Overview")

# Generate current month dates
year = date.today().year
month = date.today().month
days_in_month = calendar.monthrange(year, month)[1]
calendar_dates = [date(year, month, day) for day in range(1, days_in_month + 1)]

# Mark period and fertile window
calendar_df = pd.DataFrame({"Date": calendar_dates})
calendar_df["Status"] = "Normal"
calendar_df.loc[(calendar_df["Date"] >= next_period_start) & (calendar_df["Date"] <= next_period_end), "Status"] = "Period"
calendar_df.loc[(calendar_df["Date"] >= fertile_start) & (calendar_df["Date"] <= fertile_end), "Status"] = "Fertile"

# Plot heatmap using Plotly
fig = px.scatter(
    calendar_df, x="Date", y=[1] * len(calendar_df),
    color="Status",
    color_discrete_map={"Period": "red", "Fertile": "green", "Normal": "lightgrey"},
    symbol="Status",
    size=[15] * len(calendar_df),
    labels={"y": ""}
)
fig.update_yaxes(showticklabels=False, showgrid=False)
fig.update_layout(showlegend=True, height=150, margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# PERIOD HISTORY (last 3 cycles)
# -------------------------------
st.subheader("📝 Your Last 3 Cycles")
cycles = pd.DataFrame({
    "Cycle": [1, 2, 3],
    "Start Date": [last_period - timedelta(days=cycle_length * i) for i in range(3)],
    "End Date": [last_period - timedelta(days=cycle_length * i) + timedelta(days=period_duration) for i in range(3)]
})
st.dataframe(cycles)

# -------------------------------
# HEALTH TIP
# -------------------------------
st.header("💡 Health Tip")
import random
health_tips = [
    "Stay hydrated and track your cycles regularly for better insights! ",
    "Maintain a balanced diet to help manage your menstrual health.",
    "Regular exercise can help alleviate menstrual symptoms.",
    "Consider keeping a journal to track your mood and symptoms during your cycle.",
    "Consult with a healthcare provider if you experience severe menstrual pain.",
    "Use a menstrual cup or reusable pads to reduce waste and save money.",
    "Practice relaxation techniques like yoga or meditation to ease menstruation discomfort.",
    "Keep track of your symptoms to identify patterns and triggers.",
    "Ensure you get enough sleep during your cycle for better overall health.",
    "Discuss any irregularities in your cycle with a healthcare professional.",
    "Change Products Often: Don't wear pads or tampons for too long.",
    "Wash Gently: Use just water for your private areas. Skip scented stuff.",
    "Cotton Undies: They let your skin breathe.",
    "Use Heat: A warm pad on your belly helps with cramps.",
    "Drink Water: Lots of water can lessen bloating and headaches.",
    "Light Exercise: Gentle walks or yoga can make you feel better.",
    "Pain Meds: Over-the-counter pills like ibuprofen can help if cramps are bad.",
    "Rest: Listen to your body and take it easy if you're tired."
]
random_tip = random.choice(health_tips)
color_functions = [st.success, st.info, st.warning, st.error]
random_color = random.choice(color_functions)
random_color(random_tip)

st.header("🎵 Feeling Sad? ")
st.write("❤️ **Try this song to lift your spirits:** ")
import random
songs = [
    "Stairway to Heaven - Led Zeppelin",
    "Comfortably Numb - Pink Floyd",
    "Hotel California - Eagles",
    "Sultans of Swing - Dire Straits",
    "Blackbird - The Beatles",
    "While My Guitar Gently Weeps - The Beatles (featuring Eric Clapton)",
    "Layla - Derek and the Dominos (Eric Clapton)",
    "Sweet Child O' Mine - Guns N' Roses",
    "Dust in the Wind - Kansas",
    "More Than Words - Extreme",
    "Tears in Heaven - Eric Clapton",
    "Good Riddance (Time of Your Life) - Green Day",
    "Here Comes the Sun - The Beatles",
    "Smoke on the Water - Deep Purple",
    "Johnny B. Goode - Chuck Berry",
    "Purple Haze - Jimi Hendrix",
    "Back in Black - AC/DC"
]
random_song = random.choice(songs)
st.text(random_song)

st.write("**Listen to some relatable tunes on Spotify:** ")
spotify_url = "https://open.spotify.com/embed/playlist/6eROun27j4HRVOQF4qJgXW"  # Example playlist
st.markdown(f"""
<iframe style="border-radius:12px" src="{spotify_url}" 
width="100%" height="280" frameBorder="0" 
allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
</iframe>
""", unsafe_allow_html=True)
