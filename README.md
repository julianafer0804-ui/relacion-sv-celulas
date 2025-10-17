# Visualizador Interactivo de la Relación Superficie-Volumen Celular

Esta es una aplicación interactiva construida con Streamlit para explorar y visualizar la relación fundamental entre la superficie y el volumen de una esfera, un concepto clave en la biología celular.

![Recording 2025-10-17 200649](https://github.com/user-attachments/assets/574d7117-0f7d-4150-ba5c-e7fdcb3c45ff) 


## Descripción del Problema

La relación superficie-volumen es un principio fundamental que explica por qué las células son microscópicas. A medida que una célula aumenta de tamaño, su volumen crece mucho más rápido que su área de superficie. Esto limita el tamaño celular, ya que la membrana (superficie) debe ser lo suficientemente grande para servir a todo el citoplasma (volumen).

Esta aplicación permite a los usuarios manipular el radio de una esfera y observar de forma instantánea cómo cambian su superficie, volumen y, lo más importante, la relación entre ambos.

## Características

* **Slider Interactivo:** Modifica el radio de la esfera en tiempo real.
* **Visualización 3D:** Un gráfico interactivo de Plotly muestra la esfera cambiando de tamaño.
* **Gráfico 2D:** Una gráfica muestra cómo decae la relación S/V a medida que aumenta el radio de la célula.
* **Cálculos en Vivo:** La superficie, el volumen y la relación S/V se actualizan automáticamente.
* **Sección "¿Qué aprendemos?":** Textos explicativos que resumen las conclusiones clave del fenómeno.

## Tecnologías Utilizadas

* Python
* Streamlit
* Plotly y Matplotlib
* NumPy

## Cómo Ejecutar la Aplicación Localmente

Para correr esta aplicación en tu propia máquina, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/julianafer0804-ui/relacion-sv-celulas.git](https://github.com/julianafer0804-ui/relacion-sv-celulas.git)
    cd relacion-sv-celulas
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt

4.  **Ejecuta la aplicación:**
    ```bash
    streamlit run app.py
    ```
```eof
