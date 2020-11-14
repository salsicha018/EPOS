#importar do centro de gravidade o valor que é salvo na variavel CG

#importar do centro de pressão o valor que é salvo na variavel CP 

#pegar esses dois valores e calcular a margem estatica do foguete 

#uma coisa que pde ser feita é levar em consideraçao o movimento que o cg e cp fazem quando o foguete queima combustivel, ou seja ele acelera
#e tentar construir um grafico da variação da margem estatica em uma possivel situaçao de voo



#docstring a respeito da margem estatica. 
'''
Margem estatica

Quando se pensa em projetar um Foguete, assim como é necessario saber o ponto de equilibrio dele, ou seja, onde todas as forças de peso de concentram. 
tambem é preciso saber onde as forças de pressão estã concentradas
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
