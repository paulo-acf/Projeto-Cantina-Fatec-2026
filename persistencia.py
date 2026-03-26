import pickle
# É um módulo da biblioteca padrão do Python
# Serializa objetos py (lista etc.) em um fluxo de bytes •armazenável, •enviável e •desserializável

##############################
#######   P I C K L E
##############################

##### Salvar --> •Não carrega o arquivo; •apenas o salva

def salvar(sistema, arquivo = "dados.pkl"): # Aqui, o nome do arquivo será "dados.pkl" (padrão)
    with open(arquivo, "wb") as f: # --> Abre o arquivo em modo ♦"w" (escrita) e ♦"b" (binário - pickle usa binário)
    # with:
    #    •Fecha o arquivo automaticamente
    #    •Garante que todos os dados serão salvos
    #    •Libera recursos do sistema
    #    •Evita travamento do arquivo   
        pickle.dump(sistema, f)
        # Pega todo o objeto (self) e:
        #    •Transforma em bytes ("serializa")
        #    •Salva no arquivo "f"

##### Carregar --> •Não salva o arquivo; •apenas o carrega

def carregar(arquivo = "dados.pkl"):
    with open(arquivo, "rb") as f: # --> Abre o arquivo em modo ♦"r" (leitura) e ♦"b" (binário - pickle usa binário)
    # with:
    #    •Fecha o arquivo automaticamente
    #    •Libera recursos do sistema
    #    •Evita travamento do arquivo   
        return pickle.load(f)
        # Lê o arquivo e:
        #    •Carrega o objeto original
        #    •Retorna esse objeto