import streamlit as st
import requests
API_URL ="http://127.0.0.1:8000"
if "token" not in st.session_state:
    st.session_state.token = None
if "email" not in st.session_state:
    st.session_state.email = None
def logout():
    st.session_state.token = None
    st.session_state.email = None
    st.rerun()
if st.session_state.token is None:
    st.title("login page")
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input(
            "password",
            type="password"
        )
        submit = st.form_submit_button(
            "login"
        )
    if submit:
        try:
            response = requests.post(
                f"{API_URL}/auth/login",
                json={
                    "email": email,
                    "password": password
                }
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.token = data["access_token"]
                st.session_state.email = email
                st.success(
                    "login successful"
                )
                st.rerun()
            else:
                error = response.json()
                st.error(
                    error.get(
                        "detail",
                        "invalid credentials"
                    )
                )
        except Exception as e:
            st.error(f"cannot connect to FastAPI server: {e}")
else:
    st.title("dashboard")
    st.success(f"welcome,{st.session_state.email}")
    st.write(
        "you are logged in successfully"
    )
    st.write(
        "this is a placeholder dashboard"
    )
    if st.button("logout"):
        logout()
