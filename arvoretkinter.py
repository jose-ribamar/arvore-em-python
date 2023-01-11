#WESLEY ALVES RIBEIRO, 20211p2ads0274
#JOSÉ RIBAMAR G. DE SOUSA, 20201p2ads0153

from tkinter import *

class No:  # definicao da classe No
    def __init__(self, dado=None):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
    def obtervalor(self):
        return self.dado
    def getraiz(self):
        return self.dado
    def setraiz(self,raiz):
        self.dado=raiz    
    def getesq(self):
        return self.esquerdo
    def setesq(self,esq):
        self.esquerdo=esq
    def getdir(self):
        return self.direito
    def setdir(self,dir):
        self.direito=dir
    def __str__(self):
        return ("{", str(self.dado), "}")
    def profundidade(self):
        prof_esq = 0
        if self.esquerdo:
            prof_esq = self.esquerdo.profundidade()
        prof_dir = 0
        if self.direito:
            prof_dir = self.direito.profundidade()
        return 1 + max(prof_esq, prof_dir)
class Arvore():
    # Definicao da classe arvore
    def __init__(self):
         # inicializa a raiz
        self.raiz = None

    # cria um novo no e o retorna
    def criaNo(self, dado):
        if self.raiz==None:
            self.raiz=No(dado)
        return No(dado)

    def contaNos(self, raiz):
        if raiz == None:
            return 0
        return 1 + self.contaNos(raiz.esquerdo) + self.contaNos(raiz.direito)

    def calculaProfMaxima(self, raiz):
        if raiz == None:
            return 0
        return raiz.profundidade()

    def grau(self,no):
        if no.esquerdo and no.direito: #SE TIVER 2 NOS
            return 2

        elif no.esquerdo or no.direito:#SE TIVER UM NO
            return 1
        return 0

    def min(self, no=None):#MENOR VALOR, ULTIMO VALOR A ESQUERDA
        if no==None:
            no = self.raiz
        while no.esquerdo:
            no = no.esquerdo
        return no

    def max(self, no=None):#MAIOR VALOR, ULTIMO VALOR A DIREITA
        if no==None:
            no = self.raiz
        while no.direito:
            no = no.direito
        return no
    
    def sucessor(self,raiz):
        if raiz.direito:
            return self.min(raiz.direito)
        y=self.raiz
        while y and raiz is y.direito:
            raiz=y
            y=y.getraiz()
        return y

    def predecessor(self,raiz):
        if raiz.esquerdo:
            return self.max(raiz.esquerdo)
        y=self.raiz
        while y!=None and raiz is y.esquerdo:
            raiz=y
            y=y.getraiz()
        return y

    def busca(self,raiz,valor):
        if raiz==None:
            return "zero"
        if  raiz.obtervalor()==valor:
            return raiz
        if valor<raiz.obtervalor():
            return self.busca(raiz.esquerdo,valor)
        else:
            return self.busca(raiz.direito,valor)

    def encontraPai(self,valor,raiz):
        try:
            point=raiz
            while True:
                if point==valor:
                    return self.raiz

                elif point.esquerdo==valor or point.direito==valor:#O PAI VAI SE O
                    return point

                elif point.dado>valor.dado:
                    point=point.esquerdo

                elif point.dado<valor.dado:
                    point=point.direito
        except AttributeError:
            return

    def insere(self, raiz, dado):
        if raiz == None:
            return self.criaNo(dado)
        else:
            if dado==raiz.dado:
                return raiz
            elif dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
        return raiz
