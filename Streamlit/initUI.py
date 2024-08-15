import streamlit as st
from obj import Retangulo

class UI:
    def Main():
        st.header('Cálculo com Retângulos')
        b = st.text_input('Base')
        h = st.text_input('Altura')
        if st.button('Calcular'):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(r.calcArea())
            st.write(r.calcDiagonal())