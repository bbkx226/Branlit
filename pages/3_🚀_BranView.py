import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings

warnings.filterwarnings("ignore")

def main():

    st.set_page_config(page_title="BranView", page_icon=":rocket:")
    st.title(" :rocket: Coronavirus EDA")

if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()