import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

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




