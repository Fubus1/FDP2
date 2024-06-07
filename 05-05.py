#num=int(input("Ingrese un numero "))

#with open("archivotabla.txt", "w") as archivo:
    #for i in range (1,11):
        #archivo.write(f"{num} x {i} = {num+i} \n") \n= salto de linea

def suma (num1,num2):
    with open (f"suma{num1}mas{num2}.txt", "w") as archivo:
        archivo.write(f"la suma es {num1+num2}")

suma (6,1)
