from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone

# Show BOTH:
# - docs/ (Master Framework)
# - notebooks/01_framework/
ROOTS = [
    Path("docs"),
    Path("notebooks/01_framework"),
]

EXCLUDE_DIRS = {
    ".git", "__pycache__", ".ipynb_checkpoints", "aion_env", "venv", ".venv", "logs"
}

MAX_DEPTH = 12  # adjust later if needed

def iter_children(p: Path):
    try:
        kids = list(p.iterdir())
    except Exception:
        return []
    # dirs first, then files, alphabetical
    kids.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    return [k for k in kids if k.name not in EXCLUDE_DIRS]

def tree_lines(root: Path, prefix: str = "", depth: int = 0):
    lines = []
    if depth > MAX_DEPTH:
        return lines

    children = iter_children(root)
    for i, child in enumerate(children):
        is_last = (i == len(children) - 1)
        branch = "└── " if is_last else "├── "
        lines.append(f"{prefix}{branch}{child.name}{'/' if child.is_dir() else ''}")

        if child.is_dir():
            ext = "    " if is_last else "│   "
            lines.extend(tree_lines(child, prefix + ext, depth + 1))
    return lines

def main():
    out = []
    out.append(f"# Master Directory Tree (generated UTC {datetime.now(timezone.utc).isoformat(timespec='seconds')})")
    out.append("")
    for r in ROOTS:
        if r.exists():
            out.append(f"{r.as_posix()}/")
            out.extend(tree_lines(r))
            out.append("")
        else:
            out.append(f"{r.as_posix()}/  (missing)")
            out.append("")

    Path("data").mkdir(parents=True, exist_ok=True)
    out_path = Path("data/master_directory_tree.txt")
    out_path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out_path.resolve()}")

if __name__ == "__main__":
    main()
