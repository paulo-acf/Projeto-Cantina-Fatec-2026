# No terminal, digitar --> python main.py

from sistema import Sistema
from relatorio import gerar_pdf

s = Sistema()

# Inserindo produtos manualmente
s.adicionar_produto("Coxinha", 2.5, 5.0, "2026-03-20", "2026-03-30", 10)
s.adicionar_produto("Refrigerante", 3.0, 6.0, "2026-03-21", "2026-06-01", 15)

# Venda
s.vender(1, "João", 2)
s.vender(2, "Maria", 1)

print("=== VENDAS ===")
print(s.relatorio_vendas())

print("\n=== CONSUMO ===")
print(s.relatorio_consumo())

print("\n=== AVISOS ===")
print(s.alguns_avisos())

gerar_pdf(s)
print("PDF gerado com sucesso!")

# Testando commit

# teste 2