# Pruebas de Colab para 11-grown-ups.tex (no hay programas de dibujo en este capítulo)

# %% Función de ayuda para el sonido (Para los adultos: Sonido en Colab)
import numpy as np
from IPython.display import Audio, display

def pitido(frec=440, segs=0.5):
    tiempos = np.linspace(0, segs, int(22050 * segs))
    sonido = np.sin(2 * np.pi * frec * tiempos)
    display(Audio(sonido, rate=22050, autoplay=True))

pitido(262)

# %% Asomarse dentro de un .sb3 (necesita un archivo subido llamado mi-proyecto.sb3)
import zipfile, json

with zipfile.ZipFile("mi-proyecto.sb3") as z:
    proyecto = json.loads(z.read("project.json"))

for objeto in proyecto["targets"]:
    print("Objeto:", objeto["name"])
    for bloque in objeto["blocks"].values():
        if isinstance(bloque, dict):
            print("   ", bloque["opcode"])
