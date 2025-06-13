import sys
from src.tarea_1 import crear_y_mostrar_graficas
from src.tarea_2 import graficar_onda
from src.tarea_3 import graficar_senal_con_parametros
from src.tarea_4 import calcular_dac

def mostrar_ayuda():
    print("\nUso correcto:")
    print("  python main.py tarea_1")
    print("  python main.py tarea_2 <frecuencia>")
    print("  python main.py tarea_3 <amplitud> <frecuencia> <fase>")
    print("  python main.py tarea_4 <bits>\n")

def main():
    if len(sys.argv) < 2:
        print("Error: No se indicó ninguna tarea.")
        mostrar_ayuda()
        return

    opcion = sys.argv[1]

    if opcion == "tarea_1":
        crear_y_mostrar_graficas()

    elif opcion == "tarea_2":
        if len(sys.argv) < 3:
            print("Error: Falta el parámetro <frecuencia>")
            mostrar_ayuda()
            return
        frecuencia = float(sys.argv[2])
        graficar_onda(frecuencia)

    elif opcion == "tarea_3":
        if len(sys.argv) < 5:
            print("Error: Faltan parámetros <amplitud> <frecuencia> <fase>")
            mostrar_ayuda()
            return
        amplitud = float(sys.argv[2])
        frecuencia = float(sys.argv[3])
        fase = float(sys.argv[4])
        graficar_senal_con_parametros(amplitud, frecuencia, fase)

    elif opcion == "tarea_4":
        if len(sys.argv) < 3:
            print("Error: Falta el parámetro <bits>")
            mostrar_ayuda()
            return
        bits = int(sys.argv[2])
        calcular_dac(bits)

    else:
        print(f"Error: Tarea desconocida '{opcion}'")
        mostrar_ayuda()

if __name__ == "__main__":
    main()