''' Calculadora IMC
IMC (Indice de Massa Corporal) serve para verificar se você esta mantendo um peso saudavel.

É calculado usando o peso e a altura de uma pessoa.

O valor calculado indica as seguintes categorias:

Abaixo de Peso = Menor que de 18,5
Normal = maior ou igual a 18.5 e menor que 25
Sobrepeso = Maior que 25 e menor que 30
Obesidade =  Maior ou igual a 30

o Programa solictara o peso e altura de uma pessoal e mostrara a categoria do IMC correspondente.'''

from tkinter import *
from tkinter import ttk

# cores

co0 = '#ffffff'  # Branco
co1 = "#444466"  # Preto
co2 = '#4065a1'  # Azul

pagina = Tk()
pagina.title('')
pagina.geometry('295x230')
pagina.configure(bg=co0)

# Dividindo a pagina em duas partes:

parte_cima = Frame(pagina, width=295, height=50, bg=co0, pady=0, padx=0, relief='flat')
parte_cima.grid(row=0, column=0, sticky=NSEW)

parte_baixo = Frame(pagina, width=295, height=180, bg=co0, pady=0, padx=0, relief='flat')
parte_baixo.grid(row=1, column=0, sticky=NSEW)

# Configurando Parte cima

nome_app = Label(parte_cima, text='Calculadora IMC', width=23, height=1, padx=0, relief='flat', anchor='center',font=('Ivy 16 bold'), bg=co0, fg='black')
nome_app.place(x=0, y=0)

linha_app = Label(parte_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 '),bg=co2, fg='black')
linha_app.place(x=0, y=35)

# Configurando Parte Baixo

peso_l = Label(parte_baixo, text='Informe seu Peso', height=1, padx=0, relief='flat', anchor='center',
               font=('Ivy 10 bold'), bg=co0, fg=co1)
peso_l.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
peso_e = Entry(parte_baixo, relief='solid', width=5, font=('Ivy 10 bold'), justify='center')
peso_e.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

altura_l = Label(parte_baixo, text='Informe sua Altura', height=1, padx=0, relief='flat', anchor='center',
                 font=('Ivy 10 bold'), bg=co0, fg=co1)
altura_l.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
altura_e = Entry(parte_baixo, relief='solid', width=5, font=('Ivy 10 bold'), justify='center')
altura_e.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

resultado_l = Label(parte_baixo, text='---', width=4, height=1, padx=6, pady=12, relief='flat', anchor='center',
                    font=('Ivy 24 bold'), bg=co2, fg=co0)
resultado_l.place(x=190, y=10)

resultado_l_txt = Label(parte_baixo, text='O seu IMC é: abaixo do Peso', width=37, height=1, padx=0, pady=12, relief='flat',
                    anchor='center', font=('Ivy 10 bold'), bg=co0, fg='black')
resultado_l_txt.place(x=0, y=85)

resultado_l_txt = Button(parte_baixo, text='Resultado', width=35, height=1, padx=0, pady=12, relief='flat',
                    anchor='center', font=('Ivy 10 bold'), bg=co2, fg='White')
resultado_l_txt.grid(row=3, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

# Calculos de IMC

peso = 75
altura = 1.7
resultado = peso/altura**2

if resultado < 18.5:
    print('Seu IMC esta abaixo do peso')
elif resultado >= 18.5 and resultado < 25:
    print('Seu IMC é Normal')
elif resultado >=25 and resultado < 30:
    print('Seu IMC é Sobrepeso')
else:
    print('Seu IMC é Obesidade')

pagina.mainloop()
