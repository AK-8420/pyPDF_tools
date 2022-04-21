from argparse import ArgumentParser
import glob
import PyPDF4

argparser = ArgumentParser(description='Merge some PDF files.')
argparser.add_argument('-f', '--files', type=str, nargs='+',
                        default='*.pdf',
                        dest='pdfs',
                        help='Specify filenames of input')
argparser.add_argument('-o', '--out', type=str,
                        default='out.pdf',
                        dest='out_name',
                        help='Specify filename of output')
args = argparser.parse_args()

#pdfs = glob.glob("*.pdf")
merger = PyPDF4.PdfFileMerger()

for p in args.pdfs:
    merger.append(p)

merger.write(args.out_name)
merger.close()