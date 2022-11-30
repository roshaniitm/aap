import streamlit as st
import pandas as pd

st.title("A Subtraction App")

st.write("Hello !")

x = st.slider(“Select an integer x”, 0, 10, 1)
y = st.slider(“Select an integer y”, 0, 10, 1)

df = pd.DataFrame({“x”: [x], “y”: [y] , “x - y”: [x - y]}, index = [“subtraction row”])
st.write(df)
