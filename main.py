import docx2pdf as d2p
import os

dir_scan = list(os.scandir())

ftc = dir_scan[0].path

for entry in dir_scan:
    if (os.path.getmtime(entry.path) <= os.path.getmtime(ftc)) and (entry.path[-4:] == "docx"):
        ftc = entry.path

ftc = os.path.basename(ftc)
sfa = ftc[:-4] + "pdf"

opath = "C:/Users/YOURUSERNAME/Documents/PDF Saves/" + sfa

d2p.convert(ftc, opath)
