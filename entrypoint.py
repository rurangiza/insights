import streamlit as st

DIR = "./pages/"

########################## COMMON INFORMATIONS #################################

### Initialise session_states
st.session_state.saved = "In entrypoing.py"


### Creating the naviguation menu
st.logo("./assets/google-logo.webp")

pages = [
    st.Page(DIR + "chat.py", title="Chat", default=True),
    st.Page(DIR + "notes.py", title="Notes"),
]
pg = st.navigation(pages)


### Create the common sidebar


### Creating the common header


################################################################################

pg.run()