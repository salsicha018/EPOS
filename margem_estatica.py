
#importar do centro de gravidade o valor que é salvo na variavel CG

#importar do centro de pressão o valor que é salvo na variavel CP 

#pegar esses dois valores e calcular a margem estatica do foguete 

#uma coisa que pde ser feita é levar em consideraçao o movimento que o cg e cp fazem quando o foguete queima combustivel, ou seja ele acelera
#e tentar construir um grafico da variação da margem estatica em uma possivel situaçao de voo



#docstring a respeito da margem estatica. 
import streamlit as st

import meu_modulo as mm 
def app():
    #função para criar a aplicação de forma vazia

    st.title('Margem Estática: ')

    '''
    do se pensa em projetar um Foguete, assim como é necessario saber o ponto de equilibrio dele, ou seja, onde todas as forças de peso de concentramtambem é preciso saber onde as forças de pressão estã concentradas
    Como já vimos antes, dessas duas linhas acima, estraimos o centro de gravidade e o centro de pressão 
    Mas, mais necessario do que saber onde esses centros estão localizados, é necessario saber o quão estavel é o foguete que esta se projetando. 
    Quando um foguete esta em voo, ele esta sujeito a forças de pressão, de gravidade, de arrasto, vindas do vento e etc... Quando o vento bate no corpo do foguete:
    ocorre a ação de uma força que tem a itensidade medida por uma constante vezes a velocidade do vento. essa força provoca um torque no foguete que começa não 
    pela ponta do foguete mas sim pelo centro de gravidade dele, e esse braço se estende até onde o centro de gravidade se localiza, porque essa interação com o vento 
    muda a forma como o foguete voa no ar, o que muda nesse ponto, quando por exemplo o foguete sofre uma rajada de ar: é que ele sai de sua trajetoria de voo,
    e isso por meio de uma inclinação que é descrita pelo angulo de ataque, na literatura denotado pela letra grega alfa. 
    e quando isso acontece, o que garante que o foguete continue seu voo de maneira segura, isto é, um fator que ajuda na restauraçao da trajetoria do foguete é 
    a margem estatica. Essa margem estatica é medidaem termos de calibre [cal] = diametro do foguete. Barrowman, em seu trabalho descreve que uma boa margem estatica 
    esta entre 1,5 e 2,0 cal. sendo assim, ter conhecimento dessa medida é fundamental para o voo do foguete. 

    '''
    #st.write('A margem estatica é uma medida referente a estabilidade do foguete. É obtida a partir da ')
    #from centrodegravidade import cg# esse valor so sera importado caso o valor do centro de gravidade seja definido conforme  temos no arquivo referente a ele 
    #from centrodepressao import Xcp # o mesmo ocorre aqui, só que o problema é manter esse valor salvo depois que se muda de uma pagina para outra
    st.write('Para seguir com o calculo da margem estatica, certifique-se de estar com o valor do Cg e do Cp em mãos')

    #input dos valores do CG e CP:

    CG = st.number_input('Insira o valor do CG')
    st.write('CG: ',CG)
    CP = st.number_input('Insira o valor do CP')
    st.write('CP: ',CP)
    d = st.number_input('Insira o valor do diametro do Foguete')
    st.write('diametro: ', d)
   
    #adicionando um botão para executar uma ação
    
    botao = st.button('Calcular margem estatica')
    if botao:
        Margem_estatica = mm.Margemestatica(CG,CP,d)
        st.write(f' Margem estatica = {Margem_estatica} cal')
    

    

    

    
    pass
