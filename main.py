from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

pdf.add_page()

for index, row in df.iterrows():
    pdf.set_font(family='Arial', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['topic'], align='L', ln=1)
    # pdf.line(x1, y1, x2, y2)
    pdf.line(10, 21, 200, 21)

pdf.output(output.pdf)
