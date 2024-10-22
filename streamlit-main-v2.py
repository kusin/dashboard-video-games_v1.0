# library dashboard
import streamlit as st

# library manipulation data
import numpy as np
import pandas as pd

# library visualization data
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# import all function
from streamlit_dataset import *
from streamlit_visualization import *
# ----------------------------------------------------------------------------------------------------------------------

# config web streamlit
st.set_page_config(page_title="My Dasboard", layout="wide")

# container - header
st.markdown("## Data Visualization of Video Games Sales with Streamlit Framework")
# ----------------------------------------------------------------------------------------------------------------------

# container - total sales
st.info("Total Video Games Sales on Each Region")
col1, col2 = st.columns(2, gap="small")

# col1 - grouping by year
with col1:
  df_sales = time_series(get_dataset())
  st.pyplot(lineplot(dataset=df_sales, x="Year", y="Sales", title=""))

# col1 - grouping by region
with col2:
  df_sales = total_sales(get_dataset())
  st.pyplot(barplot(dataset=df_sales, x="Region", y="Sales", hue="Region", title=""))
  # ----------------------------------------------------------------------------------------------------------------------

# container-platform
st.info("Best platform of video games sales")
col1, col2 = st.columns(2, gap="small")

# col1 - platform
with col1:
  # grouping by platform
  df_platform = grouping_sales("Platform", get_dataset())
  df_platform = df_platform.head(3)
  st.pyplot(barplot(dataset=df_platform, x="Platform", y="Global_Sales", hue="Platform", title=""))

# col2 - platform
with col2:
  # grouping by platform
  df_platform = unpivot_sales("Platform", df_platform)
  st.pyplot(barplot(dataset=df_platform, x="Platform", y="Sales", hue="Region", title=""))
  # ----------------------------------------------------------------------------------------------------------------------

# container-genre
st.info("Best genre of video games sales")
col1, col2 = st.columns(2, gap="small")

# col1 - genre
with col1:
  # grouping by genre
  df_genre = grouping_sales("Genre", get_dataset())
  df_genre = df_genre.head(3)
  st.pyplot(barplot(dataset=df_genre, x="Genre", y="Global_Sales", hue="Genre", title=""))

# col2 - genre
with col2:
  # grouping by genre
  df_genre = unpivot_sales("Genre", df_genre)
  st.pyplot(barplot(dataset=df_genre, x="Genre", y="Sales", hue="Region", title=""))
  # ----------------------------------------------------------------------------------------------------------------------

# container-publisher
st.info("Best publisher of video games sales")
col1, col2 = st.columns(2, gap="small")

# col1 - publisher
with col1:
  # grouping by publisher
  df_publisher = grouping_sales("Publisher", get_dataset())
  df_publisher = df_publisher.head(3)
  st.pyplot(barplot(dataset=df_publisher, x="Publisher", y="Global_Sales", hue="Publisher", title=""))

# col2 - publisher
with col2:
  # grouping by publisher
  df_publisher = unpivot_sales("Publisher", df_publisher)
  st.pyplot(barplot(dataset=df_publisher, x="Publisher", y="Sales", hue="Region", title=""))
  # ----------------------------------------------------------------------------------------------------------------------