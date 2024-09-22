all: run

run:
	streamlit run entrypoint.py

install:
	python3 -m pip install -r requirements.txt