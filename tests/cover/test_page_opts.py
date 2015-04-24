# -*- coding: utf-8 -*-

"Test page options (rotate, trim etc)"

#PyFPDF-cover-test:format=PDF
#PyFPDF-cover-test:fn=page_opts.pdf
#PyFPDF-cover-test:hash=d83af8d4fa822f513905fcb288b126f1

import os

import common
from fpdf import FPDF

def page(pdf, text, orientation):
    pdf.write(8, text)
    pdf.ln(8)

@common.add_unittest
def dotest(outputname, nostamp):
    pdf = FPDF(orientation = "L", format = "A5")
    pdf.compress = False
    if nostamp:
        pdf._putinfo = lambda: common.test_putinfo(pdf)
    pdf.set_font('Arial', '', 14)
    for i, a in enumerate((0, 90, 180, 270)):
        pdf.add_page()
        pdf.set_page_options("rotate", a)
        pdf.write(8, "Page #%d - %d" % (i + 1, a))
        pdf.ln(8)
    pdf.output(outputname, 'F')

def main():
    return common.testmain(__file__, dotest)

if __name__ == "__main__":
    main()

