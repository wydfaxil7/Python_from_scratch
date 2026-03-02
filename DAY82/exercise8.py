### MERGING A PDF

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ['sample.pdf', 'sample1.pdf', 'sample2.pdf']:
    merger.append(pdf)

merger.write('merged.pdf')
merger.close()