## Proyecto: Procesamiento de Señales (PDS2)

### Descripción

Este proyecto contiene **cuatro tareas** que abordan la generación, análisis y visualización de señales continuas, discretas y digitales en Python. Se utilizan librerías estándar de procesamiento de señales y graficación.

----------

## ✅ **Tareas incluidas**

**Tarea**

**Descripción**

**tarea_1**

Graficación de señales continuas y discretas: seno, exponencial amortiguada, triangular, cuadrada.

**tarea_2**

Generación de una onda senoidal continua parametrizada por su frecuencia.

**tarea_3**

Comparativa de señales senoidales continuas y discretas con diferentes parámetros (A, f, ϕ).

**tarea_4**

Conversión digital-analógica (DAC): Cálculo y graficación de salidas analógicas según los bits.

----------

## 📂 **Estructura del proyecto**


**Estructura del repositorio:**  
├── main.py  
├── .gitignore  
├── requirements.txt  
├── README.md  
├── src/  
│ ├── tarea_1.py  
│ ├── tarea_2.py  
│ ├── tarea_3.py  
│ ├── tarea_4.py 
│ └── utils/  
│ └── grapher.py 

----------

## ⚙️ **Instalación**

1️⃣ **Clona este repositorio:**


`git clone https://github.com/maximotosc04/PDS2.git cd PDS2` 

2️⃣ **(Opcional) Crea un entorno virtual:**

`python -m venv venv # Windows: venv\Scripts\activate # Linux/macOS:  source venv/bin/activate` 

3️⃣ **Instala dependencias:**


`pip install -r requirements.txt` 

----------

## 🚀 **Uso**

`python main.py <tarea> [parámetros]` 

**Tarea**

**Comando**

**tarea_1**

`python main.py tarea_1`

**tarea_2**

`python main.py tarea_2 <frecuencia>`

**tarea_3**

`python main.py tarea_3 <amplitud> <frecuencia> <fase>`

**tarea_4**

`python main.py tarea_4 <bits>`

### 📌 Ejemplos de ejecución:



`python main.py tarea_1
python main.py tarea_2 4
python main.py tarea_3 1 2 0.785
python main.py tarea_4 8` 

----------

## 📦 **Dependencias**

-   Python 3.6 o superior
    
-   numpy
    
-   scipy
    
-   matplotlib
    

Instalación rápida:


`pip install numpy scipy matplotlib` 

----------

## 📄 **Licencia**

Este proyecto está licenciado bajo **MIT**. Consulta el archivo `LICENSE` para más información.