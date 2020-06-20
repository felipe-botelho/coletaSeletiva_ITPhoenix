import tkinter
from tkinter import *
from tkinter.ttk import Progressbar
import pygame
from pygame import *
import random
import webbrowser

#ativação do áudio
pygame.mixer.init(44100, -16, 2, 2048)
audio = pygame.mixer.Sound('audio/audio.ogg')

url = "https://drive.google.com/file/d/1HNyMzCpn7y2fejYQrOFupuR-0jpjBtnV/view?usp=sharing"

perguntas = [
    "O que é coleta seletiva? ",
    "O que é reciclagem? ",
    "O que significa os 3Rs da sustentabilidade? ",
    "Qual a cor da lixeira de PLÁSTICO? ",
    "Qual a cor da lixeira de PAPEL? ",

]

respostas_opcoes = [
    ["Nome dado ao recolhimento do lixo feito pelas cooperativas e catadores", "Processo de separação, recolhimento e reaproveitamento de resíduos por meio da reciclagem ", "Lugar para onde é destinado todo o lixo produzido",],
    ["Transformação de materiais usados em novos produtos para consumo", "Separar todo o tipo de material em lixos recicláveis", "Jogar fora todo o lixo produzido",],
    ["Reduzir, Reaproveitar e Reciclar", "Reduzir, Reutilizar e Reciclar", "Reduzir, Reutilizar e Replantar",],
    ["Amarelo", "Verde", "Vermelha",],
    ["Azul", "Verde", "Amarelo",],
]

respostas_corretas = [1,0,1,2,0,]

resposta_usuario = []

indices = []
def gen():
    global indices
    while(len(indices) < 4):
        x = random.randint(0,4)
        if x in indices:
            continue
        else:
            indices.append(x)

def botaoRespostas():
    lblTxt = Label(
        root,
        font=("Calibri", 14),
        text='Para consultar as respostas corretas, acesse o botão abaixo:',
        background="#ffffff",
    )
    lblTxt.pack(pady=(30, 0))

    btnUrl = Button(
        root,
        text="✓ Respostas ✓",
        font=("Calibri", 14),
        relief=FLAT,
        border=0,
        command=lambda: webbrowser.open(url)
    )
    btnUrl.pack(pady=30)

def mostrar_resultado(resultado):
    root.geometry("700x600+350+30")
    lblPerguntas.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    labelimagem = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimagem.pack(pady=(110,30))
    labelresultadotexto = Label(
        root,
        font = ("Calibri", 20),
        background = "#ffffff",
    )
    labelresultadotexto.pack()

    if resultado >= 15:
        img = PhotoImage(file="imagens/excelent.png")
        labelimagem.configure(image=img)
        labelimagem.image = img
        labelresultadotexto.configure(text="PARABÉNS! Você acertou mais de 80% das perguntas. \n Você é um expert e "
                                           "merece uma medalha quando o \n assunto é coleta seletiva.")
    elif (resultado <= 15 and resultado < 20):
        img = PhotoImage(file="imagens/continue.png")
        labelimagem.configure(image=img)
        labelimagem.image = img
        labelresultadotexto.configure(text="Bom trabalho, mas você pode melhorar.")
        botaoRespostas()
        #jogarNovamente()
    else:
        img = PhotoImage(file="imagens/help.gif")
        labelimagem.configure(image=img)
        labelimagem.image = img
        labelresultadotexto.configure(text="Você precisa estudar mais!")
        botaoRespostas()
        #jogarNovamente()

def calc():
    global indices,resposta_usuario,respostas_corretas
    x = 0
    resultado = 0
    for i in indices:
        if resposta_usuario[x] == respostas_corretas[i]:
            resultado = resultado + 5
        x += 1
    print(resultado)
    mostrar_resultado(resultado)

perg = 1
def selected():
    global radiovar,resposta_usuario
    global lblPerguntas,r1,r2,r3
    global perg
    x = radiovar.get()
    resposta_usuario.append(x)
    radiovar.set(-1)
    if perg < 4:
        lblPerguntas.config(text= perguntas[indices[perg]])
        r1['text'] = respostas_opcoes[indices[perg]][0]
        r2['text'] = respostas_opcoes[indices[perg]][1]
        r3['text'] = respostas_opcoes[indices[perg]][2]
        perg += 1
    else:
        print(indices)
        print(resposta_usuario)
        calc()

def iniciarJogo():
    root.geometry("700x350+350+150")
    audio.play()
    global lblPerguntas,r1,r2,r3
    lblPerguntas = Label(
        root,
        text = perguntas[indices[0]],
        font = ("Calibri",24),
        width = 500,
        justify ="center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblPerguntas.pack(pady=(50,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = respostas_opcoes[indices[0]][0],
        font = ("Calibri", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = respostas_opcoes[indices[0]][1],
        font = ("Calibri", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = respostas_opcoes[indices[0]][2],
        font = ("Calibri", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

def iniciarPressionado():
    labelimagem.destroy()
    labeltexto.destroy()
    lblInstrucoes.destroy()
    lblRegras.destroy()
    btnIniciar.destroy()
    gen()
    iniciarJogo()

def reiniciar():
    labeltexto.destroy()
    labelimagem.destroy()
    iniciarJogo()

'''def jogarNovamente():
    btnPlay = Button(
        root,
        text="Jogar novamente?",
        font=("Calibri", 14),
        relief=FLAT,
        border=0,
        command=reiniciar,
    )
    btnPlay.pack(pady=10)'''

root = tkinter.Tk()
root.title("Coleta Seletiva")
root.geometry("700x600+350+30")
root.config(background="#ffffff")
root.resizable(0,0)

img1 = PhotoImage(file="imagens/icon1.png")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file="imagens/coleta.png"))

labelimagem = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimagem.pack(pady=(40,0))

labeltexto = Label(
    root,
    text="Você sabe tudo sobre coleta seletiva?",
    font=("Calibri", 24, "bold"),
    background="#ffffff",
)
labeltexto.pack(pady=(20,35))

img2 = PhotoImage(file="imagens/start.png")

btnIniciar = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = iniciarPressionado,
)
btnIniciar.pack()

lblInstrucoes = Label(
    root,
    text = "Leia as regras e\n aperte START quando estiver pronto.",
    background = "#ffffff",
    font = ("Calibri", 14),
    justify = "center",
)
lblInstrucoes.pack(pady=(10,30))

lblRegras = Label(
    root,
    text = "Esse quiz contém 30 perguntas sobre coleta seletiva.\n "
           "Uma vez selecionada a resposta você não poderá voltar atrás. \n"
           "Pense bem antes de responder!",
    width = 100,
    font = ("Calibri", 14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRegras.pack()

root.mainloop()
