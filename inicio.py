#importacao das bibliotecas necessarias

import streamlit as st
from PIL import Image

#comeco do codigo
def app():
    
    st.title('EPOS')
    image = Image.open('logopp.jpg')
    st.image(image, use_column_width = True)
    st.header('Inicio')
    """Essa aplicação foi construida acreditando-se na necessidade uma ferrementa de facil acesso e ampla possibilidade de colaboração dos usuarios"""
    st.subheader('o que você encontrará aqui:')

    st.write('Nessa versão inicial, trazemos os calculos do centro de gravidade, centro de pressão, margem estatica e arrasto do foguete. Esses calculos foram construidos com base no trabalho de Barrowman, portanto, existem limitações para esses calculos que devem ser levadas em conta. dessa forma, aqui vão os pontos assumidos até então: ')

    st.write('1 - O regime de escoamento do ar considerado é incompressível')   
    st.write('2 - O angulo de ataque usado até então é igual a zero')
    st.write('3 - Não há formação de camada limite, pois não foi feito calculo relativo a isso ainda')
    st.write('4 - As forças de pressão sobre o corpo do foguete são iguais a 0')
    st.write('5 - Não há uma redução do dimetro do foguete em sua base')
    st.write('6 - O calculo do centro de Gravidade é feito quando ele está a uma velocidade de 0 m/s')
    st.write('7 - Ainda não foi feito um calculo da velocidade do foguete levando em consideração o empuxo gerado pelo motor')
    st.write('8 - A curvatura da terra não será levada em conta em vista do apogeu que pretende ser atingido(10000 pés)')



    st.subheader('O que há para o futuro?\n')
    st.write('Implementação de mais calculos\n')
    st.write('Sistema de saida de dados em forma de relatorio\n')
    st.write('Sistema de input de dados para agilizar os calculos')
    st.write('espero que essa aplicação seja muito util para nós como um todo')
    st.write('Desenvolvedor responsável: Paulo Vinicius Pimentel da Silva Camargo; Telefone: (12)996776894; e-mail: paulo.vine@usp.br')


