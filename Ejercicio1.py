
name = input("Hola, Por favor ingresa tu nombre: " )
var1 = int(input(f"Hola {name} Ingresa un numero entero "))
var2 = int(input(f"Hola {name} Ingresa otro numero entero "))
suma = var1+var2
resta = var1-var2
multiplicacion = var1*var2
division = var1/var2
division_entera = var1//var2
modulo = var1%var2
potencia = var1**var2

print(f"Hola {name} este este es el resultado de tus operaciones matematicas:")
print(f"la suma de tus numeros es:{suma}")
print(f"la resta de tus numeros es:{resta}")
print(f"la multiplicacion de tus numeros es:{multiplicacion}")
print(f"la division de tus numeros es:{division}")
print(f"la division entera de tus numeros es:{division_entera}")
print(f"el modulo de tus numeros es:{modulo}")
print(f"la potencia de tus numeros es:{potencia}")