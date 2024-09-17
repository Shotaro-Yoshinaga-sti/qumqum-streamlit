import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from utils.robot_voice import robot_voice

import os
from dotenv import load_dotenv

client = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_API_ENDPOINT"],
    openai_api_version="2023-03-15-preview",
    deployment_name=os.environ["DEPLOYMENT_NAME_GPT"],
    openai_api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_type="azure",
)

# ページの設定
st.set_page_config(page_title="My Great ChatGPT", page_icon="😎")
st.header("My Great ChatGPT 😎")

# チャット履歴の初期化
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="あなたはロボットです。返答はシンプルに一文で返答してください。約10文字間隔で「,」で区切ってください。"
        )
    ]

# ユーザーの入力を監視
if user_input := st.chat_input("聞きたいことを入力してね！"):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("GPT is typing ..."):
        response = client.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    robot_voice(response.content)


# チャット履歴の表示
messages = st.session_state.get("messages", [])
for message in messages:
    if isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    else:
        st.write(f"System message: {message.content}")
