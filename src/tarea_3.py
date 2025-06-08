import numpy as np
from src.utils.grapher import plot_signals
import sys

def capturar():
    """Genera todas las señales y las envía a graficar"""
    
    A = float(sys.argv[2])
    F = float(sys.argv[3])
    R = float(sys.argv[3])
    print(A, F, R)
    t = np.linspace(-1.0, 5.0, 1000)
    fs = 40.0
    ts = 0.01
    n = np.arange(-40, 201)
    
    señales = { 
        'senoidal': _generar_senoidal(t, n, fs, F, A, R, ts),
    }
    
    plot_signals(t, n, ts, señales, F)

def _generar_senoidal(t, n, fs, F, A, R, ts):
    return {
        'analogica': (A * np.sin(2 * np.pi * F * t + R)),
        'discreta': (A * np.sin(2 * np.pi * F * n * ts + R)),
        'titulo': 'Señal senoidal'
    }

if _name_ == "_   main_":
    capturar()