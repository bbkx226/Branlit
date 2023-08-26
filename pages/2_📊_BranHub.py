from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib
import matplotlib.pyplot as plt
import warnings
import glob  # Import glob to work with file paths
import os.path  # Import os.path to handle file paths

warnings.filterwarnings("ignore")

def main():
    load_dotenv()
    matplotlib.use('TkAgg')
    API_KEY = os.environ["OPENAI_API_KEY"]
    llm = OpenAI(api_token=API_KEY)
    pandas_ai = PandasAI(llm, save_charts=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(page_title="BranHub", page_icon="📊")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
    st.title("📊 BranHub: The AI Data Analyst")
    st.header("PDFs In, Answers Out! ⚡")
    st.write("""---""") 

    # Define your file path and folder
    graph_folder_path = "./exports/charts/"  # Update with the correct folder path
    count_files = len(glob.glob(os.path.join(graph_folder_path, '*.png')))  # Count the PNG files

    with open("./files/covid-data.csv", "rb") as file:
        st.download_button(
            label="Download CSV",
            data=file,
            file_name="covid-data.csv",
        )

    st.markdown('''<p style="color:red;">CSV got you down? Lift your spirits with our phenomenal COVID data!</p>''', unsafe_allow_html=True)

    st.subheader('Your CSV')
    uploaded_file = st.file_uploader(":file_folder: Upload a CSV file for analysis", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(5))
        st.write("""---""") 
        prompt = st.text_area("Enter your prompt:")

        if st.button("Generate"):
            if prompt:
                with st.spinner("Generating response..."):
                    answer = pandas_ai.run(df,prompt)
                    current_file_count = len(glob.glob(os.path.join(graph_folder_path, '*.png')))  # Count the PNG files again
                    if current_file_count > count_files:
                        count_files = current_file_count
                        st.write(answer)
                        list_of_files = glob.glob(os.path.join(graph_folder_path, '*.png')) 
                        st.write(list_of_files)
                        latest_file = max(list_of_files, key=os.path.getctime)
                        st.image(latest_file)
                    else:
                        st.write(answer)
            else:
                st.warning("Please enter a prompt.")
                
if __name__ == '__main__':
    main()
