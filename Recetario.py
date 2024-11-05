from pathlib import Path
import os
from os import system
def bienvenida():
    base = Path.home()
    guia = Path(base, 'Recetas')
    num_recetas = 0
    for txt in Path(guia).glob("**/*.txt"):
        num_recetas += 1
    print(f"hola, tus recetas estan en {guia}. Tienes {num_recetas} recetas")

def elegir_opciones():
    opcion = int(input(f"Ingresa el numero de la accion que quieras realizar:\n"
                       f"[1] - Leer Receta\n"
                       f"[2] - Crear Receta\n"
                       f"[3] - Crear Categoria\n"
                       f"[4] - Eliminar Receta\n"
                       f"[5] - Eliminar Categoria\n"
                       f"[6] - Finalizar Programa\n"))
    return opcion

def elegir_categoria():
    base = Path.home()
    guia = Path(base, 'Recetas')
    categoria = os.listdir(guia)
    seleccion = input(f"Elige la categoria escribiendo su nombre\n{categoria}\n")
    nuevaruta = Path(guia, seleccion)
    return nuevaruta

def elegir_receta(categoria):
    loc = os.listdir(categoria)
    selec = input(f"Estas son las recetas de esta categoria:\n"
                f"{loc}\n"
                f"Elige la receta escribiendo su nombre:\n") + ".txt"
    rutanueva = Path(categoria, selec)
    return(rutanueva)

def mostrar_receta(receta):
    archivo = receta
    print(archivo.read_text())

def crear_receta(categoria):
    loc = Path(categoria)
    nombre = input("Escribe el nombre de la nueva receta:\n") + ".txt"
    nuevapath = Path(loc,nombre)
    contenido = input("Escribe el contenido de la receta:\n")
    nuevapath.write_text(contenido)
    print(f"La receta {nombre} ha sido creada!")

def crear_categoria():
    nombre = input("Escribe el nombre de la nueva categoria:\n")
    base = Path.home()
    guia = Path(base, 'Recetas')
    nuevaruta = Path(guia,nombre)
    nuevaruta.mkdir()
    print("La nueva categoria ha sido creada")

def eliminar_receta():
    ruta = Path(elegir_receta(elegir_categoria()))
    ruta.unlink()
    print("La receta ha sido eliminada")

def eliminar_categoria(categoria):
    ruta = Path(categoria)
    for txt in Path(ruta).glob("**/*.txt"):
        txt.unlink()
    ruta.rmdir()
    print("La categoria ha sido eliminada")

def recetario():
    bienvenida()
    opcion = elegir_opciones()
    while opcion != 6:
        if opcion == 1:
            mostrar_receta(elegir_receta(elegir_categoria()))
        if opcion == 2:
            crear_receta(elegir_categoria())
        if opcion == 3:
            crear_categoria()
        if opcion == 4:
            eliminar_receta()
        if opcion == 5:
            eliminar_categoria(elegir_categoria())
        print(input("Ingresa cualquier tecla para regresar al menu:\n"))
        system('cls')
        opcion = elegir_opciones()
    print("Hasta luego!")
    return True

recetario()