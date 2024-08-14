from argparse import ArgumentParser
from pathlib import Path
import matplotlib.pyplot as plt
from . import parse

plt.rcParams.update({
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "font.size": 28,
})

plot_parser = ArgumentParser("sylabutil")
plot_parser.add_argument("infile", metavar="I", type=Path, nargs="+")
plot_parser.add_argument("--outfile", metavar="O", type=Path)
def plot():
    args = plot_parser.parse_args()
    infiles = args.infile
    outfile = args.outfile or Path.cwd() / "output.pdf"

    fig, ax = plt.subplots(figsize=(12, 8))
    for infile in infiles:
        filedata = parse(infile)
        block = filedata["block"]
        times = block["1"]["Time[ns]"]
        values = block["1"]["No_of_photons"]
        ax.plot(times, values, label=infile.name)
        ax.set_yscale("log")
    ax.set_xlabel("Time[ns]")
    ax.set_ylabel("No_of_photons")
    ax.legend()
    fig.tight_layout()
    fig.savefig(outfile, transparent=True)
