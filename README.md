
# Architecture Overview) 
- `requirements.txt`
- `env` file (create from makefile)
- `app.py` : main driver for streamlit app. 
- `part*.py` : each individual parts python file
- `Makefile` : pipeline, downloads, automatically start up local dev server

I learned a lot from this project, so I highlight future design choices under "Design Explanation"
# Installation and Deployment : How to Use
I utilize a makefile for local development deployment on localhost:8501. The commands are: 
- `make setup` : Run this first. This creates the python virtual environment, then activates the venv and installs the requirements via requirements.txt. (installing streamlit, pandas, matplotlib). Wait for this to finish for installation.
- `make pipeline` : activates the venv. Most of my logic occurs during the dashboard display as it offers dynamic loading, rendering, and table display 
- `make dashboard` : runs the locally hosted streamlit user interface for the data analysis from parts 1-4. 
- `make clean` : I additionally included this script to `rm -rf` the venv and pycache for local testing

# Localhost
Link to the development server port 

[http://localhost:8501/](http://localhost:8501/)

# Dashboard Documentation
- Navbar on the left to access different parts' data analysis
- Pt.2 contains a table of population frequency per sample
- Pt.3 contains the stats calculation for cell frequency distribution. Report is included at the end of page. 
- Pt.4 contains all the queries related to melanoma PBMC samples at baseline (time_from_treatment_start is 0) from patients treated with miraclib. At the bottom I included the final answer 

# Design Explanation
- Schema: I use two tables : `cells` and `freq`. `Cells` is created in load data while `freq` is created in part 2's python file. They are related via the `sample` column which acts as their sample_id. 
- Scalability : Currently, I re-initiate each table as they get accessed to avoid duplicate elements. If I were to scale this for larger projects, I would isolate the data computation and the UI display to avoid dynamic creation. 
- 