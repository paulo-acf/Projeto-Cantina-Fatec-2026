import pickle
# É um módulo da biblioteca padrão do Python
# Serializa objetos py (lista etc.) em um fluxo de bytes •armazenável, •enviável e •desserializável

##############################
#######   P I C K L E
##############################

def salvar(sistema, arquivo = "dados.pkl"):
    with open(arquivo, "wb") as f:
        pickle.dump(sistema, f)

def carregar(arquivo = "dados.pkl"):
    with open(arquivo, "rb") as f:
        return pickle.load(f)