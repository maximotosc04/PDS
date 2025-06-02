# src/utils/grapher. py
import matplotlib.pyplot as plt

def plot_signals(t, n, ts, señales):
    """Genera todas las gráficas para cada tipo de señal"""
    plt.style.use('ggplot')
    
    for nombre, señal in señales.items():
        _plot_signal(t, n, ts, señal['analogica'], señal['discreta'], señal['titulo'])
    
    plt.show()

def _plot_signal(t, n, ts, xt, xn, titulo):
    """Genera los 3 subplots para una señal específica"""
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(hspace=0.65)
    plt.suptitle(titulo)

    # Señal analógica
    plt.subplot(3, 1, 1)
    plt.plot(t, xt, '-b', lw=2)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.title('Señal analógica')
    plt.grid(True, linestyle='--', alpha=0.6)

    # Señal discreta 
    plt.subplot(3, 1, 2)
    plt.stem(n, xn, linefmt='r', markerfmt='r.')
    plt.xlabel('índice de muestra (n)')
    plt.ylabel('amplitud')
    plt.title('Señal discreta')
    plt.grid(True, linestyle='--', alpha=0.6)

    # Señal sobrepuesta
    plt.subplot(3, 1, 3)
    plt.plot(t, xt, '-b', lw=2)
    plt.stem(n*ts, xn, linefmt='r', markerfmt='r.')
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.title('Señal sobrepuesta')
    plt.grid(True, linestyle='--', alpha=0.6)