import glob
import os
import PyPDF4

pdfs = glob.glob("*.pdf")
merger = PyPDF4.PdfFileMerger()

for p in pdfs:
    merger.append(p)

merger.write("out.pdf")
merger.close()