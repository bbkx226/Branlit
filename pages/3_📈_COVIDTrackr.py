import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import os
import warnings

warnings.filterwarnings("ignore")

def main():

    st.set_page_config(page_title="COVIDTrackr", page_icon="📈", layout="wide")
    st.title(" 📈 COVIDTrackr")
    st.header("Together, We Analyze, Together, We Defeat. 🔬")
    st.write("""---""") 
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

    df = pd.read_csv("./files/covid-data.csv", encoding = "ISO-8859-1")

    col1, col2 = st.columns((2))
    df["date"] = pd.to_datetime(df["date"])

    # Getting the min and max date 
    startDate = pd.to_datetime(df["date"]).min()
    endDate = pd.to_datetime(df["date"]).max()

    with col1:
        date1 = pd.to_datetime(st.date_input("Start Date", startDate))

    with col2:
        date2 = pd.to_datetime(st.date_input("End Date", endDate))

    df = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()

    df = df[df["location"] != "World"].copy()
    df = df[df['continent'].notnull()].copy()

    st.sidebar.header("Choose your filter: ")
    continent = st.sidebar.multiselect("Pick Your Continent", df["continent"].unique())
    if not continent:
        df2 =df.copy()
    else:
        df2 = df[df["continent"].isin(continent)].copy()

    location = st.sidebar.multiselect("Pick Your Location", df2["location"].unique())
    if not location:
        df3 = df2.copy()
    else:
        df3 = df2[df2["location"].isin(location)].copy()

    if not continent and not location:
        filtered_df = df
    elif not continent:
        filtered_df = df[df["location"].isin(location)]
    elif not location:
        filtered_df = df[df["continent"].isin(continent)]
    else:
        filtered_df = df3[df3["continent"].isin(continent) & df3['location'].isin(location)] 

    # Filter out null continents
    filtered_df = filtered_df[filtered_df['continent'].notnull()] 

    filtered_df['month_year'] = filtered_df['date'].dt.to_period('M')

    end_location_df = filtered_df.groupby('location').apply(lambda group: group[group['date'] == group['date'].max()])
    start_location_df = filtered_df.groupby('location').apply(lambda group: group[group['date'] == group['date'].min()])

    end_location_df['total_cases'] = end_location_df['total_cases'].fillna(0)
    start_location_df['total_cases'] = start_location_df['total_cases'].fillna(0)

    end_location_df = end_location_df.reset_index(drop=True)
    start_location_df = start_location_df.reset_index(drop=True)

    location_df = pd.merge(end_location_df, start_location_df, on='location')

    location_df['total_cases_end'] = location_df['total_cases_x'] 
    location_df['total_cases_start'] = location_df['total_cases_y']
    location_df['total_cases_change'] = location_df['total_cases_end'] - location_df['total_cases_start']

    st.subheader("Location wise Cases")
    fig = px.bar(location_df, x = "location", y = "total_cases_change", color = "location", template="seaborn")
    st.plotly_chart(fig, use_container_width=True, height=200)

    continent_df = filtered_df.groupby('continent').apply(lambda group: group[group['date'] == group['date'].max()])

    st.subheader("Continent wise Cases")
    fig = px.pie(continent_df, values = "total_cases", names = "continent", hole = 0.5)
    fig.update_traces(text = continent_df["continent"], textposition = "outside")
    st.plotly_chart(fig,use_container_width=True)

    st.subheader('Time Series Analysis')
    monthly_cases = filtered_df.groupby(['month_year', 'location'])['total_cases'].last().reset_index()
    linechart = pd.DataFrame(monthly_cases.groupby(monthly_cases["month_year"].dt.strftime("%Y : %b"))["total_cases"].sum()).reset_index()
    linechart = linechart.sort_values(by = "total_cases")
    fig2 = px.line(linechart, x = "month_year", y="total_cases", labels = {"total_cases": "Cases"},height=500, width = 1000,template="gridon")
    st.plotly_chart(fig2,use_container_width=True)    

    st.subheader("Hierarchical view of Cases using TreeMap")
    fig3 = px.treemap(location_df, path = ["continent","location", "total_deaths"], values = "total_deaths", hover_data = ["total_deaths"],
                    color = "total_cases")
    fig3.update_layout(width = 800, height = 650)
    st.plotly_chart(fig3, use_container_width=True)

if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()