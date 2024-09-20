#Programa que lee los numeros de una matriz nxn y suma solo los numeros pares

def matriz():
    # Input: una matriz bidimensional nxn
    # Output: Suma de todos los números pares
    a = [
        [4, 2, 8],
        [1, 6, 2],
        [7, 3, 9]
    ]

    sumtotal = 0
    k = 0
    
    for i in range(len(a)):
      for j in range(len(a[i])):
          k = a[i][j]
          if k % 2 == 0:  
                sumtotal += k  

    return sumtotal
   
resultado = matriz()
print (f"Suma de numeros pares = {resultado}")
