import streamlit as st
from multiapp import MultiApp
import demo

app = MultiApp()
st.set_page_config(page_title="AttnGAN", initial_sidebar_state="auto")

st.sidebar.title("T2I")
# Add all application here

app.add_app("T2I Explained", demo.attngan_explained)
app.add_app("Demo - CUB", demo.demo_gan)
app.add_app("Demo - COCO",demo.demo_coco)



# The main app
app.run()
