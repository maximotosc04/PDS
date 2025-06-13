import numpy as np
from scipy.signal import sawtooth, square
from src.utils.grapher import mostrar_graficas
import matplotlib.pyplot as plt

def crear_y_mostrar_graficas():
    """Genera señales continuas y discretas y las muestra en gráficas."""

    # Parámetros base
    frecuencia = 2       # Frecuencia fundamental (Hz)
    fs = 40.0            # Frecuencia de muestreo (Hz)
    Ts = 1.0 / fs        # Periodo de muestreo
    t_continuo = np.linspace(-1, 5, 1000)  # Tiempo continuo
    indices = np.arange(-40, 201)          # Índices para la señal discreta
    t_discreto = indices * Ts

    # Conjunto de señales a graficar
    lista_senales = [
        {
            "titulo": "Señal seno: x₁(t) = sin(2πft)",
            "continuo": np.sin(2 * np.pi * frecuencia * t_continuo),
            "discreto": np.sin(2 * np.pi * frecuencia * t_discreto)
        },
        {
            "titulo": "Exponencial amortiguada: x₂(t) = e^(-2t)·u(t)",
            "continuo": np.exp(-2 * t_continuo) * (t_continuo >= 0),
            "discreto": np.exp(-2 * t_discreto) * (t_discreto >= 0)
        },
        {
            "titulo": "Triangular periódica: x₃(t) = tri(t, f)",
            "continuo": sawtooth(2 * np.pi * frecuencia * t_continuo, width=0.5),
            "discreto": sawtooth(2 * np.pi * frecuencia * t_discreto, width=0.5)
        },
        {
            "titulo": "Cuadrada periódica: x₄(t) = sq(t, f)",
            "continuo": square(2 * np.pi * frecuencia * t_continuo),
            "discreto": square(2 * np.pi * frecuencia * t_discreto)
        }
    ]

    # Generar gráficas
    for senal in lista_senales:
        mostrar_graficas(t_continuo, senal["continuo"], indices, senal["discreto"], t_discreto, senal["titulo"])

    # 👈 Esto asegura que todas las ventanas se muestren correctamente al final
    plt.show()

if __name__ == "__main__":
    crear_y_mostrar_graficas()
