import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data['name']}""")


def login_teacher(teacher_username, teacher_pass):
    if not teacher_username or not teacher_pass:
        return False, "All Fields are required!"

    teacher = teacher_login(teacher_username, teacher_pass)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True, "Login successful"

    return False, "Unexpected Error!"


def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Login using password', text_alignment="center")
    st.space(size="medium")

    teacher_username = st.text_input("Enter username", placeholder="Like: atin", key="login_username")

    teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter your password", key="login_password")

    st.divider()

    btcol1, btcol2 = st.columns(2)

    with btcol1:
        if st.button("Login", icon=':material/passkey:', shortcut="control+enter", width="stretch"):
            success, message = login_teacher(teacher_username, teacher_pass)
            if success:
                st.toast("Welcome back!", icon="👋")
                st.session_state.pop("login_username", None)
                st.session_state.pop("login_password", None)
                import time
                time.sleep(1)
                st.rerun()
            elif message == "All Fields are required!":
                st.error("All Fields are required!")
            else:
                st.error("Invalid username or password")

    with btcol2:
        if st.button("Register Instead", type="primary", icon=':material/passkey:', width="stretch"):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key="loginbackbtn", shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Register your teacher profile')
    st.space(size="medium")
    
    teacher_username = st.text_input("Enter username", placeholder="Like: atin", key="register_username")

    teacher_name = st.text_input("Enter name", placeholder="Like: Atin Singha", key="register_name")
    
    teacher_pass = st.text_input("Enter password", type="password", placeholder="Enter your password", key="register_password")

    teacher_pass_confirm = st.text_input("Confirm password", type="password", placeholder="Confirm your password", key="register_password_confirm")
    
    st.divider()
    
    btcol1, btcol2 = st.columns(2)
    
    with btcol1:
        if st.button("Register Now", icon=':material/passkey:', shortcut="control+enter", width="stretch"):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                st.session_state.pop("register_username", None)
                st.session_state.pop("register_name", None)
                st.session_state.pop("register_password", None)
                st.session_state.pop("register_password_confirm", None)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    
    with btcol2:
        if st.button("Login Instead", type="primary", icon=':material/passkey:', width="stretch"):
            st.session_state.teacher_login_type = "login"
            st.rerun()
    
    footer_dashboard()