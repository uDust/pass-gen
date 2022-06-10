#   librerias   #
import random
import string 

#   variables   #

#las opciones que el usuario pondra atravez de inputs
num = int(input('que tantas contrasenas quieres que se generen?: '))
long = int(input("que tan larga quieres tu contrasena?: "))

#valores que estaremos usando para generar las contrasenas
lowerstr = list(string.ascii_lowercase)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
upperstr = list(string.ascii_uppercase)


#   condiciones para las variables      #

#si el usuario quiere generar mas de 100 contrasenas dara error
if num > 100:
    print('no puedes generar mas de 100 contrasenas, vuelve a ejecutar el programa')
    sys.exit(0)

#si el usuario quiere una contrasena de mas de 64 caracteres el programa dara error 
if long > 64:
    print('no necesitas una contrasena tan larga')
    sys.exit(0)

#   funciones   #

#funcion para generar las contrasenas y devolverlas
def gen_passwd():
    #variable para la contrasena final 
    result = ''

    #bucle para ir uniendo las variables de forma aleatoria hasta completar la concion que el usuario propuso
    for x in range(long):
        #variables las cuales de forma aleatoria se iran uniendo a la variable result 
        rnum = str(random.choice(numbers))
        rlow = random.choice(lowerstr)
        rupp = random.choice(upperstr)
        
        #elegir de manera aleatoria una variable de las que estan arriba
        options = [rnum, rlow, rupp]
        option = random.choice(options)

        #unir con el caracter aleatorio
        result += option

    #devolver el resultado
    return result

#   lo que se ejecutara     #
if __name__ == "__main__":
    #bucle para ir printeando las contrasenas
    for _ in range(num):
        print(f"\ncontrasena generada: {gen_passwd()}")




    








    
