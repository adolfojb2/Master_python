"""
En matemáticas, la sucesión de Fibonacci (a veces mal llamada serie de Fibonacci)
es la sucesión infinita de números naturales.
    0,1,1,2,3,5,8,13,21,34,55,89,144,233,377...
La sucesión comienza con los números 0 y 1, y a partir de estos, cada elemento 
es la suma de los dos anteriores.
f(x) = f(x-1) + f(x-2)    
Aplicar recursividad.
https://www.youtube.com/watch?v=j9Mr70mbfOU&t=608s
"""

def fibo(num: int) ->int:
    if num == 1 or num == 0:
        return 1 
    elif num < 0:
        raise Exception("Se rompió.")    
    return fibo(num - 1) + fibo(num - 2)

numero = 3
respuesta = fibo(numero)    
print(f"fibo({numero}) = {respuesta}")