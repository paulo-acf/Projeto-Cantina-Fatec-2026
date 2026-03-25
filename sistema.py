from datetime import datetime
# "datetime" na linha acima, respectivamente --> •Módulo •Classe
# Permite trabalhar com •datas e •horas

##############################
#######   D A D O S
##############################

class Sistema: # Classe ("molde", "planta") --> Aqui, é como se fosse a estrutura de uma "cantina vazia"
    def __init__(self): # Método construtor (•Cria listas vazias •Prepara variáveis •Deixa tudo pronto)
        self.__produtos = [] # self --> Remete ao próprio objeto
        # self.__produtos --> Será uma lista de dicionários (vide   "E S T O Q U E")
        self.__pagamentos = [] # Lista --> Além de ser ordenada, permite adicionar/remover itens em qualquer posição
        self.__consumos = []
        self.__id_produto = 0 # Será usado num contador

##############################
#######   E S T O Q U E
##############################

    def adicionar_produto(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):

        self.__id_produto += 1

        produto = {
            "id": self.__id_produto,
            "nome": nome,
            "preco_compra": preco_compra,
            "preco_venda": preco_venda,
            "data_compra": data_compra,
            "data_vencimento": data_vencimento,
            "quantidade": quantidade,
            "historico": []
        }

        self.__produtos.append(produto) # self.__produtos --> É a lista de produtos dentro da classe "Sistema"

    def editar_quantidade(self, id_produto, nova_qtd, motivo = "ajuste"):
        for p in self.__produtos:
        # p = Um produto = Um dicionário = {"id": 1, "nome": "arroz", "quantidade": 10}
        # p["id"] --> Pega o id do produto
            if p["id"] == id_produto:

                p["historico"].append({
                    "antes": p["quantidade"],
                    "depois": nova_qtd,
                    "motivo": motivo,
                    "data": str(datetime.now()) # Ex. de saída --> 2026-03-22 14:35:12.483921
                })

                p["quantidade"] = nova_qtd
                return True # "Significado" --> "Deu certo!!! Produto encontrado!!!"
        return False # "Significado" --> "Não deu certo!!! Produto não encontrado!!!"
    
##############################
#######   P A G A M E N T O S
##############################

    def registrar_pagamento(self, nome, categoria, curso, valor):

        self.__pagamentos.append({
            "nome": nome,
            "categoria": categoria,
            "curso": curso,
            "valor": valor,
            "data": str(datetime.now().date()), # Ex. de saída --> data: 2026-03-22
            "hora": str(datetime.now().time()) # Ex. de saída --> hora: 14:42:18.123456
        })

##############################
#######   V E N D A S
##############################

    def vender(self, id_produto, pessoa, qtd):

        # Prioridade --> Produtos mais antigos (FIFO) (Fila)
        produtos = sorted(self.__produtos, key = lambda x: x["data_compra"])
        # sorted(), apenas --> Ordena •de A até Z ou •do Menor para o Maior 

        for p in produtos:

            if p["id"] == id_produto:

                if p["quantidade"] < qtd: # Se a quantidade disponível for menor que a quantidade pedida --> False
                    return False

                total = p["preco_venda"] * qtd

                p["quantidade"] -= qtd

                self.registrar_pagamento(
                    pessoa,
                    "aluno",
                    "IA",
                    total
                )

                self.__consumos.append({
                    "produto": p["nome"],
                    "pessoa": pessoa,
                    "quantidade": qtd,
                    "total": total
                })

                return True

        return False

##############################
#######   R E L A T Ó R I O S
##############################

    def relatorio_vendas(self):
        return self.__pagamentos # Vide   "D A D O S"

    def relatorio_consumo(self):
        return self.__consumos # Vide   "D A D O S"

##############################
#######   A V I S O S
##############################

    def alguns_avisos(self):
        avisos = []

        for p in self.__produtos:
            if p["quantidade"] < 5:
                avisos.append(f"Estoque baixo: {p['nome']}")

            if p["data_vencimento"] < str(datetime.now().date()):
                avisos.append(f"Vencido: {p['nome']}")

        return avisos