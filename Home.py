import streamlit as st
from langchain.vectorstores import Vectara

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

st.set_page_config('Home', '📖')
st.title('VectaServe HomePage 📖')
msg = st.empty()
msg.info('There is no implemented method for credential authentication from Vectara, so ensure that you enter the correct details for this app to work.')

customer_id = st.text_input('Customer ID')
corpus_id = st.text_input('Corpus ID')
api_key = st.text_input('API Key')

if customer_id and corpus_id and api_key:
    st.session_state.vector_store = Vectara(customer_id, corpus_id, api_key)
    msg.success('Credentials submitted to Vectara! Try ingest or query endpoints to confirm the connection.')
