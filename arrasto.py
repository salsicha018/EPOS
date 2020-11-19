import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import meu_modulo as mm 


def app ():
    st.title('Nessa seçao você podera calcular o Arrasto no foguete')
    st.write('A principio quando um corpo se move com uma velocidade v em um meio onde ha algum tipo de fluido, surge a força de arrasto que nada mais é que uma resistencia que o meio tem com o movimento do corpo. No nosso caso, esse fluido é o ar. Temos que levar em conta o arrasto no nosso projeto, pois ele esta diretamente ligado ao rendimento do nosso foguete')
    st.subheader('Considerações iniciais')
    st.write('Os calculos feitos nessa seção levam em consideração alguns fatores')
    st.write('O calculo do arrasto nessa fase do projeto, NÃO leva em consideração a influencia do vento sobre o foguete')
    st.write('Portanto, como não há "vento" agora o angulo de ataque é dado como 0')
    st.write('O calculo do Arrasto aqui é feito levando em conta a velocidade imediatamente antes do ar se tornar compressivel')
    st.write('No futuro esses fatores serão corrigidos')
    
    #beleza, aqui começam os calculos. todas as funções referentes a esse modulo estão definidas no arquivo meu modulo 
    
# para tornar as coisas mais simples, uma coisa que pode ser feita é importar as variaveis que são declaradas no arquivo "centrodepressao.py"
    
    st.write('Inicialmente para a velocidade do foguete, vamos colocar como um valor de input. Pois a velocidade depende da energia que o motor é capaz de gerar. E como não temos dados agora sobre a energia do motor vamos por esse caminho.')
    st.write('Por favor atente-se a colocar um valor de Velocidade coerente que não exceda o Limite do regime incompressível') 
    
    Vel = st.number_input('Insira a velocidade do foguete onde você quer calcular o arrasto')
    st.write(f'Vel = {Vel}')
             
    #a seguir vou colocar todos os valores de input do centro de pressão pois eles serão necessários para calcular o tal do arrasto 
    #  uma solução possivel a não ter que preencher novamente os campos é fazer com que os valores colocados la sejam importados para essa aba 
    #A primeira mão depois de finalizar essa parte do trabalho isso é o que será feito 
    st.subheader('Comprimento e Diâmetro do Foguete')
    #comprimento total do foguete
    Lc = st.number_input('Insira o comprimento da coifa')
    st.write('O comprimento da Coifa é: ', Lc)
    L = st.number_input('Insira o comprimento total do foguete: ')
    st.write('O comprimento total do foguete é: ', L)
    #diametro do foguete    
    d = st.number_input('insira o diametro do seu foguete: ')
    st.write('O diametro do foguete é: ', d)
    #parametros da aleta
    st.subheader('Parametros da Aleta')

    
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
        
    p = 1.2754 #numero que define a densidade do ar
    
    #vou colocar as funções que são estão no arquivo meu_modulo pq acho que tem um problema envolvendo
    # o caso onde eu chamo uma função que tem outra dunção definida dentro dela 
    
    def Re(p,u,L,Vel):#numero de reynolds
    #p e a densidade do fluido
    #u é a viscosidade do fluido
        return  ((p*Vel*L)/u)
     


    def Cffb(Rey): #coeficiente de fricção 
        Rec = 500000 #onde Rec e o numero critico de reynolds
    
        if Rec>=Rey:
            Cf = 1.328/(Rey**(1/2))
        else:
            B = Rec*((0.074/(Rey**1/5))-(1.328/(Rey**(1/2))))
            Cf = (0.074/(Rey**(1/5))) - (B/Rey)    
        return (Cf)

    def Cdfb (d,Lc,L):
        return ((((1+(60/(L/d)**3))+((25e-4)*((L - Lc)/d)))*((2.7*(Lc/d))+4*((L - Lc)/d)))*Cffb(Rey))
     

    def Cdb(Cdfb):#coeficiente de arrasto da base 
        Cdbase = 29e-3*(1/(Cdfb(d,Lc,L))**(1/2))
        return (Cdbase)

    def Cdf (Tf,n,d):
        Cff = Cffb(Rey)
        CDF = 2*Cff*(1+2*(Tf/l))*(4*n*Areatotalexpostadaaleta(a,d,b,s))/(3.14*(d**2))
        return CDF

    def Cdi (Tf,n,a,l,d):           
        CDI = 2*Cffb(Rey)*(1+2*(Tf/l))*4*n*(0.5*d*a)
        return (CDI)


    def Cdo():
        CDO = Cdfb(d,Lc,L)+Cdb(Cdfb)+Cdf(Tf,n,d)+Cdi(Tf,n,a,l,d)
        return (CDO)
    def A(d):
        Area = (3.14/4)*d**2
        return (Area)
    def arrasto (p):
        D = 0.5*p*(Vel**2)*Cdo()*A(d)
        return (D)
    #Calcular o coeficiente de arrasto para cada componente do foguete
    #Cdfb é coeficiente de arrasto no corpo do foguete que eu acho que inclui a coifa e o corpo do foguete 
    
    #escrevendo o coeficiente de fricção do Cdfb:
    
                 
                 #Arrasto na base do foguete:


#arrasto nas aletas do foguete:

#é a area total da aleta 
           
    def Areatotalexpostadaaleta(a,d,b,s):
        Afp = 0.5*(a+b)*s + 0.5*d*a
        return (Afp)
    def A(d):
        Raio = d/2
        A = 3,14*Raio**2    
        return (A)             
    
    
    
    
    
    
    
    
    #O calculo do arrasto 
    
    TudoCerto4 = st.checkbox('Calcular o Arrasto')
    if TudoCerto4:
        '''  vou deixar todas a variaveis já declaradas a fim de poupar tempo na hora de debugar o código'''
        
        A = A(d)#area da base da coifa
        p = 1.25#kg/m^3, densidade do ar 
        u = 17.2e-6 #viscosidade do ar
        Rey = Re(p,u,Vel,L)#numero de Reynolds 
        CD = Cdo()
        Afp = Areatotalexpostadaaleta(a,d,b,s)
        
        
        
        #aqui eu estou apenas printando as variaveis
        st.write(f'Numero de Reynolds {Re(p,u,Vel,L)}')
        st.write(f'Cffb = {Cffb(Rey)}')
        st.write(f'Cdfb = {Cdfb (d,Lc,L)}')
        st.write(f'Cdb = {Cdb(Cdfb)}')
        st.write(f'Cdf = {Cdf (Tf,n,d)}')
        st.write(f'Cdi = {Cdi (Tf,n,a,l,d)}')
        st.write(f'Cdo = {Cdo()}')
        CDDDDDO =Cdo()
        arrastou = 0.5*(Vel**2)*(3.14/4)*(d**2)*CDDDDDO
        st.write(f'Arrasto = {arrastou} N')
    
    
    
        
        #plotando um grafico para o arrasto do foguete até atingir a velocidade do som 
        
        while Vel < 333:#velocidade em metros por segundo
        ForcadeArrasto.append(arrastou(Vel))
        Velocidade.append(Vel)
        Vel +=5
        from bokeh.plotting import figure
        a = figure(
        title='Variação da força de arrasto de acordo com a velocidade',
        x_axis_label='Velocidade',
        y_axis_label='Arrasto')
        a.line(Velocidade,ForcadeArrasto, legend_label = 'Tendencia', line_width=2)
        st.bokeh_chart(a, use_container_width=True)

#arquivo de saida 
#colocar um codigo para realizar um esquema de arquivo de saida




    
