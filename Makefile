.PHONY: setup pipeline dashboard clean

# create venv for codespace
# activate and install requirements for the venv
setup: 
	python3 -m venv env
	source env/bin/activate && pip install -r requirements.txt

# loads the data. I developed the pipeline via streamlit so it will dynamically calculate per run
pipeline: 
	source env/bin/activate 

# launches the streamlit program
dashboard:
	source env/bin/activate && streamlit run app.py

clean:
	rm -rf env __pycache__