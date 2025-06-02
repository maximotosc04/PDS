## Tarea 1: Graficación de Señales

  

## Descripción

Este proyecto proporciona funciones para generar y visualizar señales continuas y muestreadas en Python. Incluye cuatro tipos de señales:

  

- **x₁(t)**: Senoidal de frecuencia 2 Hz.

- **x₂(t)**: Exponencial decreciente multiplicada por la función escalón (u(t)).

- **x₃(t)**: Onda triangular simétrica de frecuencia 2 Hz.

- **x₄(t)**: Onda cuadrada de frecuencia 2 Hz.

  

La salida principal es una gráfica con las versiones continuas y muestreadas de cada señal.

  

## Estructura del Proyecto

├── main.py  
├── .gitignore  
├── requirements.txt  
├── README.md
------├── src/  
---------├──utils/   
--------------├── grapher.py  
------├── tarea1.py

## Instalación

**1. Clona este repositorio:**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/maximotosc04/PDS.git
   cd PDS
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
  

## Uso


Para ejecutar una actividad (ejemplo, en tu caso debes colocar tarea_1):
```bash
  python main.py act_1
```

  
## Dependencias: 
- Python 3.6 o superior

- [NumPy](https://numpy.org/)

- [SciPy](https://scipy.org/)

- [Matplotlib](https://matplotlib.org/)

 

  

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo \LICENSE\ para más detalles.
