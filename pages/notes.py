import datetime

import streamlit as st
from time import perf_counter

### Function definitions

NOTES_DIR = "./notes/"


t0_start = perf_counter()

###########################################
st.title('Notes')
###########################################
with st.expander("See explanation"):
    st.write('''
        This app allows to 
    ''')

st.write("You have 3 options for taking notes. Either:")

st.markdown("#### 0. Send random note")
if st.button("Generate random note"):
    date: str = str(datetime.datetime.now())
    random_note = """
    This is a random note
    
    it's purpose is to test the generate button in the notes page.
    """
    with open(f'{NOTES_DIR}{date}.txt', 'w') as f:
        f.write(random_note)

st.markdown("#### 2. Upload Local Files")
if (file := st.file_uploader(label='Can be .txt, .md or .pdf', accept_multiple_files=True)):
    pass

st.markdown("#### 3. Load from Notion")
if st.button(label='Get from Notion'):
    pass

t0_end = perf_counter()
st.sidebar.write(f"Time: {round(t0_end - t0_start, 4)}s")