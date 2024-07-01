import os
registro = [
    ["Marca", "Año", "Kilometraje", "Costo", "Impuesto", "Total"]
]
regmarca=["TOYOTA", "FORD", "CHEVROLETT"]
#orden de registro con: marca, año, kilometraje, costo de reparación
def agregar():
    while True:
        try:
            print('''de acuerdo, ingrese los datos según se le irán pidiendo
                  
                  ''')
            marca=input(f'''Ingrese la marca del vehículo:
                    ''')
            año=str(input(f'''Ingrese el año del vehículo:
                    '''))
            km=str(input(f'''Ingrese el kilometraje del vehículo:
                    '''))
            costo=float(input(f'''Ingrese el costo de reparación del vehículo:
                    '''))
            impuesto=(float(costo*8))/100
            total=costo+impuesto
            registro.append([marca, año, km, costo, impuesto, total])
            regmarca.append(marca)
            break
        except:
            input("excepción al ingresar")
            break

#lista con: marca, año, kilometraje, costo de reparación, impuesto, costo total a pagar
def lista():
    while True:
        try:
            print (registro)
            break
        except:
            print ("error")

def buscarMarca(mar):
    try: 
        for item in range(len(regmarca)):
            if mar == regmarca:
                return item
        return -1
    except:
        input("excepcion al buscar por marca")


def orden():
    texto = '''     LISTADO GENERAL
-------------------------------------------
N°      RUT         NOMBRE          SUELDO 
-------------------------------------------
'''
    for row in range(len(registro)):
        texto += f"{row+1:3d} "  # numero desde 1 con ancho de 3
        texto += f"{registro[row][0]:12s}" # rut, col 0, ancho de 12, String
        texto += f"{registro[row][1]:20s}"    # nombre, col 1, ancho de 20s
        texto += f"{registro[row][2]:8d}"    # sueldo, col 2, ancho de 8d
        texto += '\n' # salto a la linea siguiente
    texto += "##############  FIN LISTADO   ###############" + '\n'
    texto += f"cantidad total de filas    = {len(registro)}" + '\n'
    texto += f"cantidad de total columnas = {len(registro[0])}" +'\n'

import datetime
def Imprimir():
    while True:
        try:
            os.system("cls")
            print("IMPRIMIR ORDEN")
            mar=input('''marca: ''')
            enc=buscarMarca(mar)
            if enc==-1:
                print('La marca no ha sido encontrada dentro del registro')
                break
            else:
                print ("marca encontrada dentro del registro")
                for row in range(len(registro)):
                    if mar == registro[row][0]:
                        ahora = datetime.datetime.now()
                        fecha = str(ahora.day) + '/' + str(ahora.month) + '/' + str(ahora.year)
                        hora = str(ahora.hour) + ':' + str(ahora.minute)
                        with open(f'orden_{fecha}.txt','w', encoding='utf-8') as archivo:
                            archivo.write(orden())
                            archivo.write(f"FECHA Y HORA DE REPORTE: {fecha} {hora}")
            print                
        except:
            print('''Excepción al ingresar''')

print("buen día")
while True:
    try:
        print(f'''indique qué es lo que desearía hacer de entre las opciones:
                1.- Registrar vehículo.
                2.- Mostrar lista de vehiculos registrados.
                3.- Imprimir una orden de reparación.
                4.- Salir
                ''')
        a=int(input(""))
        if a==1:
            agregar()
        elif a==2:
            lista()
        elif a==3:
            Imprimir()
        elif a==4:
            break
        else:
            print('''esa opción no es valida''')
    except:
        print ('''excepción al ingresar''')