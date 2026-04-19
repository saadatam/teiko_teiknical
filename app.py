import csv # for csv parsing 
import sqlite3 
import re # for data formatting 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from load_data import load_data
from part2_init_overview import part2_init
from part3_stats import part3_stats
from part4_subset import part4_subset

# initialize data
st.set_page_config(page_title="Teiko Teiknical Dashboard : Cell Analysis", layout= "wide")

# title
st.title("Cell Analysis by Ammaar")

# button to load in data from interface
if st.button("Click me to reload in data from cells-count.csv via SQLite"):
    load_data()
    st.success("Load completed")

# options for user
page = st.sidebar.radio(
    "Choose analysis",
    ["part 2: overview", "part 3: stats", "part 4: subset"]
)

if (page == "part 2: overview"):
    res = part2_init()
    # make df columns
    df = pd.DataFrame(res, columns=["sample", "total_count", "population", "count", "percentage"])
    st.subheader("Frequency per sample")
    st.dataframe(df, width='stretch')

elif (page == "part 3: stats"):
    res = part3_stats()
    # make the df columns
    st.subheader("Responders")
    st.dataframe(res[0])
    st.subheader("Non-Responders")
    st.dataframe(res[1])
# elif (page == "part 4: subset"):

