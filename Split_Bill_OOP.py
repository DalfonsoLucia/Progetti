# App: Split Bill
# Questa mini app riceve in imput il Valore Totale della BOLLETTA,
# Il Periodo relativo alla bolletta (es.Giugno 2021), il Numero di Giorni che ogni INQUILINO ha visuutto in casa,
# Il Nome di ogni inquilino
# e in base a questi input si calcolerà quanto ammonta il pagamento per ogni inquilino.
# Deve poi generare un REPORT in PDF con queste info:
# nome degli inquilini, il periodo e totale da pagare

# Bill:
#   valore_totale
#   Periodo

# Inquilino:
#   giorni_a_casa
#   nome
#   paga(bill)

# PdfReport:
#   filename
#   crea()

from fpdf import FPDF
import os

class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Inquilino:
    def __init__(self, nome, giorni_a_casa):
        self.nome = nome
        self.giorni_a_casa = giorni_a_casa

    def paga(self, bill, inquilino2):
        peso = self.giorni_a_casa / (self.giorni_a_casa + inquilino2.giorni_a_casa)
        return bill.amount * peso

class PdfReport():
    def __init__(self, filename):
        self.filename = filename

    def crea(self, inquilino1, inquilino2, bill):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 40, style = "B")
        pdf.set_text_color(0,0,255)
        pdf.cell(w = 0, h = 40, txt = "Bolletta", border = 1, align = "C", ln = 1)
        pdf.set_font ("Arial", size=20, style = "B")
        pdf.set_text_color(0,0,0)
        pdf.cell(w = 40, h = 20, txt = "Periodo: ", border=0, align= "L")
        pdf.cell(w = 60, h = 20, txt= bill.period, border=0, align= "L", ln = 1)
        pdf.set_text_color(0,0,0)
        pdf.cell(w = 40, h = 20, txt = inquilino1.nome, border = 0, align = "L")
        pdf.cell(w = 60, h = 20, txt = str(round(inquilino1.paga(bill,inquilino2), 2)) + " euro", border = 0, align = "L", ln = 1)
        pdf.cell(w = 40, h = 20, txt = inquilino2.nome, border = 0, align = "L")
        pdf.cell(w = 60, h = 20, txt = str(round(inquilino2.paga(bill,inquilino1), 2)) + " euro" , border = 0, align = "L", ln = 1)

        output = self.filename + ".pdf"
        pdf.output(output)

amount = float(input("Inserisci valore della bolletta: "))
periodo = input("A quale periodo si riferisce questa bolletta?")

nome1 = input("Nome inquilino1: ")
giorni1 = float(input(f"Quanti giorni è stato {nome1} in casa?: "))

nome2 = input("Nome inquilino2: ")
giorni2 = float(input(f"Quanti giorni è stato {nome2} in casa?: "))


bill = Bill(amount, periodo)
inq1 = Inquilino(nome1, giorni1)
inq2 = Inquilino(nome2, giorni2)

print(f"{nome1} dovrà pagare:", round(inq1.paga(bill, inq2), 2))
print(f"{nome2} dovrà pagare:", round(inq2.paga(bill, inq1), 2))
print(f"Un report PDF è stato creato relativo al periodo {periodo}")
print('Il report si trova qui: ', os.getcwd())

pdf = PdfReport(periodo)
pdf.crea(inq1, inq2, bill)

    
    















