#matriz_sencilla = [[1, 2, 3],[4, 5, 6]]
#array=            [       1,     2    ]
#print 

#for elemento in matriz_sencilla:
    #print(elemento)

matriz_sencilla = [
[1, 2, 3],
[4, 5, 6]
]
print("1)imprimir matriz")
for elemento in matriz_sencilla:
    print(elemento)
print("2)imprimir un elemento por posición")
print(matriz_sencilla[1][0])
print("3)Imprimir todos los elementos")
for fila in matriz_sencilla:
    for elemento in fila:
        print(elemento, end=' ')
print()