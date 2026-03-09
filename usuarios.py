from colorama import Fore, init

init()

def registrar_prestamo(inventario):
    print( "=" * 30)
    print("   REGISTRO DE TRAZABILIDAD")
    print("=" * 30)
    
    objeto_id = input(Fore.BLUE +"Ingrese el nombre o ID del objeto: ").strip()
    responsable = input(Fore.BLUE + "Ingrese el nombre del responsable: ").strip()

    if objeto_id and responsable:
        inventario[objeto_id] = responsable
        print(Fore.GREEN + f"[OK] El objeto '{objeto_id}' ha sido asignado a '{responsable}'." + Fore.RESET)
    else:
        print(Fore.RED + "[ERROR] El ID del objeto y el responsable son obligatorios." + Fore.RESET)

def mostrar_reporte(inventario):
    print("=" * 30)
    print("   REPORTE DE INVENTARIO")
    print("=" * 30)
    
    if not inventario:
        print("No hay objetos registrados.")
    else:
        for obj, resp in inventario.items():
            print(f"Objeto: {obj} - Responsable: {resp}")
    
    print("=" * 30)

def menu_principal():
    """
    Función de la Persona D: Menú interactivo con ciclo while.
    Une el trabajo de las Personas B y C.
    """
    inventario_escolar = {}  # Diccionario donde se guardará todo
    
  
    while True:
        print("\n" + "=".center(40, "="))
        print(Fore.BLUE + " SISTEMA DE CONTROL DE PRESTAMOS " )
        print("=".center(40, "="))
        print("1. Registrar nuevo préstamo ")
        print("2. Ver reporte de inventario ")
        print("3. Salir")
        print("=".center(40, "=") + Fore.RESET)
        
        opcion = input("Elija una opción (1-3): ")
        
        if opcion == "1":
          
            registrar_prestamo(inventario_escolar)
        elif opcion == "2":
         
            mostrar_reporte(inventario_escolar)
        elif opcion == "3":
            print(Fore.LIGHTYELLOW_EX+"\n abriendose del parche")
            break  
        else:
            print("\n[!] Error: Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()