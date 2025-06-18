import streamlit as st
l = st.number_input("inter length")
w = st.number_input("inter width")
area = l*w
st.write(area)
