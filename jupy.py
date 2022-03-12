def mcd(x,y):
    t = 0
    while (y > 0):
        t = y
        y = x % y
        x = t
    return x

def simplificacion(x,y):
    if y==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    num=int(x/mcd(x,y))
    den=int(y/mcd(x,y))
    if den==1:
        return(num)
    return str(num)+'/'+str(den)

def suma(num1,den1,num2,den2):
    if den1==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    elif den2==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    numerador=int(num1*den2)+int(num2*den1)
    denominador=int(den1*den2)
    if denominador==1:
        return(numerador)
    return str(numerador)+'/'+str(denominador)

def resta(num1,den1,num2,den2):
    if den1==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    elif den2==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    numerador=int(num1*den2)-int(num2*den1)
    denominador=int(den1*den2)
    if denominador==1:
        return(numerador)
    return str(numerador)+'/'+str(denominador)

def multiplicacion(num1,den1,num2,den2):
    if den1==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    elif den2==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    numerador=int(num1*num2)
    denominador=int(den1*den2)
    if denominador==1:
        return(numerador)
    return str(numerador)+'/'+str(denominador)

def division(num1,den1,num2,den2):
    if den1==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    elif den2==0:
        return('EL DENOMINADOR NO PUEDE SER 0')
    numerador=int(num1*den2)
    denominador=int(num2*den1)
    if denominador==1:
        return(numerador)
    return str(numerador)+'/'+str(denominador)
