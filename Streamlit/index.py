import streamlit as st
from initUI import UI

st.header('POO em Python com Streamlit')

if st.button('Clique aqui'):
    st.write('Olá, Mundo! Bem-vindo(a) ao Streamlit!')

UI.Main()