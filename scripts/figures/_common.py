"""Shared plotting helpers. Every figure is saved as PDF and as 300 dpi PNG."""
import pathlib
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
FIG = ROOT / "results" / "figures"
TAB = ROOT / "results" / "tables"
PROC = ROOT / "data" / "processed"

plt.rcParams.update({
    "figure.dpi": 110, "savefig.bbox": "tight", "font.size": 9,
    "axes.grid": True, "grid.alpha": 0.3, "axes.spines.top": False,
    "axes.spines.right": False, "legend.frameon": False,
})
PALETTE = ["#1f5f8b", "#c1553b", "#4b8f6f", "#8a6bbf", "#c9a227", "#6b6b6b", "#2b7a9b"]


def need(*paths):
    """Missing input check. Figures never invent data."""
    missing = [str(p) for p in paths if not pathlib.Path(p).exists()]
    if missing:
        print("SKIPPED: required input not found:\n  " + "\n  ".join(missing))
        sys.exit(0)
    return True


sys.path.insert(0, str(ROOT / "scripts" / "tables"))
try:                                     # the label map lives with the tables
    from _common import prettify as _prettify
except ImportError:                      # figures still render without it
    def _prettify(s):
        return s


def nice(s, wrap=0):
    """Turn a code identifier into a readable axis or legend label.

    Figure scripts label series and ticks with the identifiers they read from
    the result files, and several of them already split those on the underscore
    to fit, which yields `distribution\\nshift` rather than anything a reader
    would call a label. Both forms are normalised here and sent through the
    same map the tables use, so a figure and a table name the same thing the
    same way. `wrap` re-breaks a long result across two lines for tick labels.
    """
    if not isinstance(s, str):
        return s
    out = _prettify(s.replace("\n", "_").strip())
    if wrap and len(out) > wrap and " " in out:
        words, lines, cur = out.split(" "), [], ""
        for w in words:
            if cur and len(cur) + 1 + len(w) > wrap:
                lines.append(cur)
                cur = w
            else:
                cur = f"{cur} {w}".strip()
        lines.append(cur)
        out = "\n".join(lines)
    return out


def polish_labels(fig, wrap=16):
    """Rewrite every tick label, legend entry and axis label through `nice`."""
    for ax in fig.get_axes():
        for setter, getter in ((ax.set_xlabel, ax.get_xlabel),
                               (ax.set_ylabel, ax.get_ylabel),
                               (ax.set_title, ax.get_title)):
            setter(nice(getter()))
        for axis, w in ((ax.xaxis, wrap), (ax.yaxis, 0)):
            texts = [t.get_text() for t in axis.get_ticklabels()]
            if any("_" in t or "\n" in t for t in texts):
                axis.set_ticklabels([nice(t, wrap=w) for t in texts])
        leg = ax.get_legend()
        if leg is not None:
            for t in leg.get_texts():
                t.set_text(nice(t.get_text()))


def save(fig, name):
    FIG.mkdir(parents=True, exist_ok=True)
    polish_labels(fig)
    fig.savefig(FIG / f"{name}.pdf")
    fig.savefig(FIG / f"{name}.png", dpi=300)
    plt.close(fig)
    print(f"saved results/figures/{name}.pdf and .png")
