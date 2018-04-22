import os
from PyPDF2 import PdfFileMerger
os.chdir(r"C:\Users\mikpo\Desktop\Dossier_PhD_2018\Dossier\ ")
path = os.getcwd()
# path = r"C:\Users\mikpo\Desktop\Dossier_PhD_2018\Dossier\ "
lst = os.listdir(r"C:\Users\mikpo\Desktop\Dossier_PhD_2018\Dossier")
pdf_files = sorted(lst)

merger = PdfFileMerger()

for files in pdf_files:
    merger.append(path+"\\"+files)
if not os.path.exists(path+'merged.pdf'):
    merger.write(path + 'merged.pdf ')

merger.close()

# merger.write("Application_Michael_Pons_2018.pdf")
