from src.tarea_1 import generar_datos
from src.tarea_2 import capturar as capturar_t2
from src.tarea_3 import capturar as capturar_t3
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <tarea> [argumentos]")
        print("Tareas disponibles:")
        print(" - tarea_1")
        print(" - tarea_2")
        print(" - tarea_3 <amplitud> <frecuencia> <fase>")
        return
    
    tarea = sys.argv[1]
    
    if tarea == "tarea_1":
        generar_datos()
    elif tarea == "tarea_2":
        capturar_t2()
    elif tarea == "tarea_3":
        if len(sys.argv) < 5:
            print("Uso para tarea_3: python main.py tarea_3 <amplitud> <frecuencia> <fase>")
            return
        capturar_t3()
    else:
        print(f"Tarea '{tarea}' no reconocida")

if __name__ == "__main__":
    main()