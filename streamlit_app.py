import streamlit as st

st.title('✅ Checkbox App')

if 'count' not in st.session_state:
    st.session_state.count = 0

func1_box = st.checkbox('Function 1')
func2_box = st.checkbox('Function 2')
func3_box = st.checkbox('Function 3')
