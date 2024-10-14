# library dashboard
import streamlit as st

# library visualization
import plotly.express as px

# library manipulation data
import numpy as np
import pandas as pd

# config web streamlit
st.set_page_config(page_title="Video Games Sales",layout="wide")

# container-header
st.markdown("## Dashboard of Video Games Sales Using Framework Streamlit")

# load dataset
dataset = pd.read_csv("dataset/vgsales.csv")

# container games-sales
st.info("Exploration Data Analysis on Games Sales")
col1, col2 = st.columns([0.5,0.5], gap="small")

# calculate global-sales
df = dataset[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].aggregate("sum").sort_values(ascending=True).reset_index()
df.columns = ["Region", "Sales"]

# create Barplot
with col1:
  fig = px.bar(df, y="Region", x="Sales", text_auto='.4s')
  fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
  fig.update_layout(title="Sum of games sales by regions", xaxis_title="", yaxis_title="")
  st.plotly_chart(fig)

# create pieplot
with col2:
  fig = px.pie(df, values="Sales", names="Region", hole=0.5, color_discrete_sequence=px.colors.sequential.Bluyl_r)
  fig.update_traces(textinfo="percent")
  fig.update_layout(title="Percentage of games sales by region")
  st.plotly_chart(fig)

# container games-sales
st.info("Exploration Data Analysis on Global Sales")
col1, col2, col3, col4 = st.columns([0.25,0.25,0.25,0.25], gap="small")

# Best Platform
with col1:

  # calculate platform name
  df = dataset.groupby("Platform")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum")
  df = df.sort_values(by=["Global_Sales"]).reset_index().tail(3)

  # create barplot  
  fig = px.bar(df, x="Platform", y="Global_Sales", text_auto='.4s')
  fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
  fig.update_layout(title="Best paltform by regions", xaxis_title="", yaxis_title="")
  st.plotly_chart(fig)

# Best Genre
with col2:

  # calculate genre name
  df = dataset.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum")
  df = df.sort_values(by=["Global_Sales"]).reset_index().tail(3)

  # create barplot  
  fig = px.bar(df, x="Genre", y="Global_Sales", text_auto='.4s')
  fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
  fig.update_layout(title="Best genre by regions", xaxis_title="", yaxis_title="")
  st.plotly_chart(fig)

# Best Publisher
with col3:

  # calculate publisher name
  df = dataset.groupby("Publisher")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum")
  df = df.sort_values(by=["Global_Sales"]).reset_index().tail(3)

  # create barplot  
  fig = px.bar(df, x="Publisher", y="Global_Sales", text_auto='.4s')
  fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
  fig.update_layout(title="Best publisher by regions", xaxis_title="", yaxis_title="")
  st.plotly_chart(fig)

with col4:
  df = dataset.groupby("Name")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum")
  df = df.sort_values(by=["Global_Sales"]).reset_index().tail(3)

  fig = px.bar(df, x="Name", y="Global_Sales", text_auto='.4s')
  fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
  fig.update_layout(title="Best games by regions", xaxis_title="", yaxis_title="")
  st.plotly_chart(fig)