# Streamlit app
import streamlit as st
import streamlit.components.v1 as components

st.title("Denver Restaurants")

components.iframe("https://www.google.com/maps/d/embed?mid=1Nzb_NboB70dcPIZWB716OU_1JrMznOY&hl=en&ehbc=2E312F", width=640, height=480)

