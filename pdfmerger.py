from argparse import ArgumentParser
import PyPDF4

argparser = ArgumentParser(description='Merge some PDF files.')
argparser.add_argument('pdfs', type=str, nargs='+',
                        default='*.pdf',
                        help='Specify filenames of input')
argparser.add_argument('-o', '--out', type=str,
                        default='out.pdf',
                        dest='out_name',
                        help='Specify filename of output')
args = argparser.parse_args()

merger = PyPDF4.PdfFileMerger()

for p in args.pdfs:
    merger.append(p)

merger.write(args.out_name)
merger.close()