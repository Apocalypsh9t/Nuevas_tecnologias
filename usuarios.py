from colorama import Fore,Style, init

init()#

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

if __name__ == "__main__":
    trazabilidad_escolar = {}

    registrar_prestamo(trazabilidad_escolar)

    print(Fore.CYAN + Style.BRIGHT + "Diccionario actual:", trazabilidad_escolar)