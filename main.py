import tkinter as tk
import datetime as dt
from tkinter import ttk

lista_tipos = ['caderno', 'lapis', 'Caneta', 'borracha']


# função de inserção

def inserir():
    descricao = entry_descricao.get()
    tipo = cb_selecionar.get()
    quant = entry_quant.get()


janela = tk.Tk()

janela.title('Cadastro de produtos')

# Descrição
lbl_descricao = tk.Label(text='Descrição dos materiais')
lbl_descricao.grid(row=1, column=0, pady=10, padx=10, columnspan=1, sticky='nswe')

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, pady=10, padx=10, columnspan=4, sticky='nswe')

# Tipo
tipo_material = tk.Label(text='Tipo de material')
tipo_material.grid(row=3, column=0, pady=10, padx=10, columnspan=1, sticky='nswe', )

cb_selecionar = ttk.Combobox(values=lista_tipos)
cb_selecionar.grid(row=3, column=2, pady=10, padx=10, columnspan=2, sticky='nswe')

# Quantidade
lbl_quant = tk.Label(text='Quantidade dos materiais')
lbl_quant.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky='nswe')

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, pady=10, padx=10, columnspan=4, sticky='nswe')

# Botao
btn_cadastrar = tk.Button(text='Cadastrar')
btn_cadastrar.grid(row=6, column=0, pady=10, padx=10, columnspan=1, sticky='nswe')

janela.mainloop()
