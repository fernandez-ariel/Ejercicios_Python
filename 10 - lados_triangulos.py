"""Escribe un programa que solicite tres lados de un triangulo e indique si es
equilatero, isoles o escaleno."""

# Solicitar al usuario que ingrese los tres lados del triangulo.

lado_a = int(input("Ingrese el largo en cm del perimer lado del triangulo: "))

lado_b = int(input("Ingrese el largo en cm del segundo lado del triangulo: "))

lado_c = int(input("Ingrese el largo en cm del tercer lado del triangulo: "))

# Comprobar de acuerdo a los lados ingresados si el triangulo es equilatero, isoseles o escaleno. 

if lado_a == lado_b == lado_c: 
    print("De acuerdo a los lados ingresados el triangulo es EQUILATERO")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("De acuerdo a los lados ingresados el triangulo es ISOSELES")
else:
    print("De acuerdo a los lados ingresados el triangulo es ESCALENO")

