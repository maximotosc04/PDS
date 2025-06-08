# src/utils/grapher.py
import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

# Función genérica para Tareas 1-2
def plot_signals(t, signals_dict, title="Señal"):
    """Grafica múltiples señales desde un diccionario"""
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 4))
    
    for label, signal in signals_dict.items():
        plt.plot(t, signal, label=label)
    
    plt.title(title)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Función específica para Tarea 3
def plot_continuous_discrete(t, n, ts, cont_signal, disc_signal, title, reference_signal=None):
    """Muestra señal continua y discreta con opción de referencia"""
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    
    # Graficar referencia si existe
    if reference_signal:
        ax1.plot(t, reference_signal['analogica'], '--b', label='Referencia')
        ax2.stem(n*ts, reference_signal['discreta'], linefmt='--b', markerfmt='bo', basefmt=" ", label='Referencia')
    
    # Señal principal
    ax1.plot(t, cont_signal, '-r', label='Señal modificada')
    ax1.set_title(f'{title} (Continua)')
    ax1.set_xlabel('Tiempo [s]')
    ax1.set_ylabel('Amplitud')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    ax2.stem(n*ts, disc_signal, linefmt='-r', markerfmt='ro', basefmt=" ", label='Señal modificada')
    ax2.set_title(f'{title} (Discreta)')
    ax2.set_xlabel('Tiempo [s]')
    ax2.set_ylabel('Amplitud')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

# Función específica para Tarea 4
def plot_dac_conversion(t, original, digital, reconstructed, bits):
    """Muestra el proceso completo ADC-DAC"""
    plt.style.use('ggplot')
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
    
    ax1.plot(t, original, '-b')
    ax1.set_title('Señal Analógica Original')
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    ax2.stem(t[::len(t)//20], digital[::len(t)//20], linefmt='-r', markerfmt='ro', basefmt=" ")
    ax2.plot(t, digital, ':r', alpha=0.5)
    ax2.set_title(f'Señal Digitalizada ({bits} bits, {2**bits} niveles)')
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    ax3.plot(t, reconstructed, '-g')
    ax3.set_title('Señal Reconstruida por DAC')
    ax3.grid(True, linestyle='--', alpha=0.6)
    
    plt.suptitle(f'Proceso de Conversión Digital-Analógico (DAC de {bits} bits)')
    plt.tight_layout()
    plt.show()