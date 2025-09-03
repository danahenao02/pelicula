"""
    
NETFLIX CONSOLE
Proyecto de programación en Python
Autor: [dana henao]
Fecha: [14 agosto]


"""

import json
import os
import sys


favoritas = []  
historial = []  

"""
NETFLIX CONSOLE - Carga de datos JSON
"""

def cargar_peliculas():
    """

    
    """
    try:
        
        if not os.path.exists('peliculas.json'):
            print(" Error: No se encontró el archivo 'peliculas.json'")
            print(" Asegúrate de que esté en la misma carpeta que main.py")
            return None
        
        with open('peliculas.json', 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)
            

        if not peliculas:
            print(" Error: El archivo JSON está vacío")
            return None
            
        return peliculas
        
    except json.JSONDecodeError as e:
        print(f" Error: El archivo JSON tiene formato incorrecto")
        print(f"Detalle del error: {e}")
        return None
    except Exception as e:
        print(f" Error inesperado: {e}")
        return None

def mostrar_estadisticas_carga(peliculas):
    """
    
    """
    if not peliculas:
        return
    
    print("\n ESTADÍSTICAS DE CARGA:")
    print("=" * 30)
    
    total_peliculas = 0
    for genero, lista_peliculas in peliculas.items():
        cantidad = len(lista_peliculas)
        total_peliculas += cantidad
        print(f" {genero.replace('_', ' ').title()}: {cantidad} películas")
    
    print("=" * 30)
    print(f" Total de películas: {total_peliculas}")
    
   
    mejor_pelicula = None
    mejor_rating = 0
    
    for genero in peliculas.values():
        for pelicula in genero:
            if pelicula['rating'] > mejor_rating:
                mejor_rating = pelicula['rating']
                mejor_pelicula = pelicula
    
    if mejor_pelicula:
        print(f" Mejor calificada: {mejor_pelicula['titulo']} ({mejor_rating}/10)")

def limpiar_pantalla():
     """ limpiar pantalla de la consola"""
     os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_header():
    """muestra el encabezado del programa"""
    print("=" * 60)
    print("" * 20 + "NETFLIX CONSOLE" + "" * 20 )
    print("=" * 60)

def mostrar_menu_principal():
        """muestra el menu principal con todas las opciones"""
        print("que quieres hacer hoy?")
        print("-" * 35)
        print("1 peliculas de accion")
        print("2 peliculas de comedia")
        print("3 peliculas de terror")
        print("4 peliculas de romance")
        print("5 pelivulas de ciencia ficcion")
        print("6 buscar pelicula especifica")
        print("7 top 10 mejores calificadas")
        print("8 ver mis peliculas favoritas")
        print("9 estadisticas del sistema")
        print("0 salir del programa")
        print("-" * 35)

def obtener_opcion_usuario():

    while True:
        try:
            opcion = input("\n elige una opcion (0-9):").strip()
        
            if opcion in ['0','1','2','3','4','5','6','7','8','9']:
                return opcion
        
            else:
                print("opcion no valida. usa numeros del 0 al 9.")
                pass

        except KeyboardInterrupt:
            print("\n\¡hasta luego!")
            sys.exit(0)
        except Exception as e:
            
            print(f"error: {e}")

def pausar():
    """pausa el programa hasta que el usuario presione enter"""
    input("\npresiona enter para continuar...")

