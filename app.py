#aplicação principal 

import centrodegravidade
import centrodepressao
import arrasto
import streamlit as st 
import pandas as pd 
import meu_modulo as mm
import margem_estatica 
PAGES = {"Centro de Gravidade": centrodegravidade,
         "Centro de Pressão": centrodepressao,
         "Arrasto": arrasto,
         "Margem Estatica": margem_estatica}


st.sidebar.title('Navegação')
selection = st.sidebar.radio("Ir para", list(PAGES.keys()))
page = PAGES[selection]
page.app()
