# students/formats.py
from import_export.formats.base_formats import Format
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

class PDFFormat(Format):
    def get_title(self):
        return "pdf"

    def get_extension(self):
        return "pdf"

    def get_content_type(self):
        return "application/pdf"

    def export_data(self, dataset, **kwargs):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 40
        x = 40

        for row in dataset.dict:
            line = ", ".join([str(cell) for cell in row.values()])
            c.drawString(x, y, line)
            y -= 15
            if y < 40:
                c.showPage()
                y = height - 40

        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

    def is_binary(self):
        return True
