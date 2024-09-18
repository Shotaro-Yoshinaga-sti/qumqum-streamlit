import streamlit as st
from utils.robot_move import (
    robot_reset,
    robot_cheers,
    robot_denial,
    robot_walk,
    robot_pose_hans_up_left,
    robot_pose_hans_up_right,
    robot_turn_left,
    robot_turn_right,
    robot_arms_up_dance,
    robot_kubifuri_kyoshu,
    robot_banzai,
    robot_arms_shake_dance,
    robot_jidanda
)

st.title("ロボットの動作確認")

MOVE = [
    "前進",
    "万歳",
    "拒否",
    "左手を上げる",
    "右手を上げる",
    "左に回る",
    "右に回る",
    "リセット",
    "両手足上げダンス",
    "首振り挙手",
    "地団駄",
]

move = st.selectbox("動作を選択してください", MOVE)

if st.button("実行"):
    with st.spinner("Robot move start ..."):
        if move == "前進":
            robot_walk()
        elif move == "万歳":
            robot_cheers()
        elif move == "拒否":
            robot_denial()
        elif move == "左手を上げる":
            robot_pose_hans_up_left()
        elif move == "右手を上げる":
            robot_pose_hans_up_right()
        elif move == "左に回る":
            robot_turn_left()
        elif move == "右に回る":
            robot_turn_right()
        elif move == "リセット":
            robot_reset()
        elif move == "両手上げダンス":
            robot_arms_up_dance()
        elif move == "首振り挙手":
            robot_kubifuri_kyoshu()
        elif move == "地団駄":
            robot_jidanda()
        robot_reset()
        st.rerun()
