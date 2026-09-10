import streamlit as st
import random

if "number" not in st.session_state:
    st.session_state.number = None

if st.session_state.number is None:
    button_label = "Start"
elif st.session_state.number % 2 == 0:
    button_label = "Half it"
else:
    button_label = "Triple and add one"

if st.button(button_label):
    if st.session_state.number is None:
        st.session_state.number = random.randint(1, 100)
    elif st.session_state.number % 2 == 0:
        st.session_state.number //= 2
    else:
        st.session_state.number = 3 * st.session_state.number + 1

if st.session_state.number is None:
    st.write("Ready")
else:
    st.write(st.session_state.number)