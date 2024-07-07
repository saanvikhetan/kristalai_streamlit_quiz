import streamlit as st

st.title("Quiz")
st.write(
    "Securities and Futures Act 2001"
)

def quiz():
    st.write("Starting quiz...")
    

topics_list = ["Securities", "Securities-based derivatives contract", "Securities Industry Council"]

options = st.multiselect(
    "What topics would you like to be quizzed on?",
    (topics_list)
)

topics_selected = []
for x in topics_list:
    if x in options:
        topics_selected.append(topics_list.index(x))


st.write("You selected:", options)
st.write("The indexes are", topics_selected)

st.button("Start quiz", on_click=quiz)






