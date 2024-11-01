# frontend.py
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, StringVar, TOP
import tkinter.ttk as ttk
from backend import BancoDeDados, Filme

# Inicialização do banco de dados e inserção de dados iniciais
banco = BancoDeDados()
banco.conectar()
banco.criar_tabelas()
banco.inserir_dados_iniciais()  # Insere dados iniciais fornecidos

# Função para validar login do usuário
def validar_login():
    nome = login_var.get()
    senha = senha_var.get()
    if banco.validar_usuario(nome, senha):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        mostrar_interface_filmes()
    else:
        messagebox.showerror("Erro", "Nome ou senha incorretos!")

# Função para abrir a interface de filmes após o login
def mostrar_interface_filmes():
    login_frame.pack_forget()
    filmes_frame.pack()

# Função para adicionar um filme
def adicionar_filme():
    titulo = titulo_var.get()
    diretor = diretor_var.get()
    duracao = duracao_var.get()
    ano = ano_var.get()
    if titulo and diretor and duracao.isdigit() and ano.isdigit():
        filme = Filme(titulo=titulo, diretor=diretor, duracao=int(duracao), ano=int(ano))
        banco.inserir_filme(filme)
        carregar_filmes()
        # Limpa os campos após a inserção
        titulo_var.set("")
        diretor_var.set("")
        duracao_var.set("")
        ano_var.set("")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos corretamente.")

# Função para excluir um filme selecionado
def excluir_filme():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        filme_id = item['values'][0]
        banco.excluir_filme(filme_id)
        carregar_filmes()
    else:
        messagebox.showwarning("Atenção", "Selecione um filme para excluir.")

# Função para carregar todos os filmes da tabela
def carregar_filmes():
    for i in tree.get_children():
        tree.delete(i)
    filmes = banco.buscar_todos_filmes()
    for filme in filmes:
        tree.insert("", "end", values=filme)

# Configuração da Janela Principal
root = Tk()
root.title("Tela Cheia Locadora")
root.geometry("600x400")

# Variáveis para o Login
login_var = StringVar()
senha_var = StringVar()

# Frame de Login
login_frame = Frame(root)
login_frame.pack()
Label(login_frame, text="Login", font=("Arial", 18)).pack(pady=10)
Label(login_frame, text="Nome:").pack()
Entry(login_frame, textvariable=login_var).pack()
Label(login_frame, text="Senha:").pack()
Entry(login_frame, textvariable=senha_var, show="*").pack()
Button(login_frame, text="Entrar", command=validar_login).pack(pady=10)

# Frame da Gestão de Filmes
filmes_frame = Frame(root)
titulo_var = StringVar()
diretor_var = StringVar()
duracao_var = StringVar()
ano_var = StringVar()

# Título e formulário de inserção de filme
Label(filmes_frame, text="Gestão de Filmes", font=("Arial", 18)).pack(side=TOP, pady=10)
form_frame = Frame(filmes_frame)
form_frame.pack()
Label(form_frame, text="Título:").grid(row=0, column=0)
Entry(form_frame, textvariable=titulo_var).grid(row=0, column=1)
Label(form_frame, text="Diretor:").grid(row=1, column=0)
Entry(form_frame, textvariable=diretor_var).grid(row=1, column=1)
Label(form_frame, text="Duração (min):").grid(row=2, column=0)
Entry(form_frame, textvariable=duracao_var).grid(row=2, column=1)
Label(form_frame, text="Ano:").grid(row=3, column=0)
Entry(form_frame, textvariable=ano_var).grid(row=3, column=1)

# Botões de adicionar e excluir filme
Button(form_frame, text="Adicionar Filme", command=adicionar_filme).grid(row=4, column=0, pady=10)
Button(form_frame, text="Excluir Filme", command=excluir_filme).grid(row=4, column=1, pady=10)

# Tabela de Filmes
tree = ttk.Treeview(filmes_frame, columns=("ID", "Título", "Diretor"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Título", text="Título")
tree.heading("Diretor", text="Diretor")
tree.pack()
carregar_filmes()  # Carrega filmes ao iniciar a interface

root.mainloop()
