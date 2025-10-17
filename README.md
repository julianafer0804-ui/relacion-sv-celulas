Visualizador Interactivo de la Relación Superficie-Volumen Celular

Esta es una aplicación interactiva construida con Streamlit para explorar y visualizar la relación fundamental entre la superficie y el volumen de una esfera, un concepto clave en la biología celular.

(Sube una de tus capturas de pantalla a un sitio como Imgur y pega el enlace aquí para que sea lo primero que la gente vea).

Descripción del Problema

La relación superficie-volumen es un principio fundamental que explica por qué las células son microscópicas. A medida que una célula (o cualquier objeto esférico) aumenta de tamaño, su volumen crece mucho más rápido que su área de superficie. Esto limita el tamaño celular, ya que la membrana plasmática (superficie) debe ser lo suficientemente grande para servir a todo el citoplasma (volumen).

Esta aplicación permite a los usuarios manipular el radio de una esfera y observar de forma instantánea cómo cambian su superficie, volumen y, lo más importante, la relación entre ambos.

Características

Slider Interactivo: Modifica el radio de la esfera en tiempo real.

Visualización 3D: Un gráfico interactivo de Plotly muestra la esfera cambiando de tamaño.

Gráfico 2D: Una gráfica muestra cómo decae la relación S/V a medida que aumenta el radio de la célula.

Cálculos en Vivo: La superficie, el volumen y la relación S/V se actualizan automáticamente.

Sección "¿Qué aprendemos?": Textos explicativos dentro de la app que resumen las conclusiones clave del fenómeno.

Tecnologías Utilizadas

Python

Streamlit (para la interfaz web)

Plotly y Matplotlib (para las visualizaciones)

NumPy (para los cálculos matemáticos)

Cómo Ejecutar la Aplicación Localmente

Para correr esta aplicación en tu propia máquina, sigue estos pasos:

Clona el repositorio:

git clone [https://github.com/julianafer0804-ui/relacion-sv-celulas.git](https://github.com/julianafer0804-ui/relacion-sv-celulas.git)
cd relacion-sv-celulas


Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`


Instala las dependencias:

pip install -r requirements.txt


Ejecuta la aplicación:

streamlit run app.py
