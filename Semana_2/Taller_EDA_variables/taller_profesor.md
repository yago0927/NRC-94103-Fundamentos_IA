# Taller — Análisis exploratorio de variables categóricas y numéricas
### Versión PROFESOR (soluciones y guía de facilitación)
### Dataset: `StudentsPerformance.csv`

**Notas generales para el profesor:**
- Tiempo sugerido: 45-60 min (10 min Parte 1, 20 min Parte 2, 15-20 min Parte 3 + cierre).
- Antes de empezar, confirma que todos tengan `StudentsPerformance.csv` en la misma carpeta que su notebook — es el error más común (`FileNotFoundError`).
- La idea pedagógica central del taller: **frecuencias/porcentajes para categóricas**, **describe/histogramas para numéricas**, y conectar ambas con la noción de **distribución (forma de campana)**.

---

## Paso 0 — Preparación

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")
df.head()
```

---

## Parte 1 — Variables categóricas

### Ejercicio 1.1 — Solución
```python
print(df["gender"].value_counts())
print()
print(df["gender"].value_counts(normalize=True) * 100)
```

### Ejercicio 1.2 — Solución
```python
print(df["test preparation course"].value_counts())
print()
print(df["test preparation course"].value_counts(normalize=True) * 100)
```

**Respuesta esperada — Pregunta de reflexión 1:**
`gender` suele estar razonablemente balanceado (~48%/52%). `test preparation course` normalmente NO está balanceado (más estudiantes en `"none"` que en `"completed"`). Esto importa porque un grupo muy pequeño (por ejemplo, pocos "completed") da comparaciones menos confiables/representativas al analizar diferencias de desempeño entre grupos.

*Punto de discusión en clase:* preguntar "¿qué pasaría si quisiéramos comparar el promedio de notas entre quienes completaron el curso y quienes no, pero un grupo tiene 900 estudiantes y el otro 100?" — conecta con la idea de tamaño de muestra.

### Ejercicio 1.3 — Solución
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

df["gender"].value_counts().plot(kind="bar", ax=axes[0], title="Gender")
df["test preparation course"].value_counts().plot(kind="bar", ax=axes[1], title="Test preparation course")

plt.tight_layout()
plt.show()
```

*Error común:* olvidar `ax=axes[i]`, lo que genera dos figuras separadas en vez de un panel de dos gráficos.

---

## Parte 2 — Variables numéricas

### Ejercicio 2.1 — Solución
```python
df["math score"].describe()
```

**Respuesta esperada — Pregunta de reflexión 2:**
`mean` y `50%` (mediana) suelen ser muy parecidos (~66). Esto sugiere una distribución aproximadamente **simétrica**, sin sesgo fuerte hacia valores muy altos o muy bajos.

### Ejercicio 2.2 — Solución
```python
df[["math score", "reading score", "writing score"]].hist(figsize=(10, 4), bins=15)
plt.tight_layout()
plt.show()
```

**Respuesta esperada — Pregunta de reflexión 3:**
Sí, las tres variables muestran una forma aproximada de campana (normal): pocas barras en los extremos, pico en el centro (alrededor de 60-75), y caída simétrica hacia ambos lados. Ninguna de las tres suele mostrar una asimetría marcada, aunque `math score` a veces muestra una cola ligeramente más marcada hacia valores bajos (algunos estudiantes con notas muy bajas, cercanas a 0).

*Sugerencia de facilitación:* mostrar el diagrama de campana visto en la sesión anterior y pedir a los estudiantes que señalen en su propio histograma dónde estaría "la media/mediana" y dónde las "colas".

### Ejercicio 2.3 — Solución
```python
df.describe()
```

**Respuesta esperada — Pregunta de reflexión 4:**
Generalmente `math score` tiene la mayor dispersión (`std` más alto) y también suele tener el rango más amplio (mínimo más bajo, a veces 0). `reading score` y `writing score` tienden a estar más concentradas entre sí. Los valores exactos dependen de la versión del CSV, por lo que se recomienda verificar con la salida real antes de la clase.

---

## Parte 3 — Reto integrador (opcional) — Solución de referencia

```python
df.groupby("lunch")["math score"].mean()
```

o alternativamente:

```python
df.groupby("parental level of education")["math score"].mean().sort_values(ascending=False)
```

**Respuesta esperada — Pregunta de cierre:**
Suele observarse que el grupo con `lunch = "standard"` tiene un promedio más alto en `math score` que el grupo con `"free/reduced"`. Es una buena oportunidad para introducir la diferencia entre **correlación y causalidad**: el dataset no permite concluir que el tipo de almuerzo *cause* el resultado — puede reflejar factores socioeconómicos subyacentes no capturados directamente en esta variable.

*Cierre sugerido de la sesión:* recalcar que este taller cubre el análisis **descriptivo** (qué pasó, cómo se distribuyen los datos) — no predictivo ni causal — y que ese es el paso previo indispensable antes de cualquier modelo.

---

## Rúbrica rápida de participación (sugerida)

| Criterio | Logrado |
|---|---|
| Calcula frecuencias y porcentajes correctamente para 2 variables categóricas | ☐ |
| Interpreta correctamente el balance/desbalance de categorías | ☐ |
| Obtiene `describe()` e interpreta media vs. mediana | ☐ |
| Genera histogramas y reconoce (o descarta) la forma de campana | ☐ |
| Completa el reto integrador con `groupby` y propone una hipótesis razonable | ☐ |
