# main.py
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <tarea> [argumentos]")
        print("Tareas disponibles:")
        print(" - tarea_1")
        print(" - tarea_2")
        print(" - tarea_3 <amplitud> <frecuencia> <fase>")
        print(" - tarea_4 [bits]")
        return
    
    tarea = sys.argv[1]
    
    try:
        if tarea == "tarea_1":
            from src.tarea_1 import generar_datos
            generar_datos()
        elif tarea == "tarea_2":
            from src.tarea_2 import capturar
            capturar()
        elif tarea == "tarea_3":
            if len(sys.argv) < 5:
                print("Error: Requiere amplitud, frecuencia y fase")
                print("Ejemplo: python main.py tarea_3 1 2 0.785")
                return
            from src.tarea_3 import capturar as capturar_t3
            capturar_t3()
        elif tarea == "tarea_4":
            from src.tarea_4 import simular_dac
            bits = int(sys.argv[2]) if len(sys.argv) > 2 else 8
            simular_dac(bits)
        else:
            print(f"Error: Tarea '{tarea}' no reconocida")
    except ImportError as e:
        print(f"Error de importación: {e}")
        print("Verifica que los archivos existan y los nombres de las funciones")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()