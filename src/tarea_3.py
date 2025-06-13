import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter

def graficar_senal_con_parametros(amplitud, frecuencia, fase):
    # Señal continua
    t = np.linspace(0, 2, 1000)
    xt_modificada = amplitud * np.sin(2 * np.pi * frecuencia * t + fase)
    xt_referencia = np.sin(2 * np.pi * 1.0 * t + 0)  # A=1, f=1Hz, φ=0

    titulo_cont = f"Señal Continua y Referencia\nA={amplitud}, f={frecuencia}Hz, ϕ={fase} rad"
    continuous_plotter(t, xt_modificada, titulo_cont, f"A={amplitud}, f={frecuencia}Hz, ϕ={fase} rad", "Tiempo [s]", "Amplitud", xt_referencia)

    # Señal discreta
    Ts = 0.01
    n = np.arange(0, 200)
    tn = n * Ts
    xn_modificada = amplitud * np.sin(2 * np.pi * frecuencia * tn + fase)
    xn_referencia = np.sin(2 * np.pi * 1.0 * tn + 0)

    titulo_disc = f"Señal Discreta y Referencia\nA={amplitud}, f={frecuencia}Hz, ϕ={fase} rad"
    discrete_plotter(n, xn_modificada, xn_referencia, titulo_disc, "Índice n", "Amplitud")