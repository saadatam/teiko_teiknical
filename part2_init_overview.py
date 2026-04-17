import csv # for csv parsing 
import sqlite3 
import re # for data formatting 

# Task 1 : Calculate the total counts
# “What is the frequency of each cell type in each sample?” 

# connects to the cell database. If the db doesn't exist, it will create one
con = sqlite3.connect('cell-count.db') 

# cursor for the db connection, allowing us to execute commands
cur = con.cursor()

# Query cell count for each respective sample. 
cur.execute("SELECT b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte FROM cells;")

# extract all elements from the SQL query via the cursor. 
res = cur.fetchall()


labels = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
if res is not None: 
    with open("test_2.txt", 'w') as f:
        # check every sample 
        for row in res:
            # obtain all cell counts.
            total_count = 0
            for cell in row: 
                print(cell)
                total_count = total_count + int(cell)
            
            # calculate each frequency
            iter = 0
            for cell in row: 
                # percentage frequency calculation 
                freq = int(cell) / total_count
                freq = round(freq * 100, 2)

                # writing to file
                f.write(labels[iter] + ": " + str(freq) + "%, ")
                iter = iter + 1

            f.write("\n")


# TODO:: create table for this data