

nombre = input("¿Como te llamas? ")
print("hola " + nombre)

edad = int(input("¿Cuantos años tienes? "))
print(type(edad))
if( edad < 18):
    print("Usted es menor de edad ")
else:
      print("Usted es mayor de edad ")

genero = input("¿Cual es tu genero? (Masculino/Femenino) ")

altura = float(input("¿Cual es su estatura en metros? "))
est = altura

peso = float(input("¿Cual es tu peso en kilogramos? "))
p = peso

# Calculo del IMC: peso (En kilogramos) / estatura (En metros) **2
IMC = p / est**2

print("IMC: " + str(IMC) )

# Hacemos validaciones

if IMC >= 0 and IMC <= 15.99 :
        print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Delgadez moderada ")
elif IMC >= 17.00 and IMC <= 18.49:
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Delgadez leve ")
elif IMC >= 18.50 and IMC <= 24.99 :
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Normal ")
elif IMC >= 25.00 and IMC <= 29.99:
        print (str(nombre) + " a la edad de "+ str(edad) + " años " +str(genero) + " Tu IMC indica Sobrepeso ")
elif IMC >= 30.00 and IMC <= 34.99:
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Obesidad leve ")
elif IMC >= 35.00 and IMC <= 39.00:
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Obesidad media ")
elif IMC >= 40.00:
        print (str(nombre) + " a la edad de "+ str(edad) + " años " + str(genero) + " Tu IMC indica Obesidad morbida ")
 