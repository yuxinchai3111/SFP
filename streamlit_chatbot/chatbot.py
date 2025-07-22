import streamlit as st 
import pandas as pd
# Set page title
st.title("Your Very Own Period Tracker")

# Add header and slogan
st.header("Period Peace Begins Here! ")
st.subheader("Do you remember when your last period ended? ")

# Ask user for last period end date
last_period = st.date_input("When did your last period end? ")

#Sample DataFrame (replace with your own tracking data)
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Average Cycle Length': [28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28],
    'Last Period End Date': [last_period - pd.DateOffset(days=28*i) for i in range(12)]
})

# Add sidebar filters
st.sidebar.header("Filters")
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique()
)

periodduration_range = st.sidebar.slider(
    "Select Period Duration",
    min_value=1,
    max_value=14,
    value=(5)
)
#Filter data based on sidebar selections
filtered_df = df[
    (df['Month'] == selected_month) &
    'Period Duration':[5] * 12, 
]

#Display filtered data
st.subheader("Your Period Data")
st.dataframe(filtered_df)