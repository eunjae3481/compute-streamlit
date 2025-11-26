import streamlit as st
import math

# ---------------------
# 페이지 꾸미기
# ---------------------
st.set_page_config(
    page_title="Money Bloom ✨",
    page_icon="🌸",
    layout="centered"
)

# 파스텔 감성 CSS
page_style = """
<style>
    body {
        background: #fff5fb;
        font-family: 'Pretendard', sans-serif;
    }
    .main-title {
        font-size: 36px;
        text-align: center;
        color: #ff82bf;
        font-weight: 800;
        padding-bottom: 10px;
        margin-top: -20px;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #c25ea9;
        margin-bottom: 30px;
    }
    .calc-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(255, 150, 200, 0.2);
        margin-bottom: 25px;
    }
    .result-box {
        background: #ffe7f5;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: 600;
        color: #d24f9f;
        margin-top: 20px;
    }
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ---------------------
# UI 헤더
# ---------------------
st.markdown("<div class='main-title'>🌸 MONEY BLOOM 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>절세 + 복리로 내 돈이 피어나는 순간</div>", unsafe_allow_html=True)

# ---------------------
# 기능 선택
# ---------------------
menu = st.selectbox(
    "🌼 사용할 기능 선택:",
    ["절세계산기", "복리 계산기"],
    index=0
)

# ---------------------
# 절세계산기
# ---------------------
if menu == "절세계산기":
    st.markdown("<div class='calc-card'>", unsafe_allow_html=True)
    st.markdown("### 💸 절세계산기")
    income = st.number_input("연 소득(만원)", min_value=0, step=10)
    deduction = st.number_input("공제액(만원)", min_value=0, step=10)

    tax_rate = st.slider("적용 세율(%)", 6, 45, 15)

    if st.button("✨ 절세 금액 계산하기"):
        saved = deduction * (tax_rate / 100)
        st.markdown(f"<div class='result-box'>💖 절세 금액: {saved:,.0f} 만원</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------
# 복리 계산기
# ---------------------
else:
    st.markdown("<div class='calc-card'>", unsafe_allow_html=True)
    st.markdown("### 🌱 복리 계산기")
    principal = st.number_input("초기 금액(원)", min_value=0, step=1000)
    rate = st.number_input("연 이자율(%)", min_value=0.0, step=0.1)
    years = st.number_input("기간(년)", min_value=1, step=1)

    if st.button("🌸 복리 계산하기"):
        final_money = principal * ((1 + rate / 100) ** years)
        st.markdown(f"<div class='result-box'>🌼 최종 금액: {final_money:,.0f} 원</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
