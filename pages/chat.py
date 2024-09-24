import os
import streamlit as st
from time import perf_counter, sleep
from srcs.llm import LLM
from uuid import uuid4 as uuid
import asyncio


### Function definitions

def answer_question(question: str, streaming = True):
    with st.chat_message('human'):
        st.session_state.chat_history.append({'role': 'human', 'content': question})
        st.write(question)
    with st.chat_message('ai'):
        with st.spinner('Thinking..'):

            placeholder = st.empty()
            if streaming:
                response = llm.astream(question, placeholder)
                async def print_async_content(response, container):
                    chunks = ""
                    async for chunk in response:
                        chunks += chunk
                        container.markdown(chunks)
                asyncio.run(print_async_content(response, placeholder))
            
            else:
                response: str = llm.stream(question, placeholder)

            st.session_state.chat_history.append({'role': 'ai', 'content': response})
            st.write(response)
    return 'All Good!'


### Initialise session states
t0_start = perf_counter()

st.session_state.saved = "In Copilot"

if 'llm' not in st.session_state:
    st.session_state.llm = LLM()
llm = st.session_state.llm

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_ids = 0


### Display content

st.title('Chat')
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.write(message['content'])

if (prompt := st.chat_input("Enter your question")):
    # a question has been asked
    response = answer_question(prompt)
    if len(st.session_state.chat_history) == 0:
        # st.session_state.chat_ids = 
        pass

else:
    # no question has been asked
    if len(st.session_state.chat_history) == 0:
        # no prior conversation
        question = None
        suggestions = st.empty()
        with suggestions:
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button('What color should my doors be'):
                    question = 'What color should my doors be'
                    # st.rerun()
            with c2:
                if st.button('Who is Leonar Da Vinci and why is he known?'):
                    question = 'Who is Leonar Da Vinci and why is he known?'
                    # st.rerun()
            with c3:
                if st.button('Recommend me an anime similar to Naruto'):
                    question = 'Recommend me an anime similar to Naruto'
        if question:
            suggestions.empty()
            answer_question(question)
    else:
        # conversation exists
        pass


### Sidebar

with st.sidebar:
    if st.button("New conversation"):
        pass
    st.markdown("#### History")
    st.write()


t0_end = perf_counter()
st.sidebar.write(f"Time: {round(t0_end - t0_start, 4)}s")