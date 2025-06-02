import numpy as np
from scipy.signal import sawtooth, square
from src.utils.grapher import plot_signals

def generar_datos():
    """Genera todas las señales y las envía a graficar"""
    
    t = np.linspace(-1.0, 5.0, 1000)
    fs = 40.0  
    ts = 1.0 / fs  
    n = np.arange(-40, 201)  
    
    señales = {
        'senoidal': _generar_senoidal(t, n, fs),
        'exponencial': _generar_exponencial(t, n, ts),
        'triangular': _generar_triangular(t, n, ts),
        'cuadrada': _generar_cuadrada(t, n, ts)
    }
    
    plot_signals(t, n, ts, señales)

def _generar_senoidal(t, n, fs):
    F = 2  
    return {
        'analogica': np.sin(2 * np.pi * F * t),
        'discreta': np.sin(2 * np.pi * F * n / fs),
        'titulo': 'Señal senoidal'
    }

def _generar_exponencial(t, n, ts):
    return {
        'analogica': np.exp(-2 * t) * (t >= 0),
        'discreta': np.exp(-2 * n * ts) * (n * ts >= 0),
        'titulo': 'Señal exponencial'
    }

def _generar_triangular(t, n, ts):
    f_tri = 2
    return {
        'analogica': sawtooth(2 * np.pi * f_tri * t, width=0.5),
        'discreta': sawtooth(2 * np.pi * f_tri * n * ts, width=0.5),
        'titulo': 'Señal triangular'
    }

def _generar_cuadrada(t, n, ts):
    f_sq = 2
    return {
        'analogica': square(2 * np.pi * f_sq * t),
        'discreta': square(2 * np.pi * f_sq * n * ts),
        'titulo': 'Señal cuadrada'
    }

if __name__ == "__main__":
    generar_datos()