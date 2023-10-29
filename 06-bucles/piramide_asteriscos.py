"""
base = 10
     *
    **
   ****
  ****** 
 ********
**********
"""
#Truco: Se van reduciendo los espacios de a 1 y si aumentan los asteriscos de a 2.
base = 27 #debe ser impar
contador = 1
esp = base*2 #espacios hasta el primer asterisco
while contador <= base:
    for espacios in range(0,esp):
        print(" ",end="")
    esp -= 1 
    for aste in range(1,contador+1):
        print("*",end="")
    print("\n")    
    contador +=2
       

