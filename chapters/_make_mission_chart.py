"""Construye es/chapters/00-mission-chart.tex a partir de los títulos \\mission{...} de los capítulos 01-08."""
import re, pathlib
root = pathlib.Path(__file__).parent
parts = [("01-motion-pen", "Parte 1: Movimiento y Lápiz"), ("02-loops", "Parte 2: Bucles"),
         ("03-variables-lists", "Parte 3: Variables y listas"), ("04-operators", "Parte 4: Operadores"),
         ("05-sensing-decisions", "Parte 5: Sensores y decisiones"), ("06-functions", "Parte 6: Mis Bloques"),
         ("07-looks-sound-events", "Parte 7: Apariencia, sonido y eventos"), ("08-projects", "Grandes proyectos")]
pat = re.compile(r"^\s*\\mission\{((?:[^{}]|\{[^{}]*\})*)\}", re.M)
rows, n = [], 0
for stem, label in parts:
    f = root / f"{stem}.tex"
    titles = pat.findall(f.read_text(encoding="utf-8")) if f.exists() else []
    rows.append(rf"\multicolumn{{3}}{{l}}{{\rule{{0pt}}{{14pt}}\textbf{{{label}}}}} \\")
    for t in titles:
        n += 1
        rows.append(rf"{n} & {t} & $\star$\ \ $\star$\ \ $\star$ \\")
out = [r"% Generado por chapters/_make_mission_chart.py -- no editar a mano.",
       r"\banner{events}{SIGUE TU PROGRESO}{Mis misiones}",
       r"Colorea una estrella cada vez que termines una misión: una estrella por hacer que funcione, dos por hacer un reto, ¡y tres por hacerlos todos!",
       r"\begin{center}\renewcommand{\arraystretch}{1.12}",
       r"\begin{longtable}{c P{10.5cm} l}", r"\toprule",
       r"\textbf{Misión} & \textbf{Lo que haces} & \textbf{¿Lista?} \\", r"\midrule", r"\endhead",
       *rows, r"\bottomrule", r"\end{longtable}", r"\end{center}"]
(root / "00-mission-chart.tex").write_text("\n".join(out) + "\n", encoding="utf-8")
print(n, "misiones")
