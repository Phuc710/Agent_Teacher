#!/usr/bin/env python3
"""
Cross-platform packager for AgentTeacher skill archive.
Packages files tracked by git, filtering out QA and distribution artifacts.
"""

import os
import subprocess
import sys
import zipfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist", "agent-teacher.zip")
PACKAGE_MAX_BYTES = int(os.environ.get("TEACHER_PACKAGE_MAX_BYTES", 500000))
REQUIRED_ENTRY = "SKILL.md"

EXCLUDE_PREFIXES = ("evals/", "dist/", ".claude-plugin/")
EXCLUDE_SUBSTRINGS = ("__pycache__/", ".pyc", ".DS_Store")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if os.path.exists(OUT):
        os.remove(OUT)

    res = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    files = res.stdout.strip().splitlines()

    filtered = []
    for f in files:
        norm = f.replace("\\", "/")
        if any(norm.startswith(p) for p in EXCLUDE_PREFIXES):
            continue
        if any(s in norm for s in EXCLUDE_SUBSTRINGS):
            continue
        filtered.append(f)

    if not filtered:
        print("ERROR: no files to package. Did you forget to 'git add'?", file=sys.stderr)
        sys.exit(1)

    if REQUIRED_ENTRY not in filtered:
        print(f"ERROR: required package entry missing from files: {REQUIRED_ENTRY}", file=sys.stderr)
        sys.exit(1)

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in filtered:
            abs_path = os.path.join(ROOT, f)
            if os.path.exists(abs_path):
                zf.write(abs_path, arcname=f)

    size_bytes = os.path.getsize(OUT)
    if size_bytes > PACKAGE_MAX_BYTES:
        print(f"ERROR: package exceeds {PACKAGE_MAX_BYTES} bytes: {size_bytes} bytes", file=sys.stderr)
        sys.exit(1)

    print(f"OK: package audit passed ({size_bytes} bytes, limit {PACKAGE_MAX_BYTES})")
    print(f"OK: wrote {OUT}")


if __name__ == "__main__":
    main()
