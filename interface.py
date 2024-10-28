from tkinter import Tk, Frame, Label, Entry, Button, Scrollbar, HORIZONTAL, VERTICAL, RIGHT, LEFT, BOTTOM, Y, X, W, NO, TOP, StringVar, SOLID
import tkinter.ttk as ttk

# Configuração Inicial da Janela
root = Tk()
root.title("Locadora de Filmes")
root.geometry("800x500")
root.resizable(0, 0)

# Variáveis para Campos de Entrada
titulo_var = StringVar()
genero_var = StringVar()
ano_var = StringVar()
duracao_var = StringVar()

# Frame Superior com Título
frame_top = Frame(root, width=800, bd=1, relief=SOLID)
frame_top.pack(side=TOP)
Label(frame_top, text="Locadora de Filmes", font=('Arial', 18)).pack(side=TOP)

# Frame para Formulário de Inserção de Dados
frame_form = Frame(root, width=800)
frame_form.pack(side=TOP, pady=10)

Label(frame_form, text="Título:").grid(row=0, column=0, padx=5, pady=5)
Entry(frame_form, textvariable=titulo_var).grid(row=0, column=1, padx=5, pady=5)

Label(frame_form, text="Gênero:").grid(row=1, column=0, padx=5, pady=5)
Entry(frame_form, textvariable=genero_var).grid(row=1, column=1, padx=5, pady=5)

Label(frame_form, text="Ano:").grid(row=2, column=0, padx=5, pady=5)
Entry(frame_form, textvariable=ano_var).grid(row=2, column=1, padx=5, pady=5)

Label(frame_form, text="Duração (min):").grid(row=3, column=0, padx=5, pady=5)
Entry(frame_form, textvariable=duracao_var).grid(row=3, column=1, padx=5, pady=5)

# Botões
Button(frame_form, text="Adicionar Filme").grid(row=4, column=0, columnspan=2, pady=10)
Button(frame_form, text="Editar Filme").grid(row=4, column=2, columnspan=2, pady=10)
Button(frame_form, text="Excluir Filme").grid(row=4, column=4, columnspan=2, pady=10)

# Frame para Tabela de Filmes
frame_table = Frame(root, width=800)
frame_table.pack(side=TOP)

# Scrollbars e Treeview para a Tabela
scrollbarx = Scrollbar(frame_table, orient=HORIZONTAL)
scrollbary = Scrollbar(frame_table, orient=VERTICAL)
tree = ttk.Treeview(
    frame_table, 
    columns=("ID", "Título", "Gênero", "Ano", "Duração"), 
    selectmode="extended", 
    height=10, 
    yscrollcommand=scrollbary.set, 
    xscrollcommand=scrollbarx.set
)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

# Configuração das Colunas da Tabela
tree.heading('ID', text="ID", anchor=W)
tree.heading('Título', text="Título", anchor=W)
tree.heading('Gênero', text="Gênero", anchor=W)
tree.heading('Ano', text="Ano", anchor=W)
tree.heading('Duração', text="Duração", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=30, width=50)
tree.column('#2', stretch=NO, minwidth=200, width=200)
tree.column('#3', stretch=NO, minwidth=100, width=100)
tree.column('#4', stretch=NO, minwidth=100, width=100)

tree.pack()

# Inicializar Janela
root.mainloop()
