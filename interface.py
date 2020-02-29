from tkinter import *
janela = Tk()
def exit():
          janela.destroy()

label= Label(janela,text="Olá, Humanos!!!!!",bg="green",fg="yellow",font="Arial 12")
label.place(x=200,y=250)
janela.geometry("500x500")
janela['bg']="pink"
janela.title("Primeira interface")
inp1=Entry(janela)
inp1.place(x=200,y=280)
inp2=Entry(janela)
inp2.place(x=200,y=310)
bt=Button(janela,text="Sair!",command=exit)
bt.place(x=250,y=400)

"""------------------------------------------------------------------"""

janela.mainloop()

