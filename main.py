import streamlit as st
from utils.robot_connection import robot_connection, robot_disconnect
import atexit


def main():
    atexit.register(robot_disconnect)

    # 各Stateの初期化
    if "robot_connection" not in st.session_state:
        connection = robot_connection()
        st.session_state.robot_connection = connection

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    top_page = st.Page(page="contents/top_page.py", title="Top", icon=":material/home:")
    about = st.Page(page="contents/about.py", title="About", icon=":material/apps:")
    chat = st.Page(page="contents/chat.py", title="Chat", icon=":material/chat:")
    non_robot_chat = st.Page(
        page="contents/non-robot-chat.py",
        title="Non-Robot Chat",
        icon=":material/chat:",
    )

    if st.session_state.robot_connection:
        pg = st.navigation([top_page, chat, about])
    else:
        pg = st.navigation([top_page, non_robot_chat])

    pg.run()


if __name__ == "__main__":
    main()
