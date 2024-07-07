import streamlit as st
import pandas as pd

topics_list = ["Securities", "Securities-based derivatives contract", "Securities Industry Council"]

if "show_topic_choice" not in st.session_state:
    st.session_state.show_topic_choice = True
    


st.title("Quiz")
st.write(
    "Securities and Futures Act 2001"
)

def read_csv():
    st.session_state.question_bank = []
    for x in range(len(topics_list)):
        file_path = f"questions_{x}.csv"
        st.write("reading", file_path)
        df = pd.read_csv(file_path, sep='\t')
        st.write("read " + df.shape[0] + " rows")
        st.session_state.question_bank.append(df.values.tolist())
    st.write(st.session_state.question_bank)

read_csv()

    

def quiz():
    st.write("Starting quiz...")
    st.session_state.show_topic_choice = False
    st.session_state.selected_questions = []
    st.session_state.q_index = 0
    

if st.session_state.show_topic_choice == True:
    options = st.multiselect(
        "What topics would you like to be quizzed on?",
        (topics_list)
    )
    
    topics_selected = []
    for x in topics_list:
        if x in options:
            topics_selected.append(topics_list.index(x))
    
    
    #st.write("You selected:", options)
    #st.write("The indexes are", topics_selected)
    
    st.button("Start quiz", on_click=quiz)






