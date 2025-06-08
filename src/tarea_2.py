import numpy as np
from src.utils.grapher import plot_signals
import sys

def capturar():
    """Genera todas las señales y las envía a graficar"""
    
    F = float(sys.argv[2])
    print(F)
    t = np.linspace(-1.0, 5.0, 1000)
    fs = 40.0
    ts = 1.0/fs
    n = np.arange(-40, 201)
    
    señales = { 
        'senoidal': _generar_senoidal(t, n, fs, F),
    }
    
    plot_signals(t, n, ts, señales, F)

def _generar_senoidal(t, n, fs, F):
    return {
        'analogica': np.sin(2 * np.pi * F * t),
        'discreta': np.sin(2 * np.pi * F * n / fs),
        'titulo': 'Señal senoidal'
    }

if __name__ == "_   _main__":
    capturar()