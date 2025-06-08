import numpy as np
from src.utils.grapher import plot_signals
import sys

def capturar():
    """Genera todas las señales y las envía a graficar"""
    if len(sys.argv) < 4:
        print("Uso: python main.py tarea_3 <amplitud> <frecuencia> <fase>")
        return
    
    try:
        A = float(sys.argv[2])  # Amplitud
        F = float(sys.argv[3])  # Frecuencia (Hz)
        phi = float(sys.argv[4])  # Fase (radianes)
    except (ValueError, IndexError):
        print("Error: Los parámetros deben ser números (A F phi)")
        return
    
    # Parámetros fijos
    t = np.linspace(0, 2.0, 1000)  # De 0 a 2 segundos para ver 2 ciclos de la referencia
    ts = 0.01  # Periodo de muestreo
    n = np.arange(0, 201)  # Muestras discretas
    
    # Generar ambas señales (modificada y referencia)
    señales = {
        'modificada': {
            'analogica': A * np.sin(2 * np.pi * F * t + phi),
            'discreta': A * np.sin(2 * np.pi * F * n * ts + phi),
            'titulo': f'Señal modificada: A={A}, F={F}Hz, φ={phi:.2f}rad'
        },
        'referencia': {
            'analogica': 1 * np.sin(2 * np.pi * 1 * t + 0),
            'discreta': 1 * np.sin(2 * np.pi * 1 * n * ts + 0),
            'titulo': 'Señal de referencia: A=1, F=1Hz, φ=0'
        }
    }
    
    plot_signals(t, n, ts, señales)

if __name__ == "__main__":
    capturar()