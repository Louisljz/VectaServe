import streamlit as st
from langchain.vectorstores import Vectara

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

st.set_page_config('Home', '📖')
st.title('Docusphere HomePage 📖')

customer_id = st.text_input('Customer ID')
corpus_id = st.text_input('Corpus ID')
api_key = st.text_input('API Key')

if customer_id and corpus_id and api_key:
    st.session_state.vector_store = Vectara(customer_id, corpus_id, api_key)
st.info('Ensure you have entered the correct credentials, or else the CS bot cannot retrieve any information.')
