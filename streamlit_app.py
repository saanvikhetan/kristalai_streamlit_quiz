import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

options = st.multiselect(
    "What topics would you like to be quizzed on?",
    (["Securities", "Securities-based derivatives contract", "Securities Industry Council"])


st.write("You selected:", options)



