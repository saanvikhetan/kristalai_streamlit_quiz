import streamlit as st

topics_list = ["Securities", "Securities-based derivatives contract", "Securities Industry Council"]

if "show_topic_choice" not in st.session_state:
    st.session_state.show_topic_choice = True


st.title("Quiz")
st.write(
    "Securities and Futures Act 2001"
)



def quiz():
    st.write("Starting quiz...")
    st.session_state.show_topic_choice = False
    
    

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






