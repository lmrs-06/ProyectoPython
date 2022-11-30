
#Sistema importado para la fecha y hora
import random
import os
import time
os.system("clear") #comando que llama al sistema y ejecuta el comando clear
#Prueba de usuario
print("Hecho por Luis MIguel Rodriguez Suarez")
print( )
#Variables
fecha = time.strftime("%x") #variable de fecha
hora = time.strftime("%X") #variable de hora 
newvariante=str("ccucggcgggca") #seleccionamos la cadena de la nueva variante
codigo=input("Introduzca el codigo del paciente: ") #pedimos un codigo de paciente
numero=10000000 #longitud de cadena de ADN, cuanto mas larga, mas posibilidad de distintas respuestas
letras=["c","u","g","a"] #seleccionamos los componentes de la nueva variante
nletras=len(letras) #cuenta el nº de letras de la nueva variante
aleatorio=[]
#Principal
for i in range(0, numero, 1):
    numaleatorio = random.randint(0, nletras - 1) #generamos la cadena aleatoria
    aleatorio.append(letras[numaleatorio]) #el aleatorio se añade a la cadena de adn
generado="".join(aleatorio)
#Resultado
resultado = ""
if newvariante in generado: #se comprueba si el paciente es positivo o no mediante buscar la nueva variante con el adn que hemos generado
    resultado = "Positivo: Sí se encuentra restos de la variante COVID."
    final = "Positivo"
else:
    resultado = "Negativo: No se encuentra restos de la variante COVID."
    final = "Negativo"
#Tupla con redireccion a fichero .txt
tupla=(fecha,hora,codigo,final)
genera=list(tupla)
file=open("inf-covid.txt","a")
file.write('%s' % genera +'\n')
#Informe COVID
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Informe de Virus COVID:")
print("Fecha:",fecha)
print("Hora:",hora)
print("Código del paciente:",codigo)
print("Resultado:",resultado)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
