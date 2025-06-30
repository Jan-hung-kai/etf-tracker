
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.set_page_config(page_title="ETF 追蹤儀表板", layout="wide")

st.title("📈 ETF 追蹤儀表板")
st.markdown("版本：基本展示版 | 資料為模擬範例")

# 模擬資料區
today = datetime.date.today()
dates = pd.date_range(today - datetime.timedelta(days=6), today)

price_data = pd.DataFrame({
    '日期': dates,
    '00970B 收盤價': [8.85, 8.87, 8.91, 8.89, 8.90, 8.92, 8.93],
    '00687B 收盤價': [26.05, 26.10, 26.00, 26.08, 26.12, 26.18, 26.20],
}).set_index('日期')

volume_data = pd.DataFrame({
    '日期': dates,
    '00970B 成交量': [12000, 11500, 13000, 15000, 14500, 17000, 16000],
    '00687B 成交量': [3000, 2900, 3100, 3200, 3300, 3500, 3600],
}).set_index('日期')

st.subheader("🔹 ETF 收盤價趨勢圖")
st.line_chart(price_data)

st.subheader("🔹 ETF 成交量變化")
st.bar_chart(volume_data)

# 假設配息公告資料
dividend_data = pd.DataFrame({
    'ETF': ['00970B', '00687B'],
    '公告日期': [str(today - datetime.timedelta(days=3)), str(today - datetime.timedelta(days=15))],
    '預計發放日': [str(today + datetime.timedelta(days=10)), str(today + datetime.timedelta(days=15))],
    '每單位配息': [0.08, 0.22],
    '殖利率': ['10.76%', '3.34%']
})

st.subheader("🔹 最新配息公告")
st.dataframe(dividend_data, use_container_width=True)

# 法人買賣超簡易模擬
foreign_data = pd.DataFrame({
    '日期': dates,
    '00970B 外資買賣超(張)': [100, -50, 150, -20, 0, 80, 60],
}).set_index('日期')

st.subheader("🔹 外資買賣超趨勢")
st.bar_chart(foreign_data)

st.markdown("---")
st.caption("© 2025 ETF Tracker Demo | 本頁面由 Streamlit 部署，資料為模擬展示用途")
