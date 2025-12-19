import streamlit as st

st.title("Session State")
st.header("Counter")

def add_one():
    st.session_state.counter+=1

if "counter" not in st.session_state:
    st.session_state['counter'] = 0

count = st.session_state.counter

st.button("Add one",on_click=add_one)

st.write(count)

