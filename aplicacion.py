import sys
import sqlite3
from pathlib import Path

def tabla():
    conexion = sqlite3.connect("Baldeon_Figueroa_almacen.db")

    tabla_producto =""" CREATE TABLE Producto(
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT,
                nombre TEXT,
                precio float
                )
                """
    
    cursor = conexion.cursor()
    cursor.execute(tabla_producto)
    conexion.close()

def Registrar():
    conexion = sqlite3.connect("Baldeon_Figueroa_almacen.db") 
    cod = input("Ingrese el código del producto: ")
    nom = input("Ingrese el nombre del producto: ")
    pre =float(input("Ingrese el precio del producto: "))
    consulta = """INSERT INTO 
                PRODUCTO(codigo, nombre, precio) 
                VALUES (?,?,?)"""
    datos=(cod,nom,pre)
    cursor = conexion.cursor()
    cursor.execute(consulta,datos)
    conexion.commit()
    conexion.close
    return menu()
    
def eliminar():
    return 
    
def editar():

    return
    
def listar():
    conexion = sqlite3.connect("Baldeon_Figueroa_almacen.db")
    cursor=conexion.cursor()
    consulta="SELECT * FROM Producto"
    cursor.execute(consulta)
    records = cursor.fetchall()
    print("****************Estos son los productos****************")
    print("{:<8} {:<8} {:<13} {:<9}".format("Id","Código","Nombre","Precio"))
    for row in records:
        print("{:<8} {:<8} {:<13} {:<9}".format(*row))
        print("\n")
    conexion.commit()
    conexion.close()
    return menu()
    
def salir():
    sys.exit()

def menu():
    if Path("Baldeon_Figueroa_almacen.db").exists()==False:
       tabla()
    opcion = input("Menú Opciones \n 1. Registrar \n 2. Eliminar \n 3. Editar \n 4. Listar \n 5. Salir \nIngrese su opción:")  
    if opcion == "1":
        Registrar()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        editar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        salir()
        
menu()
    
