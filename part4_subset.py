import csv # for csv parsing 
import sqlite3 
import re # for data formatting 

# Ammaar Saadat


def part4_subset():
    # connects to the cell database. If the db doesn't exist, it will create one
    con = sqlite3.connect('cell-count.db') 

    results = []

    # cursor for the db connection, allowing us to execute commands
    cur = con.cursor()
    
    # 1) query following - all melanoma PBMC samples at time_from_treatment_start = 0 from patients who have been treated with miraclib. 
    cur.execute("SELECT * FROM cells WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND treatment = 'miraclib' AND time_from_treatment_start = '0'")
    res_samples = cur.fetchall()

    # 2) extension number of samples from each project
    cur.execute("SELECT project, COUNT(*) AS sample_count FROM cells WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND treatment = 'miraclib' AND time_from_treatment_start = '0' GROUP BY project;")
    res_sample_count = cur.fetchall()

    # 3) number of subjects that were responders / non-responders
    cur.execute("SELECT response, COUNT(DISTINCT subject) AS subject_count FROM cells WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND treatment = 'miraclib' AND time_from_treatment_start = '0' GROUP BY response;")
    res_responders = cur.fetchall()

    # 4) number of subjects that were male / female
    cur.execute("SELECT sex, COUNT(DISTINCT subject) AS sample_count FROM cells WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND treatment = 'miraclib' AND time_from_treatment_start = '0' GROUP BY sex;")
    res_sex = cur.fetchall()

    # 5) considering melanoma males, avg number of b cells for responders at t=0
    cur.execute("SELECT ROUND(AVG(b_cell), 2) FROM cells WHERE condition = 'melanoma' AND sex = 'M' AND response = 'yes' AND time_from_treatment_start = '0';")
    res_average_mel_mals = cur.fetchall()
    
    results.append(res_samples)
    results.append(res_sample_count)
    results.append(res_responders)
    results.append(res_sex) 
    results.append(res_average_mel_mals)  

    return results