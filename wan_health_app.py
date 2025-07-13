import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.title("🐶 わんちゃん健康管理アプリ")

# CSVから読み込み
try:
    df = pd.read_csv("wan_health.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["日付", "体重", "体調"])

# 入力フォーム
st.subheader("📋 今日の記録を入力")
today = date.today()
weight = st.number_input("体重 (kg)", min_value=0.0, step=0.1)
condition = st.selectbox("体調", ["元気", "普通", "少し元気ない", "病院に行った"])

if st.button("記録する"):
    new_data = pd.DataFrame([[today, weight, condition]], columns=df.columns)
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("wan_health.csv", index=False)
    st.success("✅ 記録しました！")

# 表とグラフ
st.subheader("📊 記録一覧")
st.dataframe(df)

st.subheader("📈 体重の推移")
if not df.empty:
    df["日付"] = pd.to_datetime(df["日付"])
    plt.plot(df["日付"], df["体重"], marker='o')
    plt.xlabel("日付")
    plt.ylabel("体重(kg)")
    plt.xticks(rotation=45)
    st.pyplot(plt)
