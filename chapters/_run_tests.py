"""Run every piece of one or more NN-colab-tests.py files against the real ColabTurtlePlus library.

Usage:
    <venv>/bin/python -I _run_tests.py 03-colab-tests.py [more files...]

The pieces of one file ("# %% name") run in order in one process and share variables, like cells
in one Colab notebook. Colab's display is replaced by a stand-in and time.sleep is skipped.
Pieces marked "# needs typing: p. ej. Ana, 7" (or "e.g.") get those answers typed in turn.
Pieces whose name says "broken on purpose" / "roto a propósito" must raise an error.
Pieces with "while True" or file reading are skipped.
"""
import re, sys, subprocess, pathlib, json, tempfile

RUNNER = r'''
import sys, time, builtins, itertools, json, traceback, IPython.display as d
class _H:
    def update(self, *a, **k): pass
d.display = lambda *a, **k: _H()
time.sleep = lambda s: None
from IPython.display import Audio  # noqa: keep import working
class _Stop(Exception): pass
P = json.load(open(sys.argv[1], encoding="utf-8"))
ns = {"__name__": "__main__"}
tot = {"PASS": 0, "FAIL": 0, "SKIP": 0}
for p in P:
    tag = p["file"] + " | " + p["name"][:62]
    if p["skip"]:
        tot["SKIP"] += 1; print("SKIP", tag, "|", p["skip"]); continue
    ans = itertools.cycle(p["answers"] or ["5", "si", "izquierda", "3"])
    n = [0]
    def _inp(prompt=""):
        n[0] += 1
        if n[0] > 40: raise _Stop()
        a = next(ans); print(str(prompt) + a); return a
    builtins.input = _inp
    import io, contextlib
    buf = io.StringIO()
    err = None
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(p["code"], tag, "exec"), ns)
    except _Stop:
        pass
    except Exception as e:
        err = f"{type(e).__name__}: {e}"
    out = buf.getvalue().replace("Put clearscreen() as the first line in a cell (after the import command) to re-run turtle commands in the cell\n", "").strip().replace("\n", " / ")[:90]
    if p["broken"]:
        ok = err is not None
        msg = ("expected error: " + err) if ok else "NO ERROR, but this piece should be broken"
    else:
        ok = err is None
        msg = out if ok else err
    tot["PASS" if ok else "FAIL"] += 1
    print("PASS" if ok else "FAIL", tag, "|", msg)
print("TOTAL", tot)
sys.exit(1 if tot["FAIL"] else 0)
'''

def pieces(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    chunks = re.split(r"^# %%[ \t]*(.*)$", text, flags=re.M)
    for name, code in zip(chunks[1::2], chunks[2::2]):
        m = re.search(r"needs typing:\s*(.*)|escribe:\s*(.*)", code, re.I)
        answers = []
        if m:
            t = m.group(1) or m.group(2)
            eg = re.search(r"(?:e\.g\.|p\. ?ej\.|ej\.)\s*([^)]*)", t)
            src = eg.group(1) if eg else re.split(r"\(|\+", t)[0]
            answers = [a.strip() for a in re.split(r",|\bor\b|\bo\b", src) if a.strip()]
        skip = None
        if "while True" in code: skip = "while True (stop button by design)"
        if "zipfile" in code or "open(" in code: skip = "reads a local file"
        broken = bool(re.search(r"broken on purpose|roto a prop[oó]sito", name, re.I) and re.search(r"expect|espera", name, re.I))
        yield {"file": pathlib.Path(path).name[:2], "name": name.strip(), "code": code,
               "answers": answers, "skip": skip, "broken": broken}

def main():
    tmp = pathlib.Path(tempfile.mkdtemp())
    runner = tmp / "runner.py"; runner.write_text(RUNNER, encoding="utf-8")
    bad = 0
    for f in sys.argv[1:]:
        data = tmp / "pieces.json"
        data.write_text(json.dumps(list(pieces(f))), encoding="utf-8")
        r = subprocess.run([sys.executable, "-I", str(runner), str(data)], capture_output=True,
                           text=True, timeout=600, cwd=tmp)
        print(r.stdout, end="")
        if r.returncode:
            bad += 1
            if r.stderr.strip(): print(r.stderr.strip().splitlines()[-1])
    sys.exit(1 if bad else 0)

main()