def main():

    """Función principal del programa"""
    print("Iniciando Netflix Console...")
    
    print("Programa iniciado correctamente")

    """Función principal del programa """
    print("  NETFLIX CONSOLE - Cargando datos...")
    print("=" * 50)
    

    print(" Cargando películas desde peliculas.json...")
    peliculas = cargar_peliculas()
    
    if peliculas:
        print("¡Películas cargadas exitosamente!")
        mostrar_estadisticas_carga(peliculas)
    else:
        print(" Error: No se pudieron cargar las películas")
        print(" Revisa que el archivo peliculas.json esté en la carpeta correcta")
        return
    
    print("\n Sistema listo para usar")
    """funcion principal con bucle de menu interactivo"""

    print("iniciando netflix console")
    peliculas = cargar_peliculas()
    if not peliculas:
        print ("nos e puede continuar sin las peliculas")

    print("sistema cargando correctamente")
    pausar()

    #bucle principal del menu
    while True:
        limpiar_pantalla()
        mostrar_header()
        
        mostrar_menu_principal()

        opcion = obtener_opcion_usuario

        #procesar la opcion elegida
        if opcion == "0":
            limpiar_pantalla()
            print("¡gracias por usar Netflix console!")
            print("¡que disfrutes viendo peliculas!")
            print("¡hasta la proxima!")
            break

        elif opcion == "1":
            procesar_seleccion_genero(peliculas, "accion", "ACCIÓN")
            
        elif opcion == "2":
            procesar_seleccion_genero(peliculas, "comedia", "COMEDIA")
            
        elif opcion == "3":
            procesar_seleccion_genero(peliculas, "terror", "TERROR")
            
        elif opcion == "4":
            procesar_seleccion_genero(peliculas, "romance", "ROMANCE")
            
        elif opcion == "5":
            procesar_seleccion_genero(peliculas, "ciencia_ficcion", "CIENCIA FICCIÓN")

        elif opcion == "6":
            print("\n Has elegido: BUSCAR PELÍCULA")
            print(" Función en desarrollo...")
            pausar()

        elif opcion == "7":
            print("\n Has elegido: TOP 10")
            print(" Función en desarrollo...")
            pausar()

        elif opcion == "8":
            print("\n Has elegido: MIS FAVORITAS")
            print(" Función en desarrollo...")
            pausar()
            
        elif opcion == "9":
            limpiar_pantalla()
            mostrar_header()
            mostrar_estadisticas_carga(peliculas)
            pausar()
            print(" PELÍCULAS DE {nombre_genero.upper}" )
            print("=" * 60)
    
    lista_peliculas = peliculas['genero']
    
    
    print(f"{'#':<3} {'TÍTULO':<35} {'AÑO':<6} {'RATING':<8}")
    print("━" * 60)
    
    
    for i, pelicula in enumerate(lista_peliculas, 1):
        titulo = pelicula['titulo']
        if len(titulo) > 32:
            titulo = titulo[:29] + "..."
            
        print(f"{i:<3} {titulo:<35} {pelicula['año']:<6} {pelicula['rating']:<7}")
    
    print("━" * 60)
    print(f"{len(lista_peliculas) + 1}. ⬅ Volver al menú principal")
    
    return seleccionar_pelicula_genero(lista_peliculas)

def seleccionar_pelicula_genero(lista_peliculas):
    while True:
        try:
            print(f"\ Elige una película (1-{len(lista_peliculas)}) o {len(lista_peliculas) + 1} para volver: ", end="")
            opcion = input().strip()
            
            if opcion == str(len(lista_peliculas) + 1):
                return None  
            
            numero = int(opcion)
            if 1 <= numero <= len(lista_peliculas):
                return lista_peliculas[numero - 1]
            else:
                print(f" Número fuera de rango. Usa 1-{len(lista_peliculas)} o {len(lista_peliculas) + 1}")
        
        except ValueError:
            print(" Por favor ingresa un número válido")
        except KeyboardInterrupt:
            return None
        
def procesar_seleccion_genero(peliculas, genero, nombre_genero):
    while True:
                pelicula_seleccionada = mostrar_peliculas_genero(peliculas, genero, nombre_genero)
                if pelicula_seleccionada is None:
                    break  #volver al menu principal
                print(f"\n Seleccionaste: {pelicula_seleccionada['titulo']}")
    print(" Función de detalles en desarrollo...")
    pausar()

def main():
        print("iniciando Netflix Console. . .")
        peliculas = cargar_peliculas()

        if not peliculas:
            print("❌no se puede continuar si ls peliculas")
            return
        print("✅sistema cargando correctamente")

        while True:
            limpiar_pantalla()
            mostrar_header()
            mostrar_menu_principal()

            opcion = obtener_opcion_usuario()

def mostrar_detalle_pelicula(pellicula):
    limpiar_pantalla()
    
    