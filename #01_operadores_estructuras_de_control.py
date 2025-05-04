''' * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.'''

a = 10
b = 3
print(f"Variable {a} \nVariable {b}")
# --------------------
# Operadores aritméticos
# --------------------

print("\nOperadores Aritméticos:")
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)
print()

# --------------------
# Operadores lógicos
# --------------------
x = True
y = False

print("Operadores Lógicos:")
print(f"X ={x}")
print(f"Y ={y}")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
print()

# --------------------
# Operadores de asignación
# --------------------
# --------------------
# Operadores de comparación
# --------------------
print("Operadores de Comparación:")
print("¿a == b?", a == b)
print("¿a != b?", a != b)
print("¿a > b?", a > b)
print("¿a < b?", a < b)
print("¿a >= b?", a >= b)
print("¿a <= b?", a <= b)
print()

print("Operadores de Asignación:")
c = 5
print("Valor inicial:", c)
c += 2
print("c += 2:", c)
c -= 1
print("c -= 1:", c)
c *= 3
print("c *= 3:", c)
c /= 2
print("c /= 2:", c)
c %= 4
print("c %= 4:", c)
c **= 2
print("c **= 2:", c)
c //= 3
print("c //= 3:", c)
print()


# --------------------
# Operadores de identidad
# --------------------
print("Operadores de Identidad:")
d = [1, 2, 3]
e = d
f = [1, 2, 3]

print("e is d:", e is d)
print("f is d:", f is d)
print("f is not d:", f is not d)
print()

# --------------------
# Operadores de pertenencia
# --------------------
print("Operadores de Pertenencia:")
print("2 in d:", 2 in d)
print("5 not in d:", 5 not in d)
print()

# --------------------
# Operadores a nivel de bits
# --------------------
print("Operadores de Bits:")
x = 6  # 110
y = 3  # 011
print("x & y:", x & y)   # 010
print("x | y:", x | y)   # 111
print("x ^ y:", x ^ y)   # 101
print("~x:", ~x)         # complemento
print("x << 1:", x << 1) # desplazamiento izquierda
print("x >> 1:", x >> 1) # desplazamiento derecha
print()

# --------------------
# Estructuras de control: condicionales
# --------------------
print("Condicionales:")
edad = 20
if edad >= 18:
    print("Es mayor de edad.")
elif edad > 13:
    print("Es adolescente.")
else:
    print("Es niño.")
print()

# --------------------
# Estructuras de control: iterativas
# --------------------
print("Iteración con for:")
for i in range(3):
    print("Iteración", i)

print("\nIteración con while:")
n = 0
while n < 3:
    print("n =", n)
    n += 1
print()

# --------------------
# Estructuras de control: manejo de excepciones
# --------------------
print("Manejo de Excepciones:")
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Bloque finally ejecutado.")
print()

# --------------------
# DIFICULTAD EXTRA
# --------------------

print("Ejercicio extra planteado")
for i in range (10,56):
        if i % 2 == 0 and i != 16 and i % 3 != 0: 
            print(i)