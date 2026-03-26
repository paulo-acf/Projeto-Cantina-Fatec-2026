# No terminal, digitar:
#    •pip install reportlab
#    •Se o comando da linha acima não funcionar --> python -m pip install reportlab

# Importa classes da biblioteca reportlab para criar o PDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Importa estilos prontos de texto (título, subtítulo, etc.)
from reportlab.lib.styles import getSampleStyleSheet


# Função que gera o PDF, recebendo o objeto sistema
def gerar_pdf(sistema):

    # Cria o documento PDF chamado "relatorio.pdf"
    doc = SimpleDocTemplate("relatorio.pdf")

    # Carrega estilos prontos (Title, Heading, Normal...)
    styles = getSampleStyleSheet()

    # Lista que armazenará todos os elementos do PDF
    elementos = []

    ##############################
    #######   T Í T U L O
    ##############################

    # Adiciona o título principal do relatório
    elementos.append(Paragraph("RELATÓRIO DA CANTINA", styles["Title"]))

    # Adiciona espaço entre seções
    elementos.append(Spacer(1, 12)) # •1 --> largura •12 --> altura

    ##############################
    #######   V E N D A S
    ##############################

    # Adiciona subtítulo da seção VENDAS
    elementos.append(Paragraph("VENDAS", styles["Heading2"])) # •Heading (Título) •Heading2 (Subtítulo) 

    # Obtém os dados de vendas do sistema
    vendas = sistema.relatorio_vendas()

    # Percorre cada venda
    for v in vendas:
        # Monta o texto com nome, valor e data da venda
        texto = f"{v['nome']} - R$ {v['valor']} - {v['data']}"

        # Adiciona esse texto ao PDF
        elementos.append(Paragraph(texto, styles["Normal"]))

    # Adiciona espaço entre seções
    elementos.append(Spacer(1, 12)) # •1 --> largura •12 --> altura

    ##############################
    #######   C O N S U M O
    ##############################

    # Adiciona subtítulo da seção CONSUMO
    elementos.append(Paragraph("CONSUMO", styles["Heading2"]))

    # Obtém os dados de consumo do sistema
    consumos = sistema.relatorio_consumo()

    # Percorre cada consumo
    for c in consumos:
        # Monta o texto com produto, quantidade e valor total
        texto = f"{c['produto']} - {c['quantidade']} unidades - R$ {c['total']}"

        # Adiciona esse texto ao PDF
        elementos.append(Paragraph(texto, styles["Normal"]))

    # Adiciona espaço entre seções
    elementos.append(Spacer(1, 12)) # •1 --> largura •12 --> altura

    ##############################
    #######   E S T O Q U E
    ##############################

    # Adiciona subtítulo da seção ESTOQUE
    elementos.append(Paragraph("ESTOQUE", styles["Heading2"])) # •Heading (Título) •Heading2 (Subtítulo) 

    # Acessa diretamente o atributo privado __produtos da classe Sistema
    produtos = sistema._Sistema__produtos  # acesso interno

    # Percorre os produtos
    for p in produtos:
        # Monta o texto com nome e quantidade em estoque
        texto = f"{p['nome']} - Qtd: {p['quantidade']}"

        # Adiciona esse texto ao PDF
        elementos.append(Paragraph(texto, styles["Normal"]))

    # Adiciona espaço entre seções
    elementos.append(Spacer(1, 12)) # •1 --> largura •12 --> altura

    ##############################
    #######   A V I S O S
    ##############################

    # Adiciona subtítulo da seção AVISOS
    elementos.append(Paragraph("AVISOS", styles["Heading2"])) # •Heading (Título) •Heading2 (Subtítulo) 

    # Obtém avisos do sistema (estoque baixo ou produtos vencidos)
    avisos = sistema.alguns_avisos()

    # Percorre os avisos
    for a in avisos:
        # Adiciona cada aviso no PDF
        elementos.append(Paragraph(a, styles["Normal"]))

    ##############################
    #######   A V I S O S
    ##############################

    # Gera o PDF final com todos os elementos adicionados
    doc.build(elementos)