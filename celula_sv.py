import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # pantalla ancha

# Título
st.title("📏 Relación Superficie/Volumen en Células (Esfera)")

# Slider para el radio
radio = st.slider("Selecciona el radio de la célula (µm)", 1, 20, 5)

# Cálculos
superficie = 4 * np.pi * radio**2
volumen = (4/3) * np.pi * radio**3
rel_sv = superficie / volumen

# Dividir en columnas
col1, col2 = st.columns([2, 1])

# Columna izquierda → esfera
with col1:
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111, projection='3d')

    # coordenadas de la esfera
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radio * np.outer(np.cos(u), np.sin(v))
    y = radio * np.outer(np.sin(u), np.sin(v))
    z = radio * np.outer(np.ones(np.size(u)), np.cos(v))

    # graficar esfera
    ax.plot_surface(x, y, z, color='skyblue', alpha=0.8, edgecolor='gray')
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([-20, 20])
    ax.set_title("Célula como esfera", fontsize=12)

    st.pyplot(fig)

# Columna derecha → resultados numéricos
with col2:
    st.subheader("📊 Resultados")
    st.metric("Superficie (µm²)", f"{superficie:.1f}")
    st.metric("Volumen (µm³)", f"{volumen:.1f}")
    st.metric("Relación S/V (µm⁻¹)", f"{rel_sv:.2f}")

# Gráfico 2D para ver la tendencia
st.subheader("📉 Cómo cambia la relación S/V con el tamaño celular")
radios = np.arange(1, 21, 1)
relaciones = (4 * np.pi * radios**2) / ((4/3) * np.pi * radios**3)

fig2, ax2 = plt.subplots()
ax2.plot(radios, relaciones, marker="o", color="darkblue")
ax2.axvline(radio, color="red", linestyle="--", label=f"Radio actual = {radio} µm")
ax2.set_xlabel("Radio de la célula (µm)")
ax2.set_ylabel("Relación S/V (µm⁻¹)")
ax2.set_title("Relación S/V vs. Radio")
ax2.legend()

st.pyplot(fig2)

# Explicación clara para chicos
st.info("""
🔎 **¿Qué aprendemos?**  
- Cuando el **radio aumenta**, el **volumen crece más rápido** que la superficie.  
- Por eso, la **relación S/V baja** en células más grandes.  
- Esto limita el intercambio de nutrientes y desechos, y explica por qué las células no crecen indefinidamente.
""")

