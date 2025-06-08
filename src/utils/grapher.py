# src/utils/grapher.py
import matplotlib.pyplot as plt

def plot_signals(t, n, ts, señales, F):
    """Genera todas las gráficas para cada tipo de señal"""
    plt.style.use('ggplot')
    
    for nombre, señal in señales.items():
        _plot_signal(t, n, ts, señal['analogica'], señal['discreta'], señal['titulo'], F)
    plt.show()

def _plot_signal(t, n, ts, xt, xn, titulo, F):
    """Genera los 3 subplots para una señal específica"""
    plt.figure(figsize=(7, 6))
    plt.subplots_adjust(wspace=2, hspace=0.45)
    plt.suptitle(titulo)

    plt.subplot(1, 1, 1)
    plt.plot(t, xt, '-b', lw=2)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.title(f'Señal senoidal con frecuencia de: {F} hz')
    plt.grid(True, linestyle='--', alpha=0.6)