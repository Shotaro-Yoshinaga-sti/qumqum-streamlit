import streamlit as st
from utils.robot_connection import robot_connection, robot_disconnect
from dotenv import load_dotenv

load_dotenv()

st.title("ロボットとの接続の確立")

if st.session_state.robot_connection:
    st.success("Connected to the robot")
    if st.button("Disconnect"):
        robot_disconnect()
        st.session_state.robot_connection = False
        st.success("Disconnected from the robot")
        st.rerun()
else:
    st.error("ロボットと接続されていません。")
    if st.button("Try to connect"):
        connection = robot_connection()
        if not connection:
            st.error("やはり接続が確立することができません。実機の確認をしてください。")
        else:
            st.success("接続が確立されました。")
            st.session_state.robot_connection = True
        st.rerun()
