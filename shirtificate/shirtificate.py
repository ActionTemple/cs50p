

# CS50 Shirtificate
# Andrew Waddington

from fpdf import FPDF

def main():
    name = input("Name: ")


    pdf = FPDF()
    pdf.add_page()
    #pdf.image("../shirtificate/shirtificate.png", 17.5, 55, 175)
    pdf.image("shirtificate.png", 17.5, 55, 175)
    pdf.set_font("helvetica", style="B", size=32)
    pdf.ln(15)
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", style="B", size=16)
    pdf.ln(90)
    pdf.cell(0, 10, text=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
