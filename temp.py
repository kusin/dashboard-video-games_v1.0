# library dashboard
import streamlit as st

# library manipulation data
import numpy as np
import pandas as pd

# library visualization data
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# func get_dataset
def get_dataset():
  
  # load dataset
  dataset = pd.read_csv("dataset/vgsales.csv")
  
  # return values
  return dataset



# config web streamlit
st.set_page_config(page_title="My Dasboard", layout="wide")

# container - header
st.markdown("## Data Visualization of Video Games Sales with Streamlit Framework")

# container - total sales
st.info("")
col1, col2 = st.columns(2, gap="small")

# col1 - total sales
with col1:
  st.text("Columns 1")

# col2 - total sales
with col2:
  st.text("Columns 2")
  # -------------------------------------------------------------------------------

# container - ...
st.info("")
col1, col2, col3 = st.columns(3, gap="small")

# col1 - ...
with col1:
  st.text("Columns 1")

# col2 - ...
with col2:
  st.text("Columns 2")

# col3 - ...
with col3:
  st.text("Columns 3")
  # -------------------------------------------------------------------------------