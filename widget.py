import streamlit as st

st.title("WIDGETS")
if st.button("Submit"):
    st.write("Hello Welcome!!")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input("Enter a Date")

st.time_input("Enter a Time")

if st.checkbox("You accept the T&C", value = False):
    st.write("Thank You!!")

v1 = st.radio("Colours", ["Red","Green","Blue"], index = 0)

v2 = st.selectbox("Colours", ["Red","Green","Blue"], index = 0)
st.write(v1, v2)

v3 = st.multiselect("Colours", ["Red","Green","Blue"])
st.write(v3)

st.slider("Age", min_value=18, max_value=60, value=23, step=2)

st.number_input("Numbers", min_value=18.0, max_value=60.0, value=23.0, step=2.0)

st.file_uploader("Upload a File")