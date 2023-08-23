import streamlit as st

def main():
    st.set_page_config(page_title="PDFPal", page_icon=":books:")

    st.header("Chat with multiple PDFs at once :books:")
    st.text_input("Ask question about your documents:")

    with st.sidebar:
        st.subheader('Your documents')
        st.file_uploader("Upload your PDFs here and click on Process")
        st.button("Process")

if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()