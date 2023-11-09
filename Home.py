import streamlit as st
from langchain.vectorstores import Vectara

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

st.set_page_config('Home', '📖')
st.title('VectaServe HomePage 📖')
st.info('Please verify your credentials to enable the Customer Service bot to retrieve information from your VectaraDB.')

customer_id = st.text_input('Customer ID')
corpus_id = st.text_input('Corpus ID')
api_key = st.text_input('API Key')

if customer_id and corpus_id and api_key:
    st.session_state.vector_store = Vectara(customer_id, corpus_id, api_key)
