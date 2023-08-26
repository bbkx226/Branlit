import streamlit as st
from PIL import Image
import requests
import io

def main():
    st.set_page_config(page_title="Branlit", page_icon=":brain:") 

    st.markdown("<h1 style='text-align: center; color: green;'>Welcome to Branlit! 🧠</h1>", unsafe_allow_html=True)

    st.markdown("<h3>Why Branlit?</h3>", unsafe_allow_html=True)

    st.write("""
    I realized most students are trapped in a ChatGPT bubble. They use it for everything without realizing the vast AI world beyond! 
    ChatGPT is just one star in a galaxy of large language models. I wanted to shine a light on the endless possibilities.
    So I built Branlit as an AI playground - a one-stop shop to showcase different LLM features. Consider Branlit your AI tour guide! 
    Here, you can go beyond surface level ChatGPT queries. 
    """)

    st.write("""
    I designed Branlit to be an interactive learning tool. You can upload files, analyze data, and explore metrics.
    My goal is to nourish your inner curiosity. To give you those a-ha AI moments. To help you level up your skills.
    Branlit will expand your knowledge and unlock your potential. Let your inner genius flourish!
    So buckle up, get ready to geek out over AI, and let's begin the journey!
    """)

    st.markdown("---")

    st.markdown("<h3 style='text-align: center; color: green;'>Feature #1 - PDFPal 📚</h3>", unsafe_allow_html=True)

    st.write("""
    PDFPal allows you to upload multiple PDFs and ask questions about them. The AI will 
    process the PDFs and give you answers!
    """)

    st.write("""
    For example, say a student has an assignment but doesn't fully understand the requirements.  
    They can upload the assignment PDF and ask questions to clarify what needs to be done.
    """)

    st.markdown('> "I was totally confused by my essay assignment. The prompt was vague and the requirements confusing. I uploaded the PDF to PDFPal and asked it to explain the expectations and give tips. PDFPal clarified everything for me in simple steps - now I know exactly how to ace this essay!"')

    video_file = open('./files/pdfpal.mkv', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("---")

    # Feature 2 - BranHub
    st.markdown("<h3 style='text-align: center; color: green;'>Feature #2 - BranHub</h3>", unsafe_allow_html=True)

    st.write("""
    BranHub allows you to analyze and get insights from CSV data. Upload a CSV file and ask questions - 
    the AI will process the data and provide answers!
    """)

    st.write("""
    For a data analytics student working on a project, BranHub can help reveal trends and patterns they may have missed.
    They can upload their CSV dataset and ask questions to do deeper analysis.
    """)

    st.markdown('> "I was analyzing customer data for a class project and felt totally lost in the numbers. Then I discovered BranHub! I uploaded my CSV file and started asking questions. BranHub found insights I never would have seen on my own. It perfectly summarized retention drivers and churn predictors!"')

    video_file = open('./files/branhub.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("---")

    # Extra Feature - COVIDTrackr
    st.markdown("<h3 style='text-align: center; color: green;'>Extra Feature - COVIDTrackr</h3>", unsafe_allow_html=True)

    st.write("""
    COVIDTrackr is an analytics dashboard tracking COVID-19 data since 2020. It visualizes cases, deaths, and other metrics across countries and continents.
    """)

    st.write("""
    After 3 years of COVID-19 impacting the world, COVIDTrackr helps people understand the full timeline and situation globally. Users can explore the interactive dashboards to see different trends.
    """) 

    st.markdown('''<p style="color:red;">*Dataset used in this dashboard is only up to 23th Aug 2023</p>''', unsafe_allow_html=True)
    
    video_file = open('./files/covidtrackr.mkv', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.markdown("---")

    st.markdown("<h3 style='text-align: center; color: green;'>You're not satisfied with these?</h3>", unsafe_allow_html=True)
    st.write("""
    Check out my other projects that have harnessed the power of Large Language Models (LLMs). 
    Explore the AI world beyond Branlit!
    """)

    # Create a 2x2 grid layout for buttons
    col1, col2 = st.columns(2)  # Two columns for two rows of buttons

    # Button 1
    with col1:
        st.markdown(
            """
            <a href='https://brandongpt-summarizer.web.app/' class='custom-button' style='text-decoration: none;'>
                <img src='./files/aisummarizer.png' class='button-image'/>
                <p class='button-text'>Articles Summarizer</p>
            </a>
            """
            , unsafe_allow_html=True)

    # Button 2
    with col2:
        st.markdown(
            """
            <a href='https://imagegeneratorai-6e92d.web.app/' class='custom-button' style='text-decoration: none;'>
                <img src='./files/aimage.png' class='button-image'/>
                <p class='button-text'>AI Image Generator</p>
            </a>
            """
            , unsafe_allow_html=True)

    # Button 3
    with col1:
        st.markdown(
            """
            <a href='https://quizbraniac.vercel.app/' class='custom-button' style='text-decoration: none;'>
                <img src='./files/quizbraniacbg.png' class='button-image'/>
                <p class='button-text'>QuizBraniac</p>
            </a>
            """
            , unsafe_allow_html=True)

    # Button 4
    with col2:
        st.markdown(
            """
            <a href='https://ai-verse.vercel.app/' class='custom-button' style='text-decoration: none;'>
                <img src='./files/ai.png' class='button-image'/>
                <p class='button-text'>AI-verse Community</p>
            </a>
            """
            , unsafe_allow_html=True)

if __name__ == '__main__':
    main()