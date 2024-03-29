import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/59528ad6-c294-40e3-bb93-d855204a6ffe/0VaAnvs7qX.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello,key="hello")



st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/1🌋Statistic.py", label="การนำเสนอข้อมูลด้วยสถถิติ", icon="1️⃣")
st.page_link("pages/2🛬Chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/3⛵KNNClassifile.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("pages/4🏜️DecdisionTreeClassify.py", label="การนำเสนอข้อมูลด้วยการจินตทัศน์ข้อมูล", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")