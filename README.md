# Practica N.° 09 — Árboles Binarios de Búsqueda (BST)

**SIS210 — Algoritmos y Estructuras de Datos**  
**Universidad Nacional del Altiplano — Puno**  

| | |
|---|---|
| **Estudiante** | APAZA SORITJA MICHAEL ANTHONY |
| **Docente** | Dr. Aldo Hernan Zanabria Galvez |
| **Semestre** | 2025 |

---

## Estructura del repositorio

```
Practica09_BST/
├── python/
│   ├── actividad1.py          # Búsqueda iterativa y recursiva
│   ├── actividad2.py          # Inserción en BST
│   ├── actividad3.py          # Eliminación (3 casos)
│   ├── actividad4.py          # Recorridos (in-order, pre-order, post-order)
│   ├── actividad5.py          # BFS (recorrido por niveles)
│   ├── actividad6.py          # Altura y tamaño del árbol
│   ├── actividad7.py          # Validación de invariante BST
│   └── bst_completo.py        # Implementación completa + pruebas
├── cpp/
│   ├── ArbolAcademico.hpp     # Clase template BST (C++17)
│   ├── main.cpp               # Demo de operaciones
│   ├── benchmark.cpp          # Benchmarks vs lista y diccionario
│   └── Makefile               # Compilación
├── aprendizaje/
│   ├── index.html             # Visualizador interactivo BST
│   ├── style.css              # Estilos del visualizador
│   ├── bst_core.js            # Lógica del BST (JavaScript)
│   ├── bst_renderer.js        # Renderizado SVG
│   ├── bst_animator.js        # Animación paso a paso
│   └── bst_code_panel.js      # Panel de código
├── latex/
│   ├── trabajo_investigacion.tex
│   ├── Logo_UNAP.png
│   └── compile.sh
└── README.md
```

---

## Python

```bash
cd python
python bst_completo.py
```

Ejecuta las 7 actividades con pruebas automáticas y un print visual del árbol.

Requisitos: Python 3.11+ (solo usa la biblioteca estándar).

---

## C++

```bash
cd cpp
make            # compila todo
make run_main   # ejecuta demo de operaciones
make run_benchmark  # ejecuta benchmarks
```

Requiere `g++` con soporte C++17. No depende de librerías externas.

---

## Visualizador interactivo

```bash
cd aprendizaje
python3 -m http.server 8080
# Abrir en navegador: http://localhost:8080
```

El visualizador permite:

- **Insertar**, **buscar** y **eliminar** nodos con animación paso a paso
- **Recorridos**: In-Order, Pre-Order, Post-Order y BFS
- Resaltado de línea de código en ejecución
- Carga de ejemplos predefinidos (árbol balanceado, degenerado, aleatorio)
- Panel informativo con invariante BST, complejidades Big-O y casos de eliminación

---

## LaTeX

```bash
cd latex
bash compile.sh
```

Genera `trabajo_investigacion.pdf` con carátula institucional y 4 páginas de contenido.

Requiere `pdflatex`, `biblatex` y `biber`.

---

## Operaciones BST

| Operación | Mejor caso | Promedio | Peor caso |
|-----------|-----------|----------|-----------|
| Insertar  | O(1)      | O(log n) | O(n)      |
| Buscar    | O(1)      | O(log n) | O(n)      |
| Eliminar  | O(1)      | O(log n) | O(n)      |
| Recorridos| O(n)      | O(n)     | O(n)      |

Donde *n* es el número de nodos y *h* la altura del árbol.
