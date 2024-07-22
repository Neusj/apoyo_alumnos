from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from io import BytesIO

def generar_reporte(reporte):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()
    
    # Título del documento
    title = "Reporte Psicológico"
    elements.append(Paragraph(title, styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Información del estudiante
    elements.append(Paragraph("Estudiante:", styles['Heading2']))
    elements.append(Paragraph(reporte.estudiante.nombre_completo, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Información del psicólogo
    elements.append(Paragraph("Psicólogo:", styles['Heading2']))
    elements.append(Paragraph(reporte.psicologo.nombre_completo, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Información del apoderado
    elements.append(Paragraph("Apoderado:", styles['Heading2']))
    elements.append(Paragraph(reporte.estudiante.apoderado.nombre_completo, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    # Detalles del reporte
    elements.append(Paragraph("Estado:", styles['Heading2']))
    elements.append(Paragraph(reporte.estado, styles['Normal']))
    elements.append(Spacer(1, 12))

    
    elements.append(Paragraph("Recomendación:", styles['Heading2']))
    elements.append(Paragraph(reporte.recomendacion, styles['Normal']))
    elements.append(Spacer(1, 12))
    
    
    
    # Construir el PDF
    doc.build(elements)
    
    pdf = buffer.getvalue()
    buffer.close()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporte_{reporte.estudiante.rut}.pdf"'
    
    return response
