import csv
estacionamiento = [
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], [], []],
]

def compra(piso,lugar,patente):
    if piso == 0 or 1:
        print("este estacionamiento tiene un valor de 4500 por dia ")
        if not estacionamiento[piso][lugar]:
            estacionamiento[piso][lugar]=patente
    else :
        print("este lugar de estacionamiento tiene un valor de 2500 por dia ")
        if not estacionamiento[piso][lugar]:
            estacionamiento[piso][lugar]=patente
   
def saber(estacionamiento):
    for i, piso in enumerate(estacionamiento):
        for j, lugar in enumerate(piso):
            estado = "ocupado" if lugar else "no ocupado"
            print(f"El lugar {j+1} del piso {i+1} se encuentra {estado}")

def anular (piso,lugar):
    estacionamiento[piso][lugar]=[] 
    print("el lugar a sido desocupado ") 
                
def total():
    total = 0
    autos=0
    for i, piso in enumerate(estacionamiento):
        for j, lugar in enumerate(piso):
            if lugar:
                if i in [0, 1]:
                    total += 4500
                    autos +=1
                else:
                    total += 2500
                    autos +=1
    print(f"El total a cobrar por todos los autos estacionados es {total} y el numero de autos estacionados es de {autos}")

def exportar_a_csv(estacionamiento, filename="estacionamiento.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Piso", "Lugar", "Patente"])
        for i, piso in enumerate(estacionamiento):
            for j, lugar in enumerate(piso):
                patente = lugar if lugar else "Vacío"
                writer.writerow([i + 1, j + 1, patente])
    print(f"La información ha sido exportada a {filename}.")

while True :
    print("//bienvenido//")
    print("""
que desea hacer?
          
1. saber diponibilidad
2. comprar
3. anular
4. total
5. exportar
6.salir
          """)
    op=int(input("ingrese una opcion"))
    match op:
        case (1):
            saber(estacionamiento)
        case(2):
            piso=int(input("ingrese a que piso quere ir  ")) -1
            lugar=int(input("ingrese a que lugar quere ir ")) -1 
            patente=int(input("ingrese su patente "))
            compra(piso,lugar,patente )
        case(3):
            piso=int(input("ingrese en que piso se estaciono ")) -1
            lugar=int(input("ingrese en que lugar se estaciono ")) -1 
            anular(piso,lugar)
        case(4):
            total()
        case(5):
            exportar_a_csv(estacionamiento)
        case(6):
            print("a salido de el menu ")
            break
