import os
from PyPDF2 import PdfMerger

folder = 'FolderPath'
pdfs = [f for f in os.listdir(folder) if f.endswith('.pdf')]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(folder + '/' + pdf)

merger.write("merged.pdf")
merger.close()
