import os
from PyPDF2 import PdfReader

base = "BIBLIOGRAFIA-ANTROPO/bibliografía"
files = {
    "UNIDAD_II/Boivin CAP1.pdf": "c4_boivin_cap1",
    "UNIDAD_III/boivin CAP 2.pdf": "c5_boivin_cap2",
    "UNIDAD_III/HERNANDEZ MARTINEZ -Lischetti.pdf": "c5_hernandez_particularismo",
    "UNIDAD_III/Materiales para trabajar en clases/BOHANNAN- boivin.pdf": "c5_bohannan",
}
os.makedirs("extracted", exist_ok=True)
for rel, name in files.items():
    path = os.path.join(base, rel)
    try:
        r = PdfReader(path)
        txt = "\n\n=== PAGE BREAK ===\n\n".join((pg.extract_text() or "") for pg in r.pages)
        with open(os.path.join("extracted", name + ".txt"), "w", encoding="utf-8") as f:
            f.write(txt)
        print("OK", name, len(txt))
    except Exception as e:
        print("ERR", name, str(e)[:120])