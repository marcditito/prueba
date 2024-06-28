from utilidades import mostrar_menu, agregar_alumno, listar_alumnos, buscar_alumno,salir_guardar, calcular_promedio

while True:
    opcion = mostrar_menu()

    if opcion==1:
        agregar_alumno()
    elif opcion == 2:
        listar_alumnos()
    elif opcion == 3:
        buscar_alumno()
    elif opcion ==4:
        calcular_promedio
    elif opcion ==5:
        salir_guardar()
        break
    else:
        print("opcion no valida. intente nuevamente.\n ")




