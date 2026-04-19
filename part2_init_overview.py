import csv # for csv parsing 
import sqlite3 
import re # for data formatting 

# Task 1 : Calculate the total counts
# “What is the frequency of each cell type in each sample?” 
def part2_init():
    # connects to the cell database. If the db doesn't exist, it will create one
    con = sqlite3.connect('cell-count.db') 

    # cursor for the db connection, allowing us to execute commands
    cur = con.cursor()
    labels = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]

    # clean up if run multiple times to avoid multiple insertions. 
    cur.execute("DROP TABLE IF EXISTS freq;") 

    # create relational table for summary data 
    # __________________Column_Summary_____________________
    #   sample: sample_id - str (since it's given as a str in csv files)
    #   total_count: number of cells - int
    #   population: majority cell data - string
    #   count: cell count as a number - int.
    #   percentage: representation of population cells - str 
    cur.execute("CREATE TABLE IF NOT EXISTS freq(sample, total_count, population, count, percentage);")


    # Query cell count for each respective sample. 
    cur.execute("SELECT sample, b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte FROM cells;")

    # extract all elements from the SQL query via the cursor. 
    res = cur.fetchall()

    labels = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
    data = []
    if res is not None: 

        # check every sample. 
        # 1) calculate their cell counts
        # 2) calculate the population frequncy

        for row in res:
            # obtain all cell counts.
            total_count = 0

            for cell in row[1:]: 
                total_count = total_count + int(cell)
            
            # calculate each frequency
            population = ""
            max = 0
            iter = 0 # for labels
            max_cell_count = 0
            # f.write(row[0] + ", ")
            for cell in row[1:]: 
                
                # percentage frequency calculation 
                freq = int(cell) / total_count
                freq = round(freq * 100, 2)
                if (freq >= max):
                    max = freq
                    population = labels[iter]
                    max_cell_count = cell
                # writing to file
                iter = iter + 1
            data.append((row[0], total_count, population, max_cell_count, max))

    # insert into the freq table. 
    cur.executemany("INSERT INTO freq(sample, total_count, population, count, percentage) VALUES(?, ?, ?, ?, ?)", data)
    # commit changes and close connection 
    con.commit()
    
    con.close()
    return data