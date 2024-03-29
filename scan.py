from time import sleep
import cv2 as cv
import glob
import fpdf
import os

def img2bin(f_in, f_out):
    img = cv.imread(f_in)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(f_out, img)

pdf = fpdf.FPDF()
pdf.set_auto_page_break(0)
l = sorted(glob.glob(r'.\*.jpg'))

for f in l:
    img2bin(f, f[:-4]+'_out.jpg')
    pdf.add_page()
    pdf.image(f[:-4]+'_out.jpg', w=205, h=297)
    os.remove(f[:-4]+'_out.jpg')

pdf.output(r'.\hw.pdf')   