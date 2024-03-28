import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/4712cb27-fc7f-4b90-b541-0c9d2ead268d/ess2XWfrro.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")
html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/Statistic.py", label="การนำเสนอข้อมูลด้วยสถถิติ", icon="1️⃣")
st.page_link("pages/Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")