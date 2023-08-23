from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

def main():
    load_dotenv()

    API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(api_token=API_KEY)
    pandas_ai = PandasAI(llm)

    st.title("Prompt-driven analysis with PandasAI")

    uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(3))
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                st.write("PandasAI is generating an answer, please wait...")
                pandas_ai.run(df, prompt=prompt)
            else:
                st.warning("Please enter a prompt.")
if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()