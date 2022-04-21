from argparse import ArgumentParser
import glob
import PyPDF4

argparser = ArgumentParser(description='Merge some PDF files.')
argparser.add_argument('-f', '--files', type=str, nargs='+',
                        default='*.pdf',
                        help='Specify filenames of input')
argparser.add_argument('-o', '--out', type=str,
                        default='out.pdf',
                        help='Specify filename of output')
args = argparser.parse_args()

pdfs = glob.glob("*.pdf")
merger = PyPDF4.PdfFileMerger()

for p in pdfs:
    merger.append(p)

merger.write("out.pdf")
merger.close()