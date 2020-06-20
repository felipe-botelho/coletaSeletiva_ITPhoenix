from tkinter import *
import time
from teste import Clock

janela = Tk()
janela.geometry("600x400+100+100")
janela.title("Pergunta 1")
Clock()

labeltexto = Label(
    janela,
    Clock()
)
labeltexto.pack()

#função para a resposta 1
def um():
    v.set('Você errou!! Alternativa correta é a letra B')
#função para a resposta 2
def dois():
    v.set('Você acertou!!')
def tres():
    v.set('Você errou!! Alternativa correta é a letra B')
def quatro():
    v.set('Você errou!! Alternativa correta é a letra B')
def open():
    newWindow = Tk()
#função para a resposta 3

#(2)Aqui criamos uma Label(Texto)
v = StringVar()
Label(janela, textvariable=v, font=("Helvetica",15)).pack(pady=(10,0))
#(3)Aqui criamos uma variável para o texto da Label
v.set("A sacolinha plástica é a grande vilã da sustentabilidade?")

lb = Label(janela, text="Alternativa A:")
lb.place(x=100, y=50)

lbb = Label(janela, text="Alternativa B:")
lbb.place(x=100, y=100)

lbc = Label(janela, text="Alternativa C:")
lbc.place(x=100, y=150)

lbd = Label(janela, text="Alternativa D:")
lbd.place(x=100, y=200)

lbres = Label(janela, text="Selecione a alternativa correta", font=("Arial",15))
lbres.place(x=150, y=240)

botao = Button(janela, text="Avançar", command = open)
botao.pack()
botao.place(x=500, y=360)

#(3)Aqui criamos os botões para as respostas
um = Button(janela, text="A",command=um, font=("Helvetica",20))
dois = Button(janela, text="B",command=dois, font=("Helvetica",20))
tres = Button(janela, text="C",command=tres, font=("Helvetica",20))
quatro = Button(janela, text="D",command=quatro, font=("Helvetica",20))

#(4)Aqui mostramos os botões na tela, e estipulamos o lugar
um.place(x=80, y=290, width=100, height=50)
dois.place(x=180, y=290, width=100, height=50)
tres.place(x=280, y=290, width=100, height=50)
quatro.place(x=380, y=290, width=100, height=50)

janela.mainloop()
