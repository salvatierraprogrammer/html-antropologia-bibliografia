import os
from PyPDF2 import PdfReader

base = "BIBLIOGRAFIA-ANTROPO/bibliografía"
files = {
    "UNIDAD_I/boivin-rosato- arribas INTROD..pdf": "c1_boivin_intro",
    "UNIDAD_I/Quiros-Para_que_sirve_unx_antropologx.pdf": "c1_quiros",
    "UNIDAD_I/lamas marta-CORTO.pdf": "c2_lamas",
    "UNIDAD_I/Desnaturalizar- pita, martinez.pdf": "c2_pita",
    "UNIDAD_II/bellelli.pdf": "c3_bellelli",
    "UNIDAD_II/CHIRIGUNI - NATURALEZA_1.pdf": "c3_chiriguini",
}
os.makedirs("extracted", exist_ok=True)
for rel, name in files.items():
    p = os.path.join(base, rel)
    p2 = None
    # some names may not match exactly; glob fallback
    if not os.path.exists(p):
        import glob
        cands = glob.glob(os.path.join(base, os.path.dirname(rel), "*.pdf"))
        for c in cands:
            if name.split("_",1)[1].split("_")[0].lower().replace(" ","") in os.path.basename(c).lower():
                p2 = c
    path = p2 or p
    try:
        r = PdfReader(path)
        txt = "\n\n=== PAGE BREAK ===\n\n".join((pg.extract_text() or "") for pg in r.pages)
        with open(os.path.join("extracted", name + ".txt"), "w", encoding="utf-8") as f:
            f.write(txt)
        print("OK", name, len(txt))
    except Exception as e:
        print("ERR", name, str(e)[:120])