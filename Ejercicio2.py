
name = input("Hola, Por favor ingresa tu nombre: " )

var1 = int(input(f"Hola {name} Ingresa un numero: "))
var2 = int(input(f"Hola {name} ingresa otro numero:"))

print(f"Hola {name} los numeros que ingresaste son iguales:", var1==var2)
print(f"Hola {name} los numeros que ingresaste son diferentes:", var1!=var2)
print(f"Hola {name} el numero {var1} es mayor a {var2}:", var1>var2)
print(f"Hola {name} el numero {var1} es menor a {var2}:", var1<var2)
print(f"Hola {name} el numero {var1} es mayor o igual a {var2}:", var1>=var2)
print(f"Hola {name} el numero {var1} es menor o igual a {var2}:", var1<=var2)