# No terminal abaixo (ou "New Terminal"), para instalar o Faker:
#   •pip install faker
#   •Se o comando acima não funcionar --> python -m pip install faker

from faker import Faker

from relatorio import gerar_pdf
from sistema import Sistema # Gera dados aleatórios - para "popular" ("povoar") o sistema
fake = Faker()
# •Faker (classe, "molde") •Faker() (cria objeto desta classe) •fake (objeto que gera dados falsos)

##############################
#######   F A K E R
##############################

def popular(sistema, qtd = 5):
    # "popular" = "povoar"
    # "qtd":
    #    •Quantidade de produtos a criar (aqui, o padrão é 5)
    #    •Pode ser qualquer outro valor inteiro positivo
    for _ in range(qtd):
        # _:
        #    •Aqui, indica que a variável do loop não será importante
        #    •A ideia aqui é apenas repetir o processo n vezes (ou qtd vezes)
        #    •Ou seja:
        #        ♦Os números são gerados normalmente (0, 1, 2, ... qtd-1)...
        #        ♦Mas em nenhum momento esses números são usados dentro do for
        sistema.adicionar_produto(
            fake.word(),


# @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ #


            # round(fake.random_number(2), 2), # --> Simula um PREÇO de COMPRA (número inteiro)
            # OU
            # ABAIXO, OPÇÃO DECIMAL PARA A LINHA ACIMA COM FAKER:
            round(fake.pyfloat(left_digits = 2, right_digits = 2, positive = True), 2),
            # round --> Função nativa do Python usada para arredondar números
            # pyfloat --> Método da biblioteca Faker (gera números decimais aleatórios)


# @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ #


            # Primeiro 2 --> Gera um número com até 2 dígitos
            # Segundo 2 --> Mantém até 2 casas decimais
            round(fake.random_number(2) * 1.5, 2), # --> Simula um PREÇO de VENDA                
            str(fake.date()), # --> Simula uma DATA de COMPRA 
            str(fake.date()), # --> Simula uma DATA de VENCIMENTO
            fake.random_int(1, 50) # --> Simula uma QUANTIDADE em ESTOQUE (aqui, entre 1 e 50)
        )



# DADOS JÁ PRONTOS PARA MAIN:

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