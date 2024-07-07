import streamlit as st
import pandas as pd


#### Functions

def read_csv():
    st.session_state.question_bank = []
    for x in range(len(topics_list)):
        file_path = f"questions_{x}.csv"
        #st.write("reading", file_path)
        df = pd.read_csv(file_path, sep='\t')
        #st.write("read " + str(df.shape[0]) + " rows")
        st.session_state.question_bank.append(df.values.tolist())
    #st.write(st.session_state.question_bank)

def start_quiz():
    #st.write("Starting quiz...")
    st.session_state.show_topic_choice = False
    st.session_state.show_quiz_mode = True
    st.session_state.show_end_quiz = False


    # TODO: select questions randomly

    st.session_state.selected_questions = [[1,2],[0,3],[1,5]]
    st.session_state.q_index = 0
    st.session_state.show_quiz_mode = True
    st.session_state.score = 0

def iterate_question():
    st.session_state.q_index += 1 
    if st.session_state.q_index == len(st.session_state.selected_questions):
        st.session_state.show_end_quiz = True
    user_answer_index = current_question_from_bank.index(user_answer)
    if (user_answer_index-1) == (ord(current_question_from_bank[5]) - ord('A')):
        st.write("You selected the correct answer!")
        st.session_state.score += 1
    else:
        st.write("You selected the wrong answer. The correct one was number " + 
            str((ord(current_question_from_bank[5]) - ord('A'))+1))

def start_new_quiz():
    st.session_state.show_topic_choice = True
    st.session_state.show_quiz_mode = False
    st.session_state.show_end_quiz = False

#### initialize global variables and session state

topics_list = ["Securities", "Securities-based derivatives contract", "Securities Industry Council"]

if "show_topic_choice" not in st.session_state:
    st.session_state.show_topic_choice = True
if "show_quiz_mode" not in st.session_state:
    st.session_state.show_quiz_mode = False
if "show_end_quiz" not in st.session_state:
    st.session_state.show_end_quiz = False
    
# read in question bank
read_csv()


#### Display Application Title=
st.title("Quiz")
st.write(
    "Securities and Futures Act 2001"
)


### Display option:  Show topic selector
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


### Display option:  Show quiz questions
if st.session_state.show_quiz_mode == True:
    current_question_list = st.session_state.selected_questions[st.session_state.q_index]
    current_question_from_bank = st.session_state.question_bank[current_question_list[0]][current_question_list[1]]
    #st.write(current_question_from_bank[0])
    user_answer = st.radio(
        current_question_from_bank[0],
        [current_question_from_bank[1], current_question_from_bank[2], 
        current_question_from_bank[3],current_question_from_bank[4]])

    st.button("Enter", on_click=iterate_question)

### Display option:  Show quiz end with score, and a button to start next quiz
if st.session_state.show_end_quiz == True:
    st.write(f"Your score is {st.session_state.score}/10.")
    st.button("Start another quiz", on_click=start_new_quiz)



