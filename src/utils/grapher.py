import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

def plot_signals(t, n, ts, señales):
    """Genera gráficas comparando la señal modificada con la de referencia"""
    plt.style.use('ggplot')
    
    # Configurar figura con 2 subplots (continuo y discreto)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.suptitle('Comparación de señales sinusoidales', y=1.02)
    
    # Señal en tiempo continuo
    ax1.plot(t, señales['referencia']['analogica'], '--b', lw=1.5, label='Referencia')
    ax1.plot(t, señales['modificada']['analogica'], '-r', lw=1.5, label='Modificada')
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Amplitud')
    ax1.set_title('Señal analógica continua')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Señal en tiempo discreto
    # Usamos stem para la señal discreta
    markerline, stemlines, baseline = ax2.stem(n*ts, señales['referencia']['discreta'], linefmt='--b', markerfmt='bo', basefmt=" ", label='Referencia')
    markerline, stemlines, baseline = ax2.stem(n*ts, señales['modificada']['discreta'], linefmt='-r', markerfmt='ro', basefmt=" ", label='Modificada')
    ax2.set_xlabel('Tiempo (s)')
    ax2.set_ylabel('Amplitud')
    ax2.set_title('Señal discreta')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    plt.show()