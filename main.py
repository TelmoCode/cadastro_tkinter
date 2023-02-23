import tkinter as tk
import datetime as dt
from tkinter import ttk

lista_tipos = ['caderno','lapis','Caneta','borracha']

janela = tk.Tk()

janela.title('Cadastro de produtos')

lbl_descricao = tk.Label(text='Descrição dos materiais')
lbl_descricao.grid(row=1, column=0, pady=10, padx=10, columnspan=4, sticky='nswe')

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, pady=10, padx=10, columnspan=4, sticky='nswe')

tipo_material = tk.Label(text='Tipo de material')
tipo_material.grid(row=3, column=0, pady=10, padx=10, columnspan=2, sticky='nswe')

cb_selecionar = ttk.Combobox(values=lista_tipos)
cb_selecionar.grid(row=3, column=2, pady=10, padx=10, columnspan=2, sticky='nswe')

janela.mainloop()