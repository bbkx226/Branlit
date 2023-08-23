import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    text = ""
    for pdf_doc in pdf_docs:
        pdf_reader = PdfReader(pdf_doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    # To ensure the model gets the meaning of the full sentence
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain

def handle_userinput(user_question):

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():

    load_dotenv() # load environment variables from a .env file
    
    press_button = False

    st.set_page_config(page_title="PDFPal", page_icon="📚")
    # https://i.postimg.cc/P5phFqqh/bot.png
    st.write(css, unsafe_allow_html=True)

    st.markdown("# PDFPal")
    st.sidebar.header("PDFPal")

    if "conversation" not in st.session_state: st.session_state.conversation = None

    if "chat_history" not in st.session_state: st.session_state.chat_history = None

    if "process_pressed" not in st.session_state: st.session_state.process_pressed = False
    
    st.header("Ask anything. Know everything. :brain:")
    st.write("""---""") 
    st.subheader('Your PDFs')
    
    pdf_docs = st.file_uploader("Drop files, click Process, watch our AI work its magic!", accept_multiple_files=True)

    if pdf_docs:
        press_button = st.button("Process")

    if press_button:
        with st.spinner("Processing your documents..."):
            # Get PDF text
            raw_text = get_pdf_text(pdf_docs)

            # Get the text chunks
            text_chunks = get_text_chunks(raw_text)

            # Create Vector Store
            vectorstore = get_vectorstore(text_chunks)

            # Create Conversation chain
            st.session_state.conversation = get_conversation_chain(vectorstore)

            st.session_state.process_pressed = True

    if st.session_state.process_pressed:   
        user_question = st.text_input("Pick the brain of your PDFs:", placeholder="Ask me anything...")
        if user_question: 
            handle_userinput(user_question)

if __name__ == '__main__': # define code that should only run when the script is executed directly
    main()