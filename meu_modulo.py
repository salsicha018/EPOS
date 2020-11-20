#este e um modulo criado para armazenar as funções da aplicação para que seja mais facil de lidar com o codigo principal


#calculo da massa total do foguete
def MassaTotal( Coifa , Corpo1, Corpo2,  Motor, Aleta1,AnelCentralizador,BulkHead):
    """
    Fatores de entrada:
    Coifa, é parte pontuda kkk \n
    Corpo1 onde fica a parte de avionica e recuperação\n
    Corpo2 onde fica a parte de propulsão\n
    Motor é um tubo interno no foguete\n 
    Aleta1 é a dimensão da aleta\n
    AnelCentralizador, é um componente internoque serve para conectar os componentes do foguete\n
    BulkHead é uma tampa que que impede o contato de partes separadas\n
    
    
    
    
    """
    Massa = Coifa +Corpo1+Corpo2+Motor+(3*Aleta1)+(2*AnelCentralizador)+(2*BulkHead)
    return Massa
#calculo do Centro de gravidade do foguete
#def CG(Coifa , Corpo1, Corpo2,  Motor, Aleta1 , Coifa_dis,Corpo1_dis,Corpo2_dis,Motor_dis,Aleta1_dis):
 #   cg = (1/MassaTotal(Coifa , Corpo1,Corpo2, Motor, Aleta1))*(Coifa*Coifa_dis+Corpo1*Corpo1_dis+Corpo2*Corpo2_dis+Motor*Motor_dis+ 3*(Aleta1*Aleta1_dis)+ )
 #   return cg


#refazendo o calculo do centro de gravidade considerando um novo tipo de input, que só leva em conta o comprimento dos componentes 
def CG(Coifa , Corpo1, Corpo2,  Motor, Aleta1 , Coifa_dis,Corpo1_dis,Corpo2_dis,Motor_dis,Aleta1_dis,AnelCentralizador,BulkHead):
    cg = (1/MassaTotal(Coifa , Corpo1,Corpo2, Motor, Aleta1,AnelCentralizador,BulkHead))*((Coifa_dis/2)*Coifa + Coifa_dis*AnelCentralizador +(Coifa_dis+(Corpo1_dis/2))*Corpo1+(Coifa_dis+Corpo1_dis)*AnelCentralizador+ (Coifa_dis+Corpo1_dis+(Corpo2_dis/2))*(Corpo2)+ (Coifa_dis+Corpo1_dis+Corpo2_dis - Aleta1_dis+(Aleta1_dis/2))*Aleta1*3 + (Coifa_dis+Corpo1_dis+Corpo2_dis- Motor_dis +(Motor_dis/2))*Motor)
    return (cg)

#função que calcula o raio do foguete:

def R(d):
    R = d/2
    return (R)


#funções que definem as coifas:

def coifaconica(Lc):
    Xn = (3*Lc)/3
    return (Xn)

def coifaogival(Lc):
    Xn = 0.534*Lc
    return(Xn)
def coifaparabolica(Lc):
    Xn = L/2
    return(Xn)
def coifaeliptica(Lc):
    Xn = (3*Lc)/2
    return (Xn)
def LV_HAACKcoifa(Lc):
    Xn = 0,437*Lc
    return (Xn)
def coifavonkarman(Lc):
    Xn = 0,500*Lc
    return (Xn)
def coifa_generica (Vol,R):
    
    A = float(R*R*3.14)
    Xn = Vol/A
    return (Xn)

def Kfb(d,s):# R é o raio da aleta, s a largura desde raiz interior até a raiz exterior, e essa função é um fator de interferência
    Kfb = 1 + ((d/2)/(s+(d/2)))
    return (Kfb)
def cp_aleta(a,b,m,L):
    Xfbarra = (L - a) + m*(a+2*b)/3*(a+b)+ (1/6)*(a+b- (a*b)/(a+b))
    return (Xfbarra)

def ForcaN_aleta(n,s,d,l,a):
    
    #n é o numero de aletas
    #s é a distancia da raiz da aleta até a lateral mais externa
    #l e o comprimento da linha que corta a aleta no meio
    #b é a altura da lateral mais externa da aleta
    #a é o comprimento da raiz que fica colada no corpo do foguete
    #d é o diametro d =o corpo do foguete, ou então a distancia entre as aletas.
    return ((4*n*(s/d)**2)/(1 + (1 + (2*l/(a+b))**2)**(1/2)))
    
                                                          
#calculando a força normal total na aleta

                                                          
#função que define o centro de pressão do foguete:
def CP(func,ForcaNormalTotal,forca_normal_aleta,Xn,a,b,m,Xf):
    CP = (((2*Xn) + ( forca_normal_aleta *func ) )/(ForcaNormalTotal))
    return (CP)
#função que define a margem estatica do foguete
def Margemestatica(CG,CP,d):
    '''
    A margem estatica é definida em termos de calibre, onde um cal corresponde ao diametro do foguete
    O valor ideal para esta na faixa é de 1,0 a 2,0 calibres
    '''
    Margemestatica = (CP - CG)/d
    return (Margemestatica)
#aqui começam as funções do calculo do arrasto do foguete


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
    Cff = Cffb()
    CDF = 2*Cff*(1+2*(Tf/l))*(4*n*Areatotalexpostadaaleta(a,d,b,s))/(3.14*(d**2))
    return CDF

def Cdi (Tf,n,a,l,d):           
    CDI = 2*Cffb()*(1+2*(Tf/l))*4*n*(0.5*d*a)
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
                 
#arrasto de interferencia nas aletas:
                 

                 
