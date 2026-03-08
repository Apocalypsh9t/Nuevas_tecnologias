def registrar_prestamo(inventario):
    print( "=" * 30)
    print("   REGISTRO DE TRAZABILIDAD")
    print("=" * 30)
    
    objeto_id = input("Ingrese el nombre o ID del objeto: ").strip()
    responsable = input("Ingrese el nombre del responsable: ").strip()

    if objeto_id and responsable:
        inventario[objeto_id] = responsable
        print(f"[OK] El objeto '{objeto_id}' ha sido asignado a '{responsable}'.")
    else:
        print("[ERROR] El ID del objeto y el responsable son obligatorios.")

if __name__ == "__main__":
    trazabilidad_escolar = {}

    registrar_prestamo(trazabilidad_escolar)

    print("Diccionario actual:", trazabilidad_escolar)