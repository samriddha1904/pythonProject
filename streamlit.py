import streamlit as st
import numpy as np
import pandas as pd

st.title('Samriddha`s app')

#Fetching some data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# cashing to avoid rerun of the file
@st.cache_data
def load_data(nrows):
    df=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase= lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    df[DATE_COLUMN]=pd.to_datetime(df[DATE_COLUMN])
    return df

df_load_state=st.text("Loading data.....")
df=load_data(1000)
df_load_state.text("Done! (using st.cache_data)")

#inspect raw data

st.subheader('Raw Data')
st.write(df)

# drawing a histogram
st.subheader('Number of pickups by hour')

hist_values=np.histogram(df[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# st.subheader('Map of all pickups')
# st.map(df)

# hour_to_filter=17
# filtered_data=df[df[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)

hour_to_filter=st.slider('hour',0,23,17)
filtered_data = df[df[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)