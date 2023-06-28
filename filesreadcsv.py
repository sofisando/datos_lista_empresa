#funciones
def ventas_totales():
    cont = 0
    lista = []
    datos=open('datos.csv','r')
    _=datos.readline()
    for linea in datos.readlines():
        datos_separados = linea.split(";")  #Esto es la linea de información
        total = int(datos_separados[1]) + int(datos_separados[2]) + int(datos_separados[3])+ int(datos_separados[4])
        cont += total
    # print('Las ventas totales de la empresa son: ', cont)
    return cont
    datos.close()

def ventasXtrimestre(trimestre):
    acum = 0
    lista = []
    datos=open('datos.csv','r')
    _=datos.readline()
    for linea in datos.readlines():
        datos_separados = linea.split(";")  #Esto es la linea de información
        acum += int(datos_separados[trimestre])
    return acum
    datos.close()

def promedio_año(año):
    encontrado= False
    lista = []
    datos=open('datos.csv','r')
    _=datos.readline()
    for linea in datos.readlines():         #Lee el otro archivo, toma los datos por separado y los mete en una lista.
        datos_separados = linea.split(";") #Esto es la linea de información
        if int(datos_separados[0]) == año:
            print('¡Encontrado!')
            encontrado = True
            total = int(datos_separados[1]) + int(datos_separados[2]) + int(datos_separados[3])+ int(datos_separados[4])
            promedio =(total/3)
            print('El promedio del año ', año, ' es: ', round(promedio,2))
    if encontrado == False:
        print('El año ingresado no fue encontrado')
    datos.close()

while True:
    print('Elija una opción del siguiente menú\n1 - ventas totales de la empresa\n2 - ventas totales por trimestre\n3 - promedio de ventas totales por año\n4 - salir')

    opcion = int(input())
    if opcion == 1:
        #ventas totales de la empresa
        print('Las ventas totales de la empresa son: ', ventas_totales())
                
    elif opcion == 2:
        #ventas totales por trimestre
        t= True
        while t==True:
            trimestre = int(input('¿De qué trimestre desea conocer el total?: '))
            if trimestre<1 and trimestre>4:
                print('Trimestre no válido. Los trimestres posibles son 1,2,3 y 4. Intente de nuevo.')
            else:
                print('Las ventas totales del trimestre', trimestre, 'son :', ventasXtrimestre(trimestre))
            t = False

    elif opcion == 3:
        #Promedio de ventas totales por año
        while True:
            año = int(input('¿Que año esta buscando?: '))
            promedio_año(año)
            salir= input('¿Desea salir? si/no: ')
            if salir.lower() == 'si':
                break
        
    elif opcion == 4:
        print('¡Espero tengas buen día, adios!')
        break
    else:
        print('Por favor ingrese una opción del menú')

    print ('------------------------------------------------')
