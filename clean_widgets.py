import json, sys, pathlib

nb_path = r"AST1_CEIA_UBA_TP2.ipynb"  # cambia si el nombre/ruta difiere

p = pathlib.Path(nb_path)
nb = json.loads(p.read_text(encoding="utf-8"))

# Elimina metadata.widgets si existe o si le falta 'state'
widgets = nb.get("metadata", {}).get("widgets")
if widgets is not None:
    # Si no hay 'state', o por prolijidad, lo borramos
    nb["metadata"].pop("widgets", None)

# (Opcional) normaliza metadatos vacíos en celdas
for cell in nb.get("cells", []):
    cell.setdefault("metadata", {})

p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("Listo. Volvé a subir/commitear el notebook.")