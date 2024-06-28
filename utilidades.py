listado_alumnos={}
def agregar_alumno():
    nombre        = input("Ingrese el nombre del alumno: ")
    apellido      = input("Ingrese el apellido del alimno: ")
    edad          = input("Ingrese la edad del alumno: ")
    nivel         = input("Ingrese el nivel del alumno: ")
    notas         = input("Ingrese las notas del alumno(separados por una coma): ").split(",")

    listado_alumnos[nombre] ={
        "nombre"     :nombre,
        "apellido"   :apellido,
        "edad"       :edad,
        "nivel"      :nivel,
        "notas"      :notas
    }
    print("El alumno fue agregado correctamente ")

def listar_alumnos():
    if listado_alumnos:
        print("       los alumnos son los siguientes: ")
        for nivel , i in listado_alumnos.items():
            print(f"nombre         :{i["nivel"]}")
            print(f"apellido       :{i["apellido"]}")
            print(f"edad           :{i["edad"]}")
            print(f"nivel          :{nivel}")
            print(f"notas          :{",".join(i["notas"])}")
            print("***************************************")
    else:
        print("UPS! no hay alumnos registrados. ")

def buscar_alumno():
    nivel=input("ingrese nivel del alumno:")
    if nivel in listado_alumnos:
        nivel= listado_alumnos[nivel]
        print("alumnos encontrados en el nivel:")
        print(f"nombre           :{nivel["nombre"]}")
        print(f"apellido         :{nivel["apellido"]}")
        print(f"edad             :{nivel["edad"]}")
        print(f"nivel            :{nivel["nivel"]}")
        print(f"notas            :{nivel["notas"]}")
    else:
        print("No hay alumnos en este nivel ")
def salir_guardar():
    if listado_alumnos:
        with open("listado.txt", "w") as archivo:
            for nivel, i in listado_alumnos.items():
                archivo.write(f"nombre           :{nivel["nombre"]}")
                archivo.write(f"apellido         :{nivel["apellido"]}")
                archivo.write(f"edad             :{nivel["edad"]}")
                archivo.write(f"nivel            :{nivel["nivel"]}")
                archivo.write(f"notas            :{nivel["notas"]}")
    else:
        print("no se a agregado nada aun")
        

def calcular_promedio():
    print("falta eso")
                

    
    



def mostrar_menu():
    print("********MENU USUARIO********")
    print("")
    print("1. Registrar alumno")
    print("2. Listar todos los alumnos")
    print("3. Buscar alumnos por nivel")
    print("4. Calcular la nota promedio de los alumnos")
    print("5. Salir del programa y guardar")

    while True:
        try:
            print("")
            opcion =int(input("seleccione una opcion: "))
            if opcion >=1 and opcion <=5:
                return opcion
            else:
                print("opcion invalida. vuelva a intentarlo.")
        except ValueError:
            print("Error. ingrese opcion valida")

