import numpy as np
from src.utils.grapher import continuous_plotter

def graficar_onda(frecuencia_deseada):
    """Genera y grafica una señal senoidal continua con frecuencia dada."""

    # Parámetros de la señal
    amplitud = 1.0
    frecuencia = float(frecuencia_deseada)
    t = np.linspace(0.0, 5.0, 1000)
    xt = amplitud * np.sin(2 * np.pi * frecuencia * t)

    # Parámetros para graficar
    titulo = f"Onda Senoidal Continua - Frecuencia: {frecuencia} Hz"
    subtitulo = "Señal senoidal"
    xlabel = "Tiempo [s]"
    ylabel = "Amplitud"

    # Mostrar la gráfica
    continuous_plotter(t, xt, titulo, subtitulo, xlabel, ylabel)

if __name__ == "__main__":
    # Prueba directa (puedes eliminar esto si solo usas el main.py)
    graficar_onda(2)