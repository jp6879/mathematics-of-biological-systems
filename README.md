# Mathematics of Biological Systems
### Instituto Balseiro — Maestría en Física

> **Course on Mathematical Tools for Biological Systems** — a graduate-level course from one of Latin America's most prestigious research institutes, covering the mathematical foundations used to model, analyze, and understand complex biological systems.

---

## About This Course

This repository contains all of my coursework for **Matemática de los Sistemas Biológicos** (Mathematics of Biological Systems), a graduate-level course at the [Instituto Balseiro](https://www.ib.edu.ar/), Bariloche, Argentina.

The course explores how mathematical and computational tools — from nonlinear dynamics to stochastic processes and evolutionary game theory — can be applied to understand the behavior of biological systems at multiple scales, from gene regulatory networks to ecological populations.

---

## Repository Structure

```
Matematica de los sistemas biológicos/
│
├── 📚 Notas de clase/          # Lecture notes and professor slides
├── 📖 Bibliografia/            # Core reference textbooks
├── 📝 Trabajos prácticos/      # Working guides (HTML-based problem sets)
│
├── 🧪 Practica_1/              # Deterministic Dynamical Systems
├── 🧪 Practica_2/              # Stochastic Processes & Noise
├── 🧪 Practica_3/              # Gene Regulatory Networks
├── 🧪 Practica_4/              # Stochastic Population Dynamics
└── 🧪 Practica_5/              # Evolutionary Game Theory
```

---

## Practical Works Summary

### Práctica 1 — Deterministic Dynamical Systems

**Assignment:** [`2024-tp01.pdf`](Practica_1/2024-tp01.pdf) | **Report:** [`Morales_Practica1.pdf`](Practica_1/Practico/Morales_Practica1.pdf)

Analysis of nonlinear ordinary differential equations (ODEs) and their qualitative behavior. Tools include phase-plane analysis, fixed-point stability, bifurcation diagrams, and numerical integration.

| Exercise | Description |
|----------|-------------|
| Ej. 1 | Phase portrait & fixed-point analysis |
| Ej. 2 | Numerical ODE integration and bifurcation analysis |
| Ej. 4 | Limit cycles and oscillatory behavior |
| Ej. 5 | Nonlinear system exploration (Jupyter Notebook) |
| Ej. 6 | Additional stability analysis |

**Key concepts:** Fixed points, stability, limit cycles, phase plane, bifurcations, Jacobian analysis.

**Tools:** Python, NumPy, SciPy, Matplotlib, Jupyter Notebooks, LaTeX report.

---

### Práctica 2 — Stochastic Processes & Noise in Biological Systems

**Assignment:** [`2024-tp02.pdf`](Practica_2/2024-tp02.pdf)

Study of stochastic differential equations and their role in modeling biological fluctuations. Covers the Langevin equation, Fokker-Planck formalism, and numerical simulation of stochastic dynamics.

| Exercise | Description |
|----------|-------------|
| Ej. 1 | Probability evolution: Master Equation & simulations |
| Ej. 2 | Langevin equations: additive and multiplicative noise |
| Ej. 3 | Fokker-Planck stationary distributions; extinction phenomena |

**Key concepts:** Langevin equation, Fokker-Planck equation, Master Equation, Itô vs. Stratonovich, stationary distributions, noise-induced transitions, extinction.

**Tools:** Python, Jupyter Notebooks, stochastic simulation libraries, LaTeX report.

---

### Práctica 3 — Gene Regulatory Networks

**Assignment:** [`2024-tp03.pdf`](Practica_3/2024-tp03.pdf) | **Report:** [`Morales_Practica3.pdf`](Practica_3/Informe/Morales_Practica3.pdf)

Mathematical modelling of genetic circuits and regulatory networks. Key focus on the Goodwin oscillator (a core model of circadian rhythms) and Boolean models of gene regulation.

| Exercise | Description |
|----------|-------------|
| Ej. 1 | Goodwin oscillator: parameter analysis and oscillation diagrams |
| Ej. 2 | Genetic toggle switches: bistability and phase portraits |

**Key concepts:** Goodwin oscillator, genetic oscillators, bistability, toggle switch, nullcline analysis, Boolean gene networks, Kauffman networks.

**Outputs include:**
- Goodwin oscillator phase diagrams at multiple parameter values
- Bistable switch analysis with phase portraits

**Tools:** Python, Jupyter Notebooks, SciPy ODE integration, LaTeX report.

---

### Práctica 4 — Stochastic Population Dynamics

**Assignment:** [`2024-tp04.pdf`](Practica_4/2024-tp04.pdf) | **Report:** [`Morales_Practico4.pdf`](Practica_4/informe/Morales_Practico4.pdf)

Application of stochastic methods to population dynamics and ecological models. Analysis of extinction, noise-driven transitions, and complex interaction networks.

| Exercise | Description |
|----------|-------------|
| Ej. 2 | Stochastic population network analysis; Simplex dynamics |

**Key concepts:** Stochastic ecology, population networks, random graphs, Gillespie algorithm, demographic noise, Simplex plots.

**Outputs include:**
- Network visualizations (Simplex diagrams)
- Stochastic trajectory analysis

**Tools:** Python, NetworkX, Jupyter Notebooks, LaTeX report.

---

### Práctica 5 — Evolutionary Game Theory

**Assignment:** [`2024-tp05.pdf`](Practica_5/2024-tp05.pdf) | **Report:** [`Morales_Practica5.pdf`](Practica_5/Morales_Practica5.pdf)

Evolutionary game theory applied to biological populations. Study of the replicator dynamics equation, evolutionary stable strategies (ESS), SIRS epidemic models, and bifurcation phenomena in strategic interactions.

| Exercise | Description |
|----------|-------------|
| Ej. 1 | SIRS epidemic model: stochastic simulations |
| Ej. 2 | Replicator dynamics and nullcline analysis; bifurcations |
| Ej. 3 | Multi-strategy evolutionary dynamics; phase space |

**Key concepts:** Replicator equation, evolutionary stable strategies (ESS), SIRS model, stochastic epidemics, Nash equilibria, Simplex dynamics, bifurcation theory.

**Outputs include:**
- Phase-space trajectories in simplex
- Bifurcation diagrams for evolutionary dynamics
- SIRS stochastic simulations

**Tools:** Python, Jupyter Notebooks, SciPy, Matplotlib, LaTeX report.

---

## Lecture Topics Covered

Based on the course lecture notes and slides, the following topics were addressed throughout the semester:

| Topic | Description |
|-------|-------------|
| Monito del Monte | Population dynamics of a real biological species (case study) |
| Megafauna Extinction | Mathematical modeling of prehistoric extinction events |
| Epidemics | Epidemic waves, stochastic epidemics, and complex networks |
| Pattern Formation | Turing instability and morphogenetic pattern formation |
| Evolutionary Games | Game theory applied to biological populations |
| Boolean Gene Regulation | Boolean models of genetic regulatory networks (Kauffman networks) |

---

## Bibliography

Core reference texts used throughout the course:

| Author | Title |
|--------|-------|
| J. D. Murray | *Mathematical Biology I: An Introduction* (3rd ed., Springer, 2002) |
| J. D. Murray | *Mathematical Biology II: Spatial Models and Biomedical Applications* (3rd ed., Springer, 2003) |
| W. Horsthemke & R. Lefever | *Noise-Induced Transitions: Theory and Applications in Physics, Chemistry, and Biology* |
| N. G. Van Kampen | *Stochastic Processes in Physics and Chemistry* |
| Hofbauer & Sigmund | *Evolutionary Games and Population Dynamics* |
| McKane et al. | Papers on stochastic models and population dynamics |

---

## Technologies Used

| Category | Tools |
|----------|-------|
| **Languages** | Python 3, LaTeX |
| **Scientific Computing** | NumPy, SciPy, SymPy |
| **Visualization** | Matplotlib |
| **Notebooks** | Jupyter Notebook |
| **Graph Analysis** | NetworkX |
| **Typesetting** | LaTeX (with custom `.sty` style files) |

---

## Author

**Juan Pablo Morales**

---

## About Instituto Balseiro

The [Instituto Balseiro](https://www.ib.edu.ar/) (IB) is a graduate research and teaching institution located in Bariloche, Argentina, associated with the Universidad Nacional de Cuyo and CONICET. It is widely regarded as one of the most selective and prestigious physics and engineering institutes in Latin America, with a rigorous admission process and a strong emphasis on research and analytical thinking.

---

*Course: Matemática de los Sistemas Biológicos — Instituto Balseiro, 2024*
