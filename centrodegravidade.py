import streamlit as st
import pandas as pd
import meu_modulo as mm 
import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
def app ():
    st.title('Centro de Gravidade')
    st.subheader('Nesta seção será possivel calcular o centro de gravidade do seu foguete!')
    st.write('É o ponto onde todo o peso do foguete está concentrado, portanto, se você apoiar o foguete no seu dedo sobre esse ponto, ele ficará em equilíbrio. O peso mencionado anteriormente é o somatório de todos os pesos dos componentes do foguete e, portanto, podemos afirmar que a posição do CG está relacionada com a distribuição do peso e não com o peso em si. O CG é de suma importância para a estabilidade durante o voo, pois o foguete irá girar somente em torno do centro de gravidade e se houver momento. Podemos calculá-lo a partir da seguinte equação:')
    image0 = Image.open('centrodegravidade.jpg')
    st.image(image0,caption = 'Esquema de forças de pressão sobre o foguete e forças de pressão')
    #aqui começamos a parte importante do codigo para esta seção:
    #começando com os valores de entrada

   
    
    st.header('Valores de entrada:')
    st.subheader('Valores de massa:')
    st.write('Note que você só precisa inserir as medidas de uma das aletas')
    st.write('Na parte de pesos certifique-se de especificar o peso de cada componente do foguete juntamente com as partes internas dele, ex: circuitos, recuperação, motor juntamente com o peso do propelente etc...')
    st.subheader('Componentes externos')
   
    #massas
    Coifa = st.number_input('Insira a massa da Coifa em Gramas')
    st.write('A massa da Coifa é: ', Coifa)
    
    Corpo1 =st.number_input('Insira a massa do Corpo 1 em Gramas')
    st.write('A massa do corpo 1 é  ', Corpo1)
    
    Corpo2 =st.number_input('Insira a massa do Corpo 2 em Gramas')
    st.write('A massa do corpo 2 é  ', Corpo2)
    
    Motor =st.number_input('Insira a massa do Motor em Gramas')
    st.write('A massa do Motor(sem o propelente) é:', Motor)
    
    Aleta1 =st.number_input('Insira a massa da Aleta1')
    st.write('A massa da Aleta1 é:', Aleta1)
    
    Propelente = st.number_input('Massa do propelente')
    st.write(f'A massa do Propelente é: {Propelente}')
    
    st.subheader('Componentes internos')
    st.write('note que o nome anel centralizador quer dizer na verdade, acoplador. me desculpe foi um erro aqui')
    
    
    AnelCentralizador = st.number_input('Insira a massa do anel centralizador')
    st.write('A massa do anel centralizador é: ',AnelCentralizador)
    
    BulkHead = st.number_input('Insira a massa do bulkhead')
    st.write('A massa do BulKhead é: ',BulkHead)
    #comprimentos
    st.header('Comprimento')#colocando so um titulo para separar as coisas de uma forma mais organizada
    
    
    Coifa_dis =st.number_input('Insira o Comprimento da Coifa')
    st.write('Comprimento da Coifa: ', Coifa_dis)
    
    Corpo1_dis =st.number_input('Insira o Comprimento do Corpo1: ')
    st.write('Comprimento do Corpo1: ', Corpo1_dis)
    
    Corpo2_dis =st.number_input('Insira o Comprimento do Corpo2')
    st.write('Comprimento do Corpo2: ', Corpo2_dis)
    
    Motor_dis =st.number_input('Insira o Comprimento do Corpo do Motor')
    st.write('Comprimento do Motor: ', Motor_dis)
    
    Aleta1_dis =st.number_input('Insira o Comprimento da base maior das Aletas')
    st.write('Comprimento da Aleta: ', Aleta1_dis)
    
    TudoCerto = st.checkbox('Calcular  o CG')#isso aqui é uma check box que caso seja marcada ira executar o codigo a seguir
    
    #atribuindo a massa do Propelente ao motor:
    Motor +=Propelente
    
    if TudoCerto:
        st.write('O valor do CG é: ',(mm.CG( Coifa,Corpo1,Corpo2,Motor,Aleta1,Coifa_dis,Corpo1_dis, Corpo2_dis,Motor_dis,Aleta1_dis,AnelCentralizador,BulkHead)/10))
        cg = mm.CG(Coifa , Corpo1, Corpo2,  Motor, Aleta1 , Coifa_dis,Corpo1_dis,Corpo2_dis,Motor_dis,Aleta1_dis,AnelCentralizador,BulkHead)

        
    #iremos fazer o grafico agora, só que de uma forma mais inteligente, usando um array!
    TudoCerto1 = st.checkbox('Calcular o Grafico do CG conforme a massa de propelente é queimada')#isso aqui é uma check box que caso seja marcada ira executar o codigo a seguir
   
    y = 0

    if TudoCerto1:
        Motor = np.array(np.linspace(Motor - Propelente,Motor + Propelente,100))
        y = mm.CG(Coifa , Corpo1, Corpo2,  Motor, Aleta1 , Coifa_dis,Corpo1_dis,Corpo2_dis,Motor_dis,Aleta1_dis,AnelCentralizador,BulkHead) 
        df = pd.DataFrame({'Massa_do_Motor': Motor, 'Centro_de_Gravidade': y})
        from bokeh.plotting import figure
        p = figure(
        title='Variação do Centro de Gravidade de acordo com a diminuição da massa do motor',
  x_axis_label='Massa',
  y_axis_label='CG')
        p.line(Motor, y, legend_label = 'Tendencia', line_width=2)
        st.bokeh_chart(p, use_container_width=True)
    
# criar agora uma parte para salvar os resultados
#este é um comentario teste
