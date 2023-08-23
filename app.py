import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    text = ""
    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



def main():
    load_dotenv()
    st.set_page_config(page_title="PDFPal", page_icon=":books:")

    st.header("Chat with multiple PDFs at once :books:")
    st.text_input("Ask question about your documents:")

    with st.sidebar:
        st.subheader('Your documents')
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing your documents..."):
                # Get PDF text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # Get the text chunks


                # Create Vector Store



if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()