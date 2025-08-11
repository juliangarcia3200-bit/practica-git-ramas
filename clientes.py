clientes = [
    {"id": 1, "nombre": "Ana", "edad": 30, "saldo": 1000000.0},
    {"id": 2, "nombre": "Luis Efanier", "edad": 25, "saldo": 1500000.0},
    {"id": 3, "nombre": "Marta", "edad": 28, "saldo": 2000000.0}
]

def mostrar_clientes():
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}, Edad: {cliente['edad']}, Saldo: {cliente['saldo']}")

if __name__ == "__main__":
    mostrar_clientes()