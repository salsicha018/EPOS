import streamlit as st
import meu_modulo as mm
def app ():
    st.title('Centro de Pressão')
    st.write('Nessa seção será possível calcular o Centro de pressão:')
    st.write('O centro de pressão é similar ao centro de gravidade, a única diferença é que as forças envolvidas são as forças de pressão do ar agindo sobre o foguete quando ele está voando. Fundamentalmente, pode-se dizer que o centro de pressão é o ponto onde todas as forças aerodinâmicas agem durante o voo. Na imagem abaixo vemos a distribuição das forças que agem ao longo do corpo do foguete.')
             
    st.write('O calculo a seguir é feito de acordo com o que foi postulado por Barrowman, no arquivo Calculating the center of Pressure of a Rocket os Postulados podem ser encontrados')         
             
             
             
    st.subheader('Modelo de coifa')
    option = st.selectbox('Selecione o tipo de coifa para o seu projeto',('Conica', 'Ogival', 'Parabolico','Elíptica'))
    st.write('Você selecionou:', option)
    #valores de entrada
             
    st.subheader('Comprimento e Diâmetro do foguete ')
    st.write('Coloque os valores numéricos em unidades de Metro')
    #comprimento total do foguete
    Lc = st.number_input('Insira o comprimento da coifa')
    st.write('O comprimento da Coifa é: ', Lc)
    L = st.number_input('Insira o comprimento total do foguete: ')
    st.write('O comprimento total do foguete é: ', L)
    #diametro do foguete    
    d = st.number_input('insira o diametro do seu foguete: ')
    st.write('O diametro do foguete é: ')
    #parametros da aleta
    st.subheader('Parametros da Aleta')
    
    st.subheader('Nomenclatura das Variaveis a seguir')
    
    st.write('Tf : espessura das aletas\n')
    st.write('a : é o comprimento da lateral mais longa\n')
    st.write('s : é a distancia entre as laterais\n')
    st.write('b : é a altura da lateral externa\n')
    st.write('m : é a diferença da lateral maior para a lateral menor \n')
    st.write('l : é o comprimento da linha que passa pela parte central da aleta\n')
    st.write('observação: ainda n temos uma função para o valor de l, então ele deve ser calculado manualmente\n')
    Tf =st.number_input('Insira o valor de "Tf": ')
    st.write('Tf = ',Tf)
    a = st.number_input('Insira o valor de "a": ')
    st.write('a = ',a)
    b = st.number_input('Insira o valor de "b": ')
    st.write('b = ',b)
    s = st.number_input('Insira o valor de "s": ')
    st.write('s = ',s)
    m = st.number_input('Insira o valor de "m": ')
    st.write('m = ',m)
    l = st.number_input('Insira o valor de "l": ')
    st.write('l = ',l)
    st.write('A seguir escolha quantas aletas você deseja para o seu foguete')
    o = st.selectbox('Selecione o numero de aletas do seu foguete', ( '3','4' ) )
    st.write('Você selecionou:', o)
    if o == '3':#atribui um valor para n assim que o usuario faz a escolha
        n = int(3)
    else: 
        n = int(4)
             
    TudoCerto3 = st.checkbox('Calcular CP')
    if TudoCerto3:
        st.write('Great!')
        #então aqui temos a função do centro de pressão de acordo com o que foi escolhido 
        if option == 'Conica':
            Xn = mm.coifaconica(Lc)
        elif option == 'Ogival':
            Xn = mm.coifaogival(Lc)
        elif option == 'Parabolico':
            Xn = mm.coifaparabolica(Lc)
        elif option == 'Elíptica':
            Xn = mm.Coifaeliptica(Lc)         
             
        forca_normal_aleta = mm.Kfb(d,s)*mm.ForcaN_aleta(n,s,d,l,a,b)         
        ForcaNormalTotal = 2 + forca_normal_aleta     
        Xf = L - a
        Xcp =100*mm.CP(mm.cp_aleta(a,b,m,Xf),ForcaNormalTotal,forca_normal_aleta,Xn,a,b,m,Xf)   
        st.write('A localização do Cp no foguete é: ',Xcp)
             
    
    # tem-se a necessidade de criar um grafico do movimento do centro de pressao do foguetao 
    
    
    
             
             
             
