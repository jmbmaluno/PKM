from bs4 import BeautifulSoup
import requests

Status = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]


#Recebe uma url, faz o request e devolve a classe BeautifulSoup
class Site:
    def __init__(self, url):
        self.url = url
        self.result = requests.get(self.url)
        self.doc = BeautifulSoup(self.result.text, "html.parser")
        
    
    def get_doc(self):
        return self.doc
    
class Pkm:

    def __init__(self, nome = "", url_pkm = ""):
        self.nome = nome
        if url_pkm == "":
            self.site = None
            self.site_move = None
        else:
            self.site = Site(url_pkm)
            self.site_move = Site(url_pkm + "/move/3")
        
        self.tipo = []
        self.habilidade = []
        self.status = [0] * 6
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_url_pkm(self, url):
        self.site = Site(url)
        self.site_move = Site(url + "/move/3") 
    
    def atualizar_dados(self):
        doc = self.site.get_doc()

        dados_tipo = doc.find("th", string = "Type").parent
        for i in dados_tipo.find_all("a"):
            self.tipo.append(str(i.string))

        dados_habilidade = doc.find("th", string = "Abilities").parent
        for i in dados_habilidade.find_all("a"):
            self.habilidade.append(str(i.string))
        
        global Status
        for i in range(len(Status)):
            dados_status = doc.find("th", string = str(Status[i])).parent
            self.status[i] = int(dados_status.find("td", {"class" : "cell-num"}).string)