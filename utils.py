# No terminal abaixo (ou "New Terminal"), para instalar o Faker:
#   •pip install faker
#   •Se o comando acima não funcionar --> python -m pip install faker

from faker import Faker # Gera dados aleatórios - para "popular" ("povoar") o sistema
fake = Faker()
# •Faker (classe, "molde") •Faker() (cria objeto desta classe) •fake (objeto que gera dados falsos)

##############################
#######   F A K E R
##############################

def popular(sistema, qtd = 5):
    for _ in range(qtd):
        sistema.adicionar_produto(
            fake.word(),


# @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ #


            round(fake.pyfloat(left_digits = 2, right_digits = 2, positive = True), 2),


# @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ # @ #


            round(fake.random_number(2) * 1.5, 2),
            str(fake.date()),
            str(fake.date()),
            fake.random_int(1, 50)
        )