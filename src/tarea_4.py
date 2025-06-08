import numpy as np
from src.utils.grapher import plot_dac_conversion
import sys

def simular_dac(default_bits=8):
    """Simula el proceso completo de conversión ADC-DAC"""
    try:
        bits = int(sys.argv[2]) if len(sys.argv) > 2 else default_bits
    except (ValueError, IndexError):
        print("¡Error en bits! Usando valor por defecto (8 bits)")
        bits = default_bits
    
    # 1. Generar señal analógica original
    t = np.linspace(0, 1, 1000)  # 1 segundo
    f = 2  # Hz
    original = np.sin(2 * np.pi * f * t)
    
    # 2. Proceso de digitalización (ADC)
    niveles = 2**bits
    digital = np.round(original * (niveles/2 - 1)) / (niveles/2 - 1)
    
    # 3. Reconstrucción (DAC) - Filtrado simple
    reconstructed = np.convolve(digital, np.ones(10)/10, mode='same')
    
    # 4. Visualización
    plot_dac_conversion(t, original, digital, reconstructed, bits)

if __name__ == "__main__":
    simular_dac()