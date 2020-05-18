"""import csv

with open(r'employee_file.csv', mode='a+', newline='') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #employee_writer = csv.writer(employee_file)
    employee_writer.writerow(['Camila', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])"""

"""from reportlab.pdfgen import canvas
def hello(c):
 	c.drawString(180,400,"GRACIAS POR COMPRAR EN PYSTREAM")
 	c.drawString(180,300,"GRACIAS POR COMPRAR EN PYSTREAM")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
canvas.drawString(30,750,'PYSTREAM.SA')
canvas.drawString(30,735,'COMPROBANTE DE COMPRA')
canvas.drawString(500,750,"12/12/2010")
canvas.line(480,747,580,747)
canvas.drawString(275,725,'MONTO POR:')
canvas.drawString(500,725,"$1,000.00")
canvas.line(378,723,580,723)
canvas.drawString(30,703,'REALIZADO POR:')
canvas.line(120,700,580,700)
canvas.drawString(160,703,"JOHN DOE")
canvas.line(30,680,580,680)
canvas.drawString(190,682,"LISTADO DE CANCIONES COMPRADAS")
#canvas.drawString(190,662,"LISTADO DE CANCIONES COMPRADAS")
altura=642
var1="hola amigo"
var2="como estas"
for i in range(3):
	canvas.drawString(190,altura, var1+"..................."+var2)
	altura-=20

#canvas.line(30,680,580,650)
canvas.save()

"""import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story=[]
#logo = "python_logo.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"
formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]
#im = Image(logo, 2*inch, 2*inch)
#Story.append(im)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '<font size="12">%s</font>' % formatted_time
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
# Create return address
ptext = '<font size="12">%s</font>' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))       
for part in address_parts:
    ptext = '<font size="12">%s</font>' % part.strip()
    Story.append(Paragraph(ptext, styles["Normal"]))   
Story.append(Spacer(1, 12))
ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
ptext = '<font size="12">We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName, 
                                                                                                issueNum,
                                                                                                subPrice,
                                                                                                limitedDate,
                                                                                                freeGift)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = '<font size="12">Sincerely,</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 48))
ptext = '<font size="12">Ima Sucker</font>'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)"""