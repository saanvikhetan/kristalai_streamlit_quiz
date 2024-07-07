import streamlit as st
import pandas as pd

topics_list = ["Securities", "Securities-based derivatives contract", "Securities Industry Council"]

if "show_topic_choice" not in st.session_state:
    st.session_state.show_topic_choice = True
if "quiz_mode" not in st.session_state:
    st.session_state.quiz_mode = False

    


st.title("Quiz")
st.write(
    "Securities and Futures Act 2001"
)

def read_csv():
    st.session_state.question_bank = []
    for x in range(len(topics_list)):
        file_path = f"questions_{x}.csv"
        #st.write("reading", file_path)
        df = pd.read_csv(file_path, sep='\t')
        #st.write("read " + str(df.shape[0]) + " rows")
        st.session_state.question_bank.append(df.values.tolist())
    #st.write(st.session_state.question_bank)

read_csv()

    

def start_quiz():
    #st.write("Starting quiz...")
    st.session_state.show_topic_choice = False

    # TODO: select questions randomly

    st.session_state.selected_questions = [[1,2],[0,3],[1,5]]
    st.session_state.q_index = 0
    st.session_state.quiz_mode = True


    

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
    
    st.button("Start quiz", on_click=start_quiz)


def iterate_question():
    st.session_state.q_index += 1 
    user_answer_index = current_question_from_bank.index(user_answer)
    if (user_answer_index-1) == (ord(current_question_from_bank[5]) - ord('A')):
        st.write("You selected the correct answer!")
    else:
        st.write(f"You selected the wrong answer. The correct one was number {(current_question_from_bank[5] - 'A')+1}")

if st.session_state.quiz_mode == True:
    current_question_list = st.session_state.selected_questions[st.session_state.q_index]
    current_question_from_bank = st.session_state.question_bank[current_question_list[0]][current_question_list[1]]
    #st.write(current_question_from_bank[0])
    user_answer = st.radio(
        current_question_from_bank[0],
        [current_question_from_bank[1], current_question_from_bank[2], 
        current_question_from_bank[3],current_question_from_bank[4]])

    st.button("Enter", on_click=iterate_question)





