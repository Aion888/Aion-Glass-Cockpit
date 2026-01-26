import json, os
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"

def list_files(base: Path, exts=None):
    out = []
    if not base.exists():
        return out
    for p in sorted(base.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if exts and p.suffix.lower() not in exts:
            continue
        out.append(rel)
    return out

index = {
    "generated_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    "docs": list_files(DOCS, exts={".md"}),
    "data": list_files(DATA, exts={".json", ".csv", ".xlsx"}),
}

out_path = DATA / "project_index.json"
out_path.write_text(json.dumps(index, indent=2), encoding="utf-8")
print(f"Wrote {out_path}")
