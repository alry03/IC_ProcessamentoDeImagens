from tkinter import *

def mouseClique(evento):
    print("---------------------------------------")
    print(f"Clique em: ({str(evento.x)},{str(evento.y)})")

def mouseRelease(evento):
    print(f"Release em: ({str(evento.x)},{str(evento.y)})")
    print("---------------------------------------")

janela = Tk()
#Dá nome a GUI
janela.title("Mouse tracker")
#Instrução do que deve ser feito
instrucao = Label(janela, text= 'Clique com o mouse para saber as coordenadas do clique e release.',
                  font=("Arial", 12), pady=10)
instrucao.pack()
#Exibe as coordenadas do cursor do mouse no clique
janela.bind("<Button-1>", mouseClique)
#Exibe as coordenadas do cursor do mouse ao soltar o clique
janela.bind("<ButtonRelease>", mouseRelease)
janela.mainloop()