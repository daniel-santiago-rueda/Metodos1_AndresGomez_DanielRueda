#Punto 1
def factorial(n:int):
    if n in (0,1):
        return 1

    if n > 1:
        resultado = n*factorial(n-1)

        return resultado

for i in range(0, 21):
    print ("Factorial de " + str (i) + ": " + str (factorial(i)))

#Punto 2
def variaciones(n:int, r:int):
    return factorial(n)/factorial(n-r)

#Punto 2.a
print("\nSe puede ubicar 6 carros en 3 estacionamientos de " + str (variaciones(6, 3)) + " maneras.")

#Punto 3
def combinaciones(n:int, m:int):
    return factorial(n)/(factorial(m)*factorial(n-m))

#Punto 3.a
print("\nSi cualquiera puede ser el arquero, se pueden formar " + str (combinaciones(22, 11)) + " equipos.")

#Punto 3.b
print("\nSi se sabe quien será el arquero, se pueden formar " + str (combinaciones(21, 10)) + " equipos.")
