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
            file_guarda.writerows(lista_empleados)
            print("se guardo correctamente")
            print()
            return
    except IOError:
        print("Ocurrio un error con el archivo")

def informar(archivo,archivo2):
      guardar2=False
      while guardar2==False:
            archivo_ei=(input("Con Cual Archivo de empleados desea trabajar?: "))
            if os.path.exists(archivo_ei):
              archivo=archivo_ei
              guardar2=True
            else:
              print("El archivo no existe. Quiere elegir otro?: ")
              eleccion_z=(input("si/no?: "))
              if eleccion_z=="no":
                  print("Muchas gracias. Lo guiaremos al menu principal por si quiere crear un archivo de empleados")
                  print()
                  menu()
       

      archivo_vi=(input("Con Cual Archivo de viaticos desea trabajar ?"))
      if os.path.exists(archivo_vi):
        archivo2=archivo_vi
      else:
        print("El archivo no existe. Quiere trabajar con el archivo",archivo2,":?")
        eleccion_aqn=(input("si/no:? "))
        if eleccion_aqn=="si":
          archivo2=archivo2
        else:
          print("No contamos con otro archivo. Lo siento lo redigiremos al menu principal")
          menu()


    
      

      empleado_a=open(archivo) 
      viaticos_a=open(archivo2)
      empleado_csv = csv.reader(empleado_a)
      viaticos_csv = csv.reader(viaticos_a)

      
      empleado=next(empleado_csv,None)
      viaticos=next(viaticos_csv,None)
      legajo_usuario=input("Ingrese numero de legajo buscado: ")
      print()
      bandera2=False    
      while bandera2==False:           
             try:
                   int(legajo_usuario)
                   bandera2=True
             except ValueError:
                   print()
                   print("Necesita ingresar un numero entero en el Legajo")
                   legajo_usuario=input("Ingrese numero de legajo correcto: ")
                   print()
      count=0            
      saldo_viaticos_a=0
      saldo_viaticos_t=0
      while (empleado):
              if (empleado[0]==legajo_usuario):
                  while viaticos:   
                                     
                    if(viaticos[0]==legajo_usuario):
                                                                   
                       while (viaticos[0]==legajo_usuario):
                         count=count+1
                         saldo_viaticos_a= int(viaticos[1])
                         saldo_viaticos_t= saldo_viaticos_t+saldo_viaticos_a
                         viaticos= next(viaticos_csv, None)
                       
                       if saldo_viaticos_t > 5000:
                            limite= 5000
                            diferencia= saldo_viaticos_t-limite
                            print(f"Legajo {empleado[0]} {empleado[2]} {empleado[1]} gasto",saldo_viaticos_t, "y se ha pasado del presupuesto por $",diferencia)
                            menu()
                       else:
                         print(f"Legajo {empleado[0]} {empleado[2]} {empleado[1]} gasto",saldo_viaticos_t, ":")
                       print()
                       menu()
                       
                    viaticos= next(viaticos_csv, None)
              else:
                empleado=next(empleado_csv,None)   
      print("El legajo no existe")
      print("Lo guiaremos al menu principal. Puede intentar nuvemente si desea")
      print()
                
              
      

     
      empleado_a.close()
      viaticos_a.close()

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
        if opcion == "3":
            exit()
      
        else:
            print("Por favor elija una opcion valida")

menu()