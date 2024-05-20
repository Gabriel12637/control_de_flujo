#este codigo imprime los numeros
#edad 1 al 10
 for n in range(1,11):
     print(n)


# crear un programa que imprima las 5 vocales

vocales:str"aeiou"
for n in range(0,5)
      print(vocales[n])

# crear un programa que me muestre los 8 primeros numeros pares 



for n in range(1,17):
     if n%2==0:
       contador+=1
       print (f"[n] es par numero[contador]")





# crear unprograma que pida al usuario escribir una oracion 
# y mostrar por terminal la cantidad de vocales  que 
# tiene esa oracion
# ojo solo las "a" minuscula


oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if n=="a":
        contador=contador+1
        #contador+=1


for n in "aeiou":
    print(n)


for ind_vocal,let_vocal in enumerate("aeiou"):
    print(f"el indice es(i) y la letra es (i)")

print(f"la cantidad de letras a que es (contador) ")



# crear un programa que me cuente la cantidad de comas y me muestre
# sus indices.
# ojo: tiene que pedir al usuario


texto:str=input(" ingresa un texo:")
cantidad de comas = 0
indice_comas=[]
for indice,caracter in enumerate(texto)
 if caracter ==",":
    cantidad_commas+=1
    indice_comas.append(indice)

print("cantidad de comas:",cantidad_comas)
print("indice de las comas:",indice_comas)

# escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
# que ha cumplido (1 hasta su edad)

edad=int(input("ingresa tu edad: "))
for i in range(1 , edad+1):
    print("ha cumplido",i,"años")

# crea un programa que me pida el nombre de tres personas y guarde
# variable global la ultima letra de sus nombres
# mostrar por pantalla la variable global con los tres ultimos letras del nombre de cada persona
  
for n in range(3):
    nombre:str=input("escribe tu nombre: ")
   #ultima_letra+=nombre[-1]
   last_letter:str=init=nombre[-1]
ultima_letra+=last_letter
#ultima_letra-ultima_letra+last_latter
print(ultima_letra)






vocales = ['A','E','I','O','U']
for i in range(len(vocales)):
        linea = ''
    for i in range(i+1):
     linea+=
     vocales[1]. lower()
     print(linea.capitalize())


CONTADOR=0
white contador<=5:
print(contador)
contador+=1
print(f"valor final(contador)")
 
nombre="jose"
nombre.upper() #convierte al texto en mayusculas

apellidos="alvarez"
print(apellido.lower() # convierte el texto a minusculas
segundo_nombre="luis"
print(segundo_nombre.capitalize()) # convierte la primera letra mayuscula 

# crear un programa que piada la cantidad de notas que se debe registrar
# luego pedira las notas e imprimira el promedio 


num_notas = int(input("Ingrese la cantidad de notas a registrar: "))
suma_notas = 0

for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / num_notas

print("\nEl promedio de las notas ingresadas es: ", promedio)



