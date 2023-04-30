import streamlit as st
import pandas as pd


view = [100, 150, 30]
seview = pd.Series(view)

st.write("# Youtube view")
st.write("## 1. raw")
view
st.write("## 2. Bar_chart")
st.bar_chart(view)
st.write("## 3. Series")
seview
