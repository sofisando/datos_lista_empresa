while True:
    print('Elija una opción del siguiente menú\n1 - ventas totales de la empresa\n2 - ventas totales por trimestre\n3 - promedio de ventas totales por año\n4 - salir')

    opcion = int(input())
    if opcion == 1:
        #ventas totales de la empresa
        cont = 0
        lista = []
        datos=open('datos.csv','r')
        _=datos.readline()
        for linea in datos.readlines():
            datos_separados = linea.split(";")  #Esto es la linea de información
            total = int(datos_separados[1]) + int(datos_separados[2]) + int(datos_separados[3])+ int(datos_separados[4])
            cont += total
        print('Las ventas totales de la empresa son: ', cont)
        datos.close()
                
    elif opcion == 2:
        #ventas totales por trimestre
        t= True
        while t==True:
            acum = 0
            trimestre = int(input('¿De qué trimestre desea conocer el total?: '))
            if trimestre<1 and trimestre>4:
                print('Trimestre no válido. Los trimestres posibles son 1,2,3 y 4. Intente de nuevo.')
            else:
                lista = []
                datos=open('datos.csv','r')
                _=datos.readline()
                for linea in datos.readlines():
                    datos_separados = linea.split(";")  #Esto es la linea de información
                    acum += int(datos_separados[trimestre])
                print('Las ventas totales del trimestre', trimestre, 'son :', acum)
                datos.close()
            t = False

    elif opcion == 3:
        #Promedio de ventas totales por año  TIENE UN ERROR, SI NO ENCUENTRA EL PRIMERO NO ENCUENTRA LOS DEMAS
        while True:
            encontrado = False
            año = int(input('¿Que año esta buscando?: '))
            lista = []
            datos=open('datos.csv','r')
            _=datos.readline()
            for linea in datos.readlines():         #Lee el otro archivo, toma los datos por separado y los mete en una lista.
                datos_separados = linea.split(";") #Esto es la linea de información
                if int(datos_separados[0]) == año:
                    total = int(datos_separados[1]) + int(datos_separados[2]) + int(datos_separados[3])+ int(datos_separados[4])
                    promedio =(total/3)
                    print('El promedio del año ', año, ' es: ', round(promedio,2))
                    encontrado = True
            datos.close()
            if encontrado == False:
                print('El año ingresado no fue encontrado')
            else:
                break
        
    elif opcion == 4:
        print('¡Espero tengas buen día, adios!')
        break
    else:
        print('Por favor ingrese una opción del menú')

    print ('------------------------------------------------')
