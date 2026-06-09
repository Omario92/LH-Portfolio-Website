from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
frontend_dir = root / "front-end"
missing = []
for html_file in frontend_dir.glob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    refs = re.findall(r"(?:href|src)=['\"]([^'\"]+)['\"]", text)
    for ref in refs:
        if ref.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean_ref = ref.split("?")[0].split("#")[0]
        if not clean_ref:
            continue
        path = frontend_dir / clean_ref
        if not path.exists():
            missing.append((html_file.name, ref))

if missing:
    print("Missing references:")
    for f, ref in missing:
        print(f"- {f}: {ref}")
    sys.exit(1)

print("OK: no missing local href/src references.")
