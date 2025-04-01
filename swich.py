while True:
    opcion = input("Elige una opción (1-3, 0 para salir): ")

    if opcion == "1":
        print("Opción 1 seleccionada.")
    elif opcion == "2":
        print("Opción 2 seleccionada.")
    elif opcion == "3":
        print("Opción 3 seleccionada.")
    elif opcion == "0":
        print("👋 Saliendo del programa...")
        break  # Termina el bucle
    else:
        print("❓ Opción no válida. Intenta de nuevo.")
