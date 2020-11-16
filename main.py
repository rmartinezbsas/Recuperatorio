import csv
import os.path

def cargar(archivo, campos):
    formato='w'
     

    guardar = "si"
    lista_empleados = []
    while guardar == "si":
        empleado = []
        print()
            
        for campo in campos:
             empleado.append(input(f"Ingrese {campo} del empleado: "))
        bandera=False    
        while bandera==False:           
             try:
                   int(empleado[0])
                   bandera=True
             except ValueError:
                  print()
                  print("Necesita ingresar un numero entero en el Legajo")
                  empleado[0]=input("Ingrese numero de legajo correcto: "
                  )
        
         
        lista_empleados.append(empleado)
        guardar = input("Desea seguir cargando empleados? Si/No: ")
        print()

    try:
        formato='w'
        archivo_usuario=(input("Ingrese el nombre del archivo: "))  
        if os.path.exists(archivo_usuario):
             archivo=archivo_usuario
             formato=(input("Desea agregar o sobreescribir? \n Agregar - a \n Sobreescribir- w    "))
             
          
        else:
            print("El archivo no existe, se creara uno nuevo")
            archivo=archivo_usuario


        with open(archivo, formato, newline='') as file:
            file_guarda = csv.writer(file)
            #file_guarda.writerow(campos)
            file_guarda.writerows(lista_empleados)
            print("se guardo correctamente")
            print()
            return
    except IOError:
        print("Ocurrio un error con el archivo")



def menu():

    ARCHIVO = "empleados.csv"
    ARCHIVO2 ="Viaticos.csv"
    CAMPOS = ['Legajo', 'Apellido', 'Nombre']

    while True:
        print("Elija una opcion: \n 1.Cargar datos \n 2.Informe de viaticos \n 3.Salir")
        opcion = input("")
                 
        if opcion == "1":
           cargar(ARCHIVO, CAMPOS)
        if opcion == "2":
           informar(ARCHIVO,ARCHIVO2)
           pass
        if opcion == "3":
            exit()
        else:
            print("Por favor elija una opcion valida")

menu()