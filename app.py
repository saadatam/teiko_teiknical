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
st.title("Cell Analysis by Ammaar Saadat")

# button to load in data from interface
if st.button("Click this button to reload data from cells-count.csv into the database via SQLite"):
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
    st.subheader("Population Frequency per Sample")
    st.dataframe(df, width='stretch')

elif (page == "part 3: stats"):
    resp_dict, non_resp_dict = part3_stats()

    # make the df columns
    rows = []

    # st.subheader("Responders")
    # st.subheader("Non-Responders")

    for population, samples in resp_dict.items():
        for freq in samples:
            rows.append({"population": population, "percentage": float(freq), "group": "responder"})
    for population, samples in non_resp_dict.items():
        for freq in samples:
            rows.append({"population": population, "percentage": float(freq), "group": "non-responder"})

    df = pd.DataFrame(rows)

    # constructing respond data into box plots 
    labels = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    plot_data = []
    tick_labels = []
    for population in labels: 


        # grabbing from df map for percentage displaying
        responders = df[(df["population"] == population) & (df["group"] == "responder")]["percentage"].tolist()
        non_responders = df[(df["population"] == population) & (df["group"] == "non-responder")]["percentage"].tolist()
        
        # percentages
        plot_data.extend([responders, non_responders])

        # labels, marking responder / non-responder
        tick_labels.extend([f"{population}\nR",f"{population}\nNR"])
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.boxplot(plot_data, patch_artist=True)
    ax.set_xticklabels(tick_labels, rotation=0)
    ax.set_title("Part 3: Cell Frequency Distribution (resp vs. non-resp)")
    ax.set_ylabel("Population percentage (%)")
    ax.grid(axis="y", alpha=0.3)
    ax.set_xlabel("Immune Cell Populations - Response (R) vs. Non-response (NR)")
    st.pyplot(fig)

elif (page == "part 4: subset"):
    res = part4_subset()
    # project, subject, condition, age, sex, treatment, response, sample, sample_type, time_from_treatment_start, b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte
    df0 = pd.DataFrame(res[0], columns=["project", "subject", "condition", "age", "sex", "treatment", "response", "sample", "sample_type", "time_from_treatment_start", "b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"])
    st.subheader("Melanoma PBMC Samples at Baseline (time_from_treatment_start is 0) From Patients Treated with Miraclib")
    st.dataframe(df0, width='stretch')

    # ext #1 : samples from each project
    df1 = pd.DataFrame(res[1], columns=["Project", "Count"])
    st.subheader("Extension 1: Samples from each project")
    st.dataframe(df1, width='stretch')

    # ext #2 : resp vs. non-responders
    df2 = pd.DataFrame(res[2], columns=["Response", "Subject Count"])
    st.subheader("Extension 2: Subjects that were responders/non-responders")
    st.dataframe(df2, width='stretch')

    # ext #3 : subjects that were males/females
    df3 = pd.DataFrame(res[3], columns=["Sex", "Count"])
    st.subheader("Extension 3: Subjects that were males/females")
    st.dataframe(df3, width='stretch')




