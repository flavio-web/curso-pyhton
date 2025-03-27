
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
    
    
for i in range(5):  # Genera los números 0, 1, 2, 3, 4
    print(i)
    
    
print("---- range con argumento inicial ----")
for i in range(2, 10, 2):  # Empieza en 2, llega hasta 10 (sin incluirlo), con saltos de 2
    print(i)


datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in datos.items():
    print(f"{clave}: {valor}")
