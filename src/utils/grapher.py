import matplotlib.pyplot as plt

def mostrar_graficas(tiempo, señal_continua, indices, señal_discreta, tiempo_discreto, titulo):
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(hspace=0.5)

    # Continua
    plt.subplot(3, 1, 1)
    plt.plot(tiempo, señal_continua, color='blue', linewidth=2)
    plt.title(f"{titulo} (Continua)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Discreta
    plt.subplot(3, 1, 2)
    plt.stem(indices, señal_discreta, linefmt='r', markerfmt='ro', basefmt="k")
    plt.title("Discreta (Índices)")
    plt.xlabel("Índice n")
    plt.ylabel("Amplitud")
    plt.grid(True)

    # Superposición
    plt.subplot(3, 1, 3)
    plt.plot(tiempo, señal_continua, color='blue', linewidth=2, label="Continua")
    plt.stem(tiempo_discreto, señal_discreta, linefmt='r', markerfmt='ro', basefmt="k", label="Discreta")
    plt.title("Comparativa continua y discreta")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def continuous_plotter(t, señal_modificada, titulo, subtitulo, xlabel, ylabel, señal_referencia=None):
    plt.figure(figsize=(8, 4))
    plt.plot(t, señal_modificada, label=subtitulo, color='blue', linewidth=2)

    if señal_referencia is not None:
        plt.plot(t, señal_referencia, '--', color='red', label='Referencia')

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def discrete_plotter(n, señal_modificada, señal_referencia, titulo, xlabel, ylabel):
    plt.figure(figsize=(8, 4))
    plt.stem(n, señal_modificada, linefmt='b-', markerfmt='bo', basefmt="k", label='Modificada')
    plt.stem(n, señal_referencia, linefmt='r--', markerfmt='ro', basefmt="k", label='Referencia')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