class Aplicacao(Arvore):
    def __init__(self, root):
        self.arvore = None
        # ENVIAR VALORES 
        self.t1 = Entry(root,bg="lightblue")
        self.t1.bind("<Return>", self.constroiArvore)
        self.t1.place(x=10, y=10, width=100,height=30)

        self.t2=Entry(root,bg="lightblue")
        self.t2.bind("<Return>", self.destroiNo)
        self.t2.place(x=10, y=40, width=100,height=30)

        self.t3=Entry(root,bg="lightblue")
        self.t3.bind("<Return>", self.caminho)
        self.t3.place(x=110, y=80, width=100,height=30)

        self.t4=Entry(root,bg="lightblue")
        self.t4.bind("<Return>",self.caminho)
        self.t4.place(x=10, y=80, width=100,height=30)

        self.t5=Entry(root,bg="lightblue")
        self.t5.bind("<Return>", self.buscarNo)
        self.t5.place(x=10, y=120, width=100,height=30)

        
        self.bt_enviar=Button(root,text="INSERIR",command=self.constroiArvore)
        self.bt_enviar.place(x=110, y=10, width=100,height=30)
        
        self.bt_remover=Button(root,text="REMOVER",command=self.destroiNo)
        self.bt_remover.place(x=110, y=40, width=100,height=30)

        self.bt_caminhoAB=Button(root,text="CAMINHO AB",command=self.caminho)
        self.bt_caminhoAB.place(x=210, y=80, width=100,height=30)

        self.bt_buscar=Button(root,text="BUSCAR",command=self.buscarNo)
        self.bt_buscar.place(x=110, y=120, width=100,height=30)


        #TELA
        self.c1 = Canvas(root, width=1000, height=1000)
        self.c1.pack(side=RIGHT)

    def buscarNo(self,*args):
        valor=float(self.t5.get())
        raiz=self.raiz
        busca=self.arvore.busca(raiz,valor)
        if busca=="zero":
            return
        else:
            grau=self.arvore.grau(busca)
            point=self.raiz
            prof=0
            while True:
                if point.dado<busca.dado:
                    point=point.direito
                    prof+=1
                elif point.dado>busca.dado:
                    point=point.esquerdo
                    prof+=1
                else:
                    break
            
            pai=self.arvore.encontraPai(valor,raiz)
            if busca==self.raiz:
                pai="Não tem, é a raiz"
            else:
                pai=self.arvore.encontraPai(busca,self.raiz).dado

            self.c1.create_rectangle(170,20,340,100, fill="red")
            
            self.c1.create_text(250, 60, text=f"DADOS DO NÓ BUSCADO:\nValor:{valor}\nPai:{pai}\nGrau: {grau}\nProfundidade:{prof}")

    def caminho(self,*args):
        valor=float(self.t3.get())
        valor2=float(self.t4.get())
        
        buscado=self.arvore.busca(self.raiz,valor)
        point=self.arvore.busca(self.raiz,valor2)
        if buscado!="zero" and point!="zero":
            self.c1.create_rectangle(0, 0, self.HORIZONTAL, self.VERTICAL, fill="blue")
            temp=Arvore()
            while point!=None:
                temp.insere(temp.raiz,point.dado)
                if point.dado==valor:
                    break
                elif point.dado<valor:
                    point=point.direito
                else:
                    point=point.esquerdo

        if temp.raiz==None:
            return
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(0, 0, self.HORIZONTAL, self.VERTICAL, fill="blue")
        self.xmax = self.c1.winfo_width()-140  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = temp.calculaProfMaxima(self.raiz)#OBS
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.desenhaNo(temp.raiz, x1, y1, x1, y1, 1, False)

    def destroiNo(self,*args):
        try:
            valor=float(self.t2.get())

            if valor==self.raiz.dado: #REMOVER A RAIZ
                if self.raiz.esquerdo==None and self.raiz.direito==None:#SEM NO
                    del self.arvore
                    self.arvore=None
                    self.desenhaArvore()
                    return
                
                if self.raiz.esquerdo==None and self.raiz.direito:#NO A DIREITA
                    self.raiz=self.raiz.direito
                    self.desenhaArvore()
                    return

                elif self.raiz.esquerdo and self.raiz.direito==None:#NO A DIREITA
                    self.raiz=self.raiz.esquerdo
                    self.desenhaArvore()
                    return
                else:#NO ESQUERDA/DIREITA
                    valor=float(self.t2.get())
                    substituto=self.arvore.sucessor(self.raiz)
                    paiDoSubstituto=self.arvore.encontraPai(substituto,self.raiz)
                    direita=self.raiz.direito
                    esquerda=self.raiz.esquerdo
                    if paiDoSubstituto==self.raiz:
                        self.raiz=substituto
                        self.raiz.esquerdo=esquerda

                    elif substituto.direito==None:
                        if paiDoSubstituto.dado>substituto.dado:
                            self.raiz=substituto
                            paiDoSubstituto.esquerdo=None
                            self.raiz.esquerdo=esquerda
                            self.raiz.direito=direita
                        else:
                            self.raiz=substituto
                            paiDoSubstituto.direito=None
                            self.raiz.esquerdo=esquerda
                            self.raiz.direito=direita
                    else:
                        if paiDoSubstituto.dado>substituto.dado:
                            self.raiz=substituto
                            paiDoSubstituto.esquerdo=substituto.direito
                            self.raiz.direito=direita
                            self.raiz.esquerdo=esquerda
                        else:
                            self.raiz=substituto
                            paiDoSubstituto.esquerdo=substituto.direito
                            self.raiz.direito=direita
                            self.raiz.esquerdo=esquerda

                self.desenhaArvore()
                return        
            else:  #NÃO É A RAIZ
                buscado=self.arvore.busca(self.raiz,valor)
                if buscado!="zero:":
                    paiDoBuscado=self.arvore.encontraPai(buscado,self.raiz) #REMOVENDO NÓS FOLHA
                    if buscado.esquerdo==None and buscado.direito==None:
                        if paiDoBuscado.dado>buscado.dado:
                            paiDoBuscado.esquerdo=None
                        else:
                            paiDoBuscado.direito=None
                    elif buscado.esquerdo and buscado.direito==None:#REMOVENDO NÓS SÓ COM UM FILHO NA ESQUERDA
                        if paiDoBuscado.dado>buscado.dado:
                            paiDoBuscado.esquerdo=buscado.esquerdo
                        else:
                            paiDoBuscado.direito=buscado.esquerdo
                    elif buscado.esquerdo==None and buscado.direito:#REMOVENDO NÓS SÓ COM UM FILHO NA DIREITA
                        if paiDoBuscado.dado>buscado.dado:
                            paiDoBuscado.esquerdo=buscado.direito
                        else:
                            paiDoBuscado.direito=buscado.direito
                    else:#REMOVENDO NÓS COM DOIS FILHOS
                        substituto=self.arvore.sucessor(buscado)
                        paiDoSubstituto=self.arvore.encontraPai(substituto,self.raiz)
                        direita=buscado.direito
                        esquerda=buscado.esquerdo

                        if paiDoSubstituto.dado!=buscado.dado:
                            if paiDoBuscado.dado>buscado.dado:
                                paiDoBuscado.esquerdo=substituto
                                substituto.esquerdo=esquerda
                                paiDoSubstituto.esquerdo=None
                                substituto.direito=direita
                            else:
                                paiDoBuscado.direito=substituto
                                substituto.esquerdo=esquerda
                                paiDoSubstituto.esquerdo=None
                                substituto.direito=direita
                        else:
                            if valor > self.raiz.dado: #SE ELE FOR PARA ESQUERDA
                                if valor == self.raiz.direito.dado:
                                    paiDoBuscado.direito=substituto
                                    substituto.esquerdo=esquerda
                                elif valor > self.raiz.direito.dado: 
                                    paiDoBuscado.direito=substituto
                                    substituto.esquerdo=esquerda
                                else:
                                    paiDoBuscado.esquerdo=substituto
                                    substituto.esquerdo=esquerda
                            else:
                                paiDoBuscado.esquerdo=substituto
                                substituto.esquerdo=esquerda
                              
                else:
                    print("valor não existe nessa arvore")
            self.desenhaArvore()
            self.infos()
        except AttributeError:
            return
    def infos(self):
        raiz=self.raiz
        self.c1.create_rectangle(20,20,160,100, fill="lightblue")
        try:
            prof=(self.arvore.calculaProfMaxima(self.raiz))
            qtd=self.arvore.contaNos(raiz)

            self.c1.create_text(80, 50, text=f"   ALTURA:{prof}\n   QUANTIDADE DE NÓS:{qtd}")
        except AttributeError:
            return
    def constroiArvore(self, *args):
        try:
            valores = str(self.t1.get()).split(";")
        except Exception:
            return
        for valor in valores:
            if self.arvore == None:
                self.arvore = Arvore()
                self.raiz = self.arvore.criaNo(float(valor))
            else:
                self.arvore.insere(self.raiz, float(valor))
            self.desenhaArvore(False)
            self.infos()
    def desenhaArvore(self, comFB = False):
        if self.raiz==None:
            return
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(0, 0, self.HORIZONTAL, self.VERTICAL, fill="blue")
        self.xmax = self.c1.winfo_width()-140  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = self.arvore.calculaProfMaxima(self.raiz)
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.desenhaNo(self.raiz, x1, y1, x1, y1, 1, comFB)
    def desenhaNo(self, no, posAX, posAY, posX, posY, linha, comFB = False):
        if no == None:
            return
        numero_colunas = 2**(linha + 1)#mexer no tamanho
        x1 = int(posX - self.tamanho/2)
        y1 = int(posY - self.tamanho/2)

        x2 = int(posX + self.tamanho/2)
        y2 = int(posY + self.tamanho/2)

        cor = "white"

        self.c1.create_line(posAX, posAY+15, posX, posY, fill= "red",width=5)
        self.c1.create_oval(x1, y1, x2, y2, fill=cor)

        rotulo = str(no.dado)

        self.c1.create_text(posX, posY, text=str(rotulo))
        posAX, posAY = posX, posY
        dx = self.xmax / numero_colunas
        dy = self.ymax / (self.numero_linhas + 1)
        posX = posAX + dx
        posY = posAY + dy
        self.desenhaNo(no.direito, posAX, posAY, posX, posY, linha + 1, comFB)
        posX = posAX - dx
        self.desenhaNo(no.esquerdo, posAX, posAY, posX, posY, linha + 1, comFB)

if __name__ == "__main__":
    root = Tk(None, None)
    root.geometry("2048x1500")
    app = Aplicacao(root)
    root.mainloop()