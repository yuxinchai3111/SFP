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

import plotly.figure_factory as ff
from datetime import datetime, timedelta
import calendar

def create_beautiful_calendar(last_period, cycle_length=28, period_length=5, fertile_days=6):
    today = datetime.today().date()
    current_year = today.year
    current_month = today.month

    # Calculate important dates
    next_period_start = last_period + timedelta(days=cycle_length)
    period_days = [next_period_start + timedelta(days=i) for i in range(period_length)]

    ovulation_day = next_period_start - timedelta(days=14)
    fertile_window = [ovulation_day - timedelta(days=i) for i in range(fertile_days)]

    # Generate all days for current month
    cal = calendar.Calendar()
    month_days = [d for week in cal.monthdatescalendar(current_year, current_month) for d in week]

    # Prepare data for Plotly table
    data = []
    for day in month_days:
        color = 'white'
        text_color = 'black'

        if day == today:
            color = '#87CEFA'  # Light blue for today
        if day in period_days:
            color = '#FF9999'  # Red for period days
        if day in fertile_window:
            color = '#90EE90'  # Green for fertile days

        data.append({
            'Task': ' ',
            'Start': day,
            'Finish': day + timedelta(days=1),
            'Resource': color
        })

    # Create Gantt-like calendar
    fig = ff.create_gantt(data, index_col='Resource', show_colorbar=False,
                          title=f"{calendar.month_name[current_month]} {current_year}",
                          group_tasks=True, showgrid_x=True, showgrid_y=True)
    return fig

import streamlit as st
from datetime import date

last_period = st.date_input("When did your last period end?")
fig = create_beautiful_calendar(last_period)
st.plotly_chart(fig, use_container_width=True)
st.write("Light blue indicates TODAY.")
st.write("Red indicates your period days.")
st.write("Green indicates your fertile days.")

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

st.header("🚑 When to Seek Help")
st.markdown("""
If your period cramps are **too severe** or **do not improve with home remedies**, consider reaching out to a healthcare professional.

**Malaysia Healthcare Hotlines:**
- **KKM Healthline (MOH):** 03-8883 4400  
- **Hospital Kuala Lumpur (HKL):** +603-2615 5555  
- **Pantai Hospital Kuala Lumpur:** +603-2296 0888  
- **Gleneagles Hospital Kuala Lumpur:** +603-4141 3000  

For emergencies, call **999** or visit the nearest clinic/hospital.
""")


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

st.header("📚 Our Group Members Who Made This Web Application:")
members = {
    "Chai Yu Xin",
    "Hani Yasmin",
    "Choy Yuee Yann",
    "Angel Thu"
}
st.write("**Members:** ")
for member in members:
    st.write(f"- {member}")