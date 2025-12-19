import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image
import os

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

city = pd.DataFrame({
    'awesome cities' : ['Chicago','Minneapolis','Louisville','Topeka'],
    'lat' : [41.868171, 44.979840, 38.257972, 39.030575],
    'lon' : [-87.667458, -93.272474, -85.765187, -95.702548]
})

st.title("Streamlit Charts Demo")

st.subheader("Map")
st.map(city)

st.subheader("Flow Chart")
st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch                                   }
 """)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a', y= 'b',tooltip = ['a','b']
)
st.subheader("Altair Chart")
st.altair_chart(chart)

fig, ax = plt.subplots()  

ax.scatter(data['a'], data['b'])
ax.set_title("Scatter Plot (a vs b)")
ax.set_xlabel("a")
ax.set_ylabel("b")

st.pyplot(fig)  

st.subheader("Line Chart")
st.line_chart(data)

st.subheader("Area Chart")
st.area_chart(data)

st.subheader("Bar Chart")
st.bar_chart(data)

st.subheader("Image")

BASE_DIR = os.path.dirname(__file__)
img_path = os.path.join(BASE_DIR, "sal.jpg")

if os.path.exists(img_path):
    img = Image.open(img_path)
    st.image(img, caption="Sample Image", use_container_width=True)
else:
    st.error("Image 'sal.jpg' not found in Streamlit folder")

st.subheader("Video")
st.components.v1.iframe(
    "https://www.youtube.com/embed/videoseries?list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5",
    width=800,
    height=450
)