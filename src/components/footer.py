import streamlit as st
from src.utils.image_utils import image_html


def footer_home():

    st.markdown(f"""
        <div style="margin-top:5rem; display:flex; gap:6px; items-align:center; justify-content:center; margin-bottom:-15rem">
            <p style="font-weight:bold; color:white;">Created with ❤️ by Atin<p/>
        </div>
    """, unsafe_allow_html=True)