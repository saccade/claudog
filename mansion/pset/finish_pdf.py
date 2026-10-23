"""After latexmk: clean the PDF's metadata and file it under its title with a timestamp, replacing the old one.
Claude (Anthropic), 2026-10-23, for doc (14:10): the PDF says only its title, author, and subject (set in the .tex);
xdvipdfmx's Producer goes, and the dates are written in local time (xdvipdfmx gets the zone wrong).
Usage: python3 finish_pdf.py   (from mansion/pset, after latexmk -xelatex mansion_pset.tex)"""
import datetime, glob, os, shutil, subprocess
import pikepdf
pdf = pikepdf.open("mansion_pset.pdf", allow_overwriting_input=True)
for k in ("/Producer", "/Creator", "/Keywords", "/Trapped"):
    if k in pdf.docinfo: del pdf.docinfo[k]
now = datetime.datetime.now().astimezone()
off = now.strftime("%z"); stamp = now.strftime("D:%Y%m%d%H%M%S") + f"{off[:3]}'{off[3:]}'"
pdf.docinfo["/CreationDate"] = stamp; pdf.docinfo["/ModDate"] = stamp
pdf.save("mansion_pset.pdf")
for old in glob.glob("The Mansion that did not Spin *.pdf") + glob.glob("Claude Mansion problem set *.pdf"):
    subprocess.run(["git", "rm", "-q", "--ignore-unmatch", old]); os.path.exists(old) and os.remove(old)
name = f"The Mansion that did not Spin {now:%y%m%d%H%M}.pdf"
shutil.copy("mansion_pset.pdf", name); subprocess.run(["git", "add", name]); print(name)
