#importacao das bibliotecas necessarias

import streamlit as st


#comeco do codigo
def app():
    
    st.title('EPOS')
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



    st.subheader('O que há para o futuro?')
    st.write('Um passo para trás, dois pra frente: todo esse trabalho que esta sendo desenvolvido agora, pode não ser tão animador agora. Ainda temos muitos desafios a serem superados, mas isso é natural. Para mim, seria impossivel fazer tudo que esse projeto se propõe a fazer sozinho. Somos uma equipe, e o resultado que obteremos em competições futuras depende só de nós. Temos que trabalhar juntos. Tudo o que fazemos hoje, tem reflexo no amanhã, é inutil nesse caso pensar que estamos perdendo tempo de nossas vidas fazendo parte desse time, se estamos aqui é por que em algum momento nós desejamos isso individualmente. Como disse antes, tudo que fazemos hoje tem reflexo no amanhã. Hoje eu escrevo uma linha, amanhã eu obtenho um Resultado. Não adianta querer as coisas prontas de uma vez só, temos que ser pacientes! O amanhã logo virá, precisamos estar prontos pro que vier. Se a esmola é muita, o santo desconfia. Tudo que vem facil, vai facil. Todas essas coisas, agora parando para pensar enquanto escrevo isso, trazem a tona uma verdade, nada grandioso é construido com facilidade. Leva tempo, suor, bunda na cadeira e muitas outras coisas. para mim o sentido da vida é: ser melhor a cada dia e deixar nossa marca no mundo. Novamente, nada do que fizemos e faremos é atoa, se você acha que sim, talvez seja hora de parar um pouco e refletir, o que te trouxe até aqui?')
    st.write('espero que essa aplicação seja muito util para nós como um todo')
    st.write('Desenvolvedor responsável: Paulo Vinicius Pimentel da Silva Camargo; Telefone: (12)996776894; e-mail: paulo.vine@usp.br')


