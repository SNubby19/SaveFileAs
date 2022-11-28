import docx2pdf as d2p
import os

dir_scan = list(os.scandir())

ftc = ""

for entry in dir_scan:
    ftc = entry.path

    if (os.path.getmtime(entry.path) <= os.path.getmtime(ftc)) and (entry.path[-4:] == "docx"):
        ftc = entry.path

ftc = os.path.basename(ftc)
sfa = ftc[:-4] + "pdf"

opath = "C:\\Users\\USER\\Documents\\PDF Saves\\" + sfa

d2p.convert(ftc, opath)
