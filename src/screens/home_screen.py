import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.utils.image_utils import show_image

def home_screen():
    header_home()

    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        show_image("student.png", width=120, custom_style="margin-bottom: 10px")
        if st.button('Student Portal', type="primary", icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        show_image("teacher.png", width=149, custom_style="margin-bottom: 10px")
        if st.button('Teacher Portal', type="primary", icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()