import streamlit as st
from src.utils.image_utils import image_html


def header_home():

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            {image_html("logo.png")}
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)