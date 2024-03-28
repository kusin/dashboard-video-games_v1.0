# import library streamlit
import streamlit as st;

# library manipulation dataset
import pandas as pd

# library manipulation array
import numpy as np

# library data visualization
import plotly.express as px

# config web streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
    }
)

# load dataset
dataset = pd.read_csv("dataset/vgsales.csv")

# container-header
with st.container():
    st.markdown("## Data Science - Exploratory Data Analysis of Video Games Sales")
    st.markdown("- Created By. Aryajaya Alamsyah, Okt 2023 (link download on https://www.kaggle.com/datasets/gregorut/videogamesales)")

# container-dataset
with st.container():
    st.dataframe(dataset, use_container_width=True)

# container-sales video games
with st.container():
    # labels
    st.error("Sum of video games sales from all regions")
    
    # load history sales video games on global region
    df = dataset.groupby(by=['Year'])['Global_Sales'].sum().reset_index()
    df = df.sort_values(by="Year")
    
    # visualization lineplot
    fig = px.line(df, x="Year", y="Global_Sales")
    fig.update_traces(
        line_color="#67001f",
        line_width=2.5,
    )
    fig.update_layout(
        title = "History video games sales on global region",
        xaxis_title = "Year Sales",
        yaxis_title = "Sum of Sales Video",
    )
    st.plotly_chart(fig,use_container_width=True)

    # Sum video games sales on all region
    df = dataset[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].aggregate("sum").sort_values(ascending=False).reset_index()
    df.columns = ["Region", "Sales"]
    
    # visualization of sum video games sales
    col1, col2 = st.columns([1,1], gap="large")
    with col1:
        # show pieplot
        fig = px.pie(
            df, labels="Region", values="Sales", hole=0.25
        )
        fig.update_traces(
            marker=dict(colors=px.colors.diverging.RdBu, line=dict(color='#FFFFFF', width=2))
        )
        fig.update_layout(
            title = "Sales Video Games by Region",
            legend=dict(orientation='h', x=0.05, y=0.0),
            showlegend=True,
        )
        st.plotly_chart(fig,use_container_width=True)
    with col2:
        # show barplot
        fig = px.bar(
            df, x="Region", y="Sales", text_auto='.3s' 
        )
        fig.update_traces(
            marker_color = px.colors.diverging.RdYlBu
        )
        fig.update_layout(
            title = "Sales Video Games by Region",
            xaxis_title = "Region Sales",
            yaxis_title = "Sum of Sales Video",
        )
        st.plotly_chart(fig, use_container_width=True)

# container-best game, platform, genre, publisher
with st.container():
    # labels
    st.error("Best of Game, Platform, Genre, Publisher on All Region")

    # func groupBarplot
    def barplot(column, title, xlabel, ylabel):
        
        # grouping on pandas 
        sales_by_column = dataset.groupby(column)[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].aggregate("sum").sort_values(by=['Global_Sales'],ascending=[False]).head(5).reset_index()
        
        # show barplot
        fig = px.bar(sales_by_column, x=column, y=['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'], barmode='group')
        
        colors = {
            'NA_Sales': 'rgb(165,0,38)', 
            'EU_Sales': 'rgb(215,48,39)', 
            'JP_Sales': 'rgb(244,109,67)', 
            'Other_Sales': 'rgb(253,174,97)'
        }
        for i, col in enumerate(['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']):
            fig.update_traces(marker_color=colors[col], selector=dict(name=col), name=f'{col.split("_")[0]} Sales')

        fig.update_layout(
            title=title,
            xaxis_title=xlabel,
            yaxis_title=ylabel,
            xaxis=dict(tickangle=0),
            yaxis=dict(tickangle=0),
            legend=dict(title='', orientation='h', yanchor='top', y=1.05, xanchor='center', x=0.5)
        )
        return fig
    
    # visualization of best game, platform, genre, publisher
    col1, col2 = st.columns(2, gap="large")
    with col1:
        col1.plotly_chart(
            barplot(
                'Name',
                'Top 5 of game on all regions', 
                'Game name', 
                'Sum of Video Games'
            ), use_container_width=True
        )
    with col2:
        col2.plotly_chart(
            barplot(
                'Platform',
                'Top 5 of platform on all regions', 
                'Platform name', 
                'Sum of Video Games'
            ), use_container_width=True
        )

    # visualization of best game, platform, genre, publisher
    col1, col2 = st.columns(2, gap="large")
    with col1:
        col1.plotly_chart(
            barplot(
                'Genre',
                'Top 5 of genre on all regions', 
                'Genre name', 
                'Sum of Video Games'
            ), use_container_width=True
        )
    with col2:
        col2.plotly_chart(
            barplot(
                'Publisher',
                'Top 5 of publisher on all regions', 
                'Publisher name', 
                'Sum of Video Games'
            ), use_container_width=True
        )