# No terminal, digitar --> python main.py

from sistema import Sistema
from relatorio import gerar_pdf
from utils import popular # Para "povoar" o sistema

s = Sistema() # C O L O C A R   D A D O S   M A N U A I S   L O G O   A B A I X O   D A S   A R R O U B A S
# @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @

# s.adicionar_produto("Coxinha de frango", 3.50, 7.00, "2026-03-20", "2026-03-25", 30)
# s.adicionar_produto("Refrigerante lata 350ml", 2.80, 6.00, "2026-03-01", "2026-09-01", 50)
# s.adicionar_produto("Água mineral 500ml", 1.50, 3.50, "2026-03-10", "2027-03-10", 100)
# s.adicionar_produto("Pão francês", 0.50, 1.20, "2026-03-25", "2026-03-26", 200)
# s.adicionar_produto("Suco natural de laranja", 4.00, 8.00, "2026-03-25", "2026-03-27", 25)
# s.adicionar_produto("Barra de chocolate ao leite", 3.00, 6.50, "2026-02-15", "2026-12-15", 40)
# s.adicionar_produto("Bala sortida pacote", 1.00, 2.50, "2026-01-10", "2027-01-10", 80)
# s.adicionar_produto("Salgadinho milho 100g", 2.20, 5.00, "2026-02-20", "2026-08-20", 60)
# s.adicionar_produto("Sanduíche natural", 5.00, 10.00, "2026-03-25", "2026-03-26", 15)
# s.adicionar_produto("Café expresso", 1.00, 4.00, "2026-03-25", "2026-03-25", 70)

# # 🔴 Inserir produto
# s.adicionar_produto("Coxinha", 3.5, 7.0, "2026-03-20", "2026-03-25", 30)
# # 🔴 Realizar venda
# s.vender(1, "João", 5, "aluno", "IoT")          # Saída --> True (venda realizada)
# # 🔴 Ver vendas
# s.relatorio_vendas()                            # Saída --> [{'nome': 'João', 'valor': 35.0, ...}]
# # 🔴 Ver consumo
# s.relatorio_consumo()                           # Saída --> [{'produto': 'Coxinha', 'quantidade': 5, ...}]
# # 🔴 Editar quantidade (estoque)
# s.editar_quantidade(1, 10, "ajuste manual")     # Saída --> True
# # 🔴 Ver avisos (estoque baixo / vencido)
# s.alguns_avisos()                               # Saída --> ['Estoque baixo: Coxinha'] ou ['Vencido: Coxinha']
# # 🔴 Gerar PDF
# gerar_pdf(s)                                    # Saída --> PDF com relatório completo

# @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @
# # COMENTAR QUANDO NÃO FOR NECESSÁRIO:
# #   •PARA FAZER COM FAKER (e não manualmente) (•Nome produto •Preço compra •Preço venda •Datas •Quantidade)
# popular(s, 5)
# #   •PARA FAZER COM FAKER (e não manualmente)
# # VENDA
# s.vender(1, "João", 2, "aluno", "IoT")
# s.vender(2, "Maria", 1, "professor", "ADS")
# ############################################

############################################
# RELATÓRIOS E PDF
print("=== VENDAS ===")
print(s.relatorio_vendas())

print("\n=== CONSUMO ===")
print(s.relatorio_consumo())

print("\n=== ESTOQUE ===")
for p in s.relatorio_estoque():
    print(f"{p['nome']} - Qtd: {p['quantidade']}")

print("\n=== AVISOS ===")
print(s.alguns_avisos())

# GERANDO PDF
gerar_pdf(s)
print("PDF gerado com sucesso!")
############################################