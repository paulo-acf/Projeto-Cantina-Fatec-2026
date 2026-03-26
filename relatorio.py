# No terminal, digitar:
#    •pip install reportlab
#    •Se o comando da linha acima não funcionar --> python -m pip install reportlab

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def gerar_pdf(sistema):
    doc = SimpleDocTemplate("relatorio.pdf")
    styles = getSampleStyleSheet()

    elementos = []

    # Título
    elementos.append(Paragraph("RELATÓRIO DA CANTINA", styles["Title"]))
    elementos.append(Spacer(1, 12))

    # =========================
    # VENDAS
    # =========================
    elementos.append(Paragraph("VENDAS", styles["Heading2"]))

    vendas = sistema.relatorio_vendas()
    for v in vendas:
        texto = f"{v['nome']} - R$ {v['valor']} - {v['data']}"
        elementos.append(Paragraph(texto, styles["Normal"]))

    elementos.append(Spacer(1, 12))

    # =========================
    # CONSUMO
    # =========================
    elementos.append(Paragraph("CONSUMO", styles["Heading2"]))

    consumos = sistema.relatorio_consumo()
    for c in consumos:
        texto = f"{c['produto']} - {c['quantidade']} unidades - R$ {c['total']}"
        elementos.append(Paragraph(texto, styles["Normal"]))

    elementos.append(Spacer(1, 12))

    # =========================
    # ESTOQUE
    # =========================
    elementos.append(Paragraph("ESTOQUE", styles["Heading2"]))

    produtos = sistema._Sistema__produtos  # acesso interno
    for p in produtos:
        texto = f"{p['nome']} - Qtd: {p['quantidade']}"
        elementos.append(Paragraph(texto, styles["Normal"]))

    elementos.append(Spacer(1, 12))

    # =========================
    # AVISOS
    # =========================
    elementos.append(Paragraph("AVISOS", styles["Heading2"]))

    avisos = sistema.alguns_avisos()
    for a in avisos:
        elementos.append(Paragraph(a, styles["Normal"]))

    # Gerar PDF
    doc.build(elementos)