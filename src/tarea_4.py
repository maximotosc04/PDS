import numpy as np
from src.utils.grapher import continuous_plotter

def calcular_dac(bits):
    VFS = 5.0  # Voltaje de referencia máximo
    niveles = 2 ** bits
    paso = VFS / (niveles - 1)
    resolucion = 100 / (niveles - 1)

    entradas = np.arange(niveles)
    salidas_analogicas = entradas * paso

    print("\nResultados del DAC:")
    print(f"Bits: {bits}")
    print(f"Niveles: {niveles}")
    print(f"Tamaño del paso: {paso:.4f} V")
    print(f"Resolución: {resolucion:.4f} %")

    titulo = f"Salida Analógica del DAC de {bits} bits"
    continuous_plotter(entradas, salidas_analogicas, titulo, "Salida del DAC", "Entrada Digital", "Voltaje de Salida [V]")