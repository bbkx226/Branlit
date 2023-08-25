from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

def main():
    
    load_dotenv()
    matplotlib.use('TkAgg')
    API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(api_token=API_KEY)
    pandas_ai = PandasAI(llm)

    st.set_page_config(page_title="BranHub", page_icon="📊")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    st.title("📊 BranHub: The AI Data Analyst")
    st.header("PDFs In, Answers Out! ⚡")
    st.write("""---""") 
    st.subheader('Your CSV')
    uploaded_file = st.file_uploader(":file_folder: Upload a CSV file for analysis", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(5))
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    answer = pandas_ai.run(df,prompt)
                    fig_number = plt.get_fignums()
                    if fig_number:
                        st.pyplot(plt.gcf())
                    else:
                        st.write(answer)
            else:
                st.warning("Please enter a prompt.")
                
if __name__ == '__main__':
    main()