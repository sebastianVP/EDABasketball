import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.title("NBA Player Stats Explorer")

st.markdown("""
This apps perfoms simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data Source     :** [Basketball-reference.com](https://www.basketball-reference.com/).

""")

st.sidebar.header('User Input Features')

selected_year = st.sidebar.selectbox('Year',list(reversed(range(1950,2020))))


# Web Scrapying of NBA players stats
