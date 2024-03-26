from tkinter import*
import tkinter.messagebox
import customtkinter as ctk

janela=ctk.CTk()
janela.geometry("440x300")
janela.resizable(False,False)
janela.title("SELETOR DE CORES")
janela.configure(background="white")



# image
frame_color=ctk.CTkFrame(janela, width=200, height=200,bg_color="white")
frame_color.place(x=0,y=0)
tela = Label(janela, width=200, height=200, bd=1)
tela.grid(row=0, column=0)


# seletor de cor
frame_rgb=ctk.CTkFrame(janela,width=240,height=200)
frame_rgb.place(x=200,y=0)


#resultado da cor
frame_resultado=ctk.CTkFrame(janela,width=440,height=100)
frame_resultado.place(x=0,y=200)


# funcao ESCALAR
def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()

    rgb = f'{r}, {g}, {b}'

    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    #alterando a cor do fundo da tela
    tela['bg'] = hexadecimal

    # alterando a entry
    e_cor.delete(0,END)
    e_cor.insert(0,hexadecimal)


# funcao clicar 
def copiar():
    # informar
    tkinter.messagebox.showinfo('Cor', "a cor foi copiada")

    # serve para criar botao copiar
    clip = ctk.CTk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()




 #configurando o frame_rgb (seletor de cor)
l_red = ctk.CTkLabel(frame_rgb,text='Red', width=7,font=("Time New Roman", 18, "bold"))
l_red.place(x=10,y=10)
s_red=Scale(frame_rgb, from_=0,command=escala, to=255, length=150, bg="Black", fg="red", orient=HORIZONTAL)
s_red.place(x=80,y=10)

l_green = ctk.CTkLabel(frame_rgb,text='Green', width=7,  font=("Time New Roman", 18, "bold"))
l_green.place(x=10,y=75)
s_green=Scale(frame_rgb, from_=0,command=escala, to=255, length=150, bg="Black", fg="green", orient=HORIZONTAL)
s_green.place(x=80,y=75)

l_blue = ctk.CTkLabel(frame_rgb,text='Blue', width=7, font=("Time New Roman", 18, "bold"))
l_blue.place(x=10,y=140)
s_blue=Scale(frame_rgb, from_=0,command=escala, to=255, length=150, bg="Black", fg="blue", orient=HORIZONTAL)
s_blue.place(x=80,y=140)




# configurando o frame_resultado( resultado da cor)
l_rgb = ctk.CTkLabel(frame_resultado,text='CÓDIGO HEXADECIMAL :',font=("Century Gothic bold",14))
l_rgb.place(x=0,y=18)

#entry
e_cor = Entry(frame_resultado, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
e_cor.place(x=170,y=20)

# botao copiar
b_copiar = ctk.CTkButton(frame_resultado,command=copiar, text='Copiar', font=("Century Gothic bold",16),corner_radius=20)
b_copiar.place(x=290,y=15)

# app nome
l_app_nome = ctk.CTkLabel(frame_resultado,text='Seletor de Cores', font=("Century Gothic bold",16))
l_app_nome.place(x=150,y=60)



janela.mainloop()
