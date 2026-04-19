import sqlite3 
import csv # for csv parsing 
import re # for data formatting 

# Written by: Ammaar Saadat
# documentation I'm utilizing : https://docs.python.org/3/library/sqlite3.html
def load_data():
    # connects to the cell database. If the db doesn't exist, it will create one
    con = sqlite3.connect('cell-count.db') 

    # cursor for the db connection, allowing us to execute commands
    cur = con.cursor()

    # Clean up before every run
    cur.execute("DROP TABLE IF EXISTS cells;") 

    # execute the db table creation. Good thing about sqlite3 is that specifying datatypes is optional, 
    # so for regular SQL commands, it'd be best practice to specify each. 
    # TODO:: change this into relational databases
    cur.execute("CREATE TABLE IF NOT EXISTS cells(project, subject, condition, age, sex, treatment, response, sample, sample_type, time_from_treatment_start, b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte);")

    # initialize each row in the data.
    data = []
    with open('cell-count.csv', newline='') as f:
        reader = csv.reader(f) # obtain all the elements in the csv file
        # iterate through the rows and insert
        next(reader) # skip first element as it's the header
        for row in reader:
            data.append(row)
        cur.executemany("INSERT INTO cells(project, subject, condition, age, sex, treatment, response, sample, sample_type, time_from_treatment_start, b_cell, cd8_t_cell, cd4_t_cell, nk_cell, monocyte) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    # Query and data insertion testing, can optionally remove this for performance benchmarks
    # cur.execute("SELECT * FROM cells;")
    # res = cur.fetchall()
    # if res is not None: 
    #     with open("test_1.txt", 'w') as f:
    #         for row in res:
    #             n_row = re.findall(r"'([^']*)'", str(row))
    #             n_row = ",".join(n_row)
                # f.write(n_row)
                # f.write("\n")

    # commit changes to the samples database
    con.commit()

    # close context manager connection
    con.close()