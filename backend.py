# backend.py
import sqlite3
import os
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    plano: str
    senha: str

@dataclass
class Filme:
    titulo: str
    diretor: str
    duracao: int
    ano: int

@dataclass
class Serie:
    titulo: str
    criador: str
    temporadas: int
    episodios: int
    ano_inicio: int

@dataclass
class Documentario:
    titulo: str
    diretor: str
    duracao: int
    ano: int

class BancoDeDados:
    def __init__(self, nome_banco="banco.sqlite"):
        # Define o caminho do banco de dados
        self.nome_banco = os.path.join(os.path.dirname(__file__), nome_banco)
        self.conexao = None

    def conectar(self):
        # Conecta ao banco de dados
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def criar_tabelas(self):
        # Cria as tabelas necessárias para o sistema
        if self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                plano TEXT NOT NULL,
                senha TEXT NOT NULL
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Filme (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                diretor TEXT NOT NULL,
                duracao INTEGER NOT NULL,
                ano INTEGER NOT NULL
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Serie (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                criador TEXT NOT NULL,
                temporadas INTEGER NOT NULL,
                episodios INTEGER NOT NULL,
                ano_inicio INTEGER NOT NULL
            )""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Documentario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                diretor TEXT NOT NULL,
                duracao INTEGER NOT NULL,
                ano INTEGER NOT NULL
            )""")
            self.conexao.commit()
    
    def inserir_dados_iniciais(self):
        # Insere dados iniciais fornecidos na descrição
        cursor = self.conexao.cursor()
        pessoas = [
            Pessoa(nome="Andre", idade=32, plano="basico", senha="Pa1234"),
            Pessoa(nome="Jessica", idade=24, plano="premium", senha="Easy2024"),
            Pessoa(nome="Gabriel", idade=22, plano="basico", senha="life321"),
            Pessoa(nome="Taina", idade=28, plano="basico", senha="wic616")
        ]
        filmes = [
            Filme(titulo="Venon 3", diretor="Pedro Paulo", duracao=120, ano=2024),
            Filme(titulo="Senhor dos Aneis", diretor="Roberto Injusto", duracao=170, ano=2005),
            Filme(titulo="Mestre das Armas", diretor="Nicolas Carlos", duracao=70, ano=2010),
            Filme(titulo="Contraaventores", diretor="Renato Aragão", duracao=120, ano=2024),
            Filme(titulo="Midia Teen", diretor="Jenette McArdi", duracao=60, ano=2024),
            Filme(titulo="Sharkday", diretor="Tom Cavanagh", duracao=40, ano=2014),
        ]

        # Insere dados nas tabelas, garantindo que não haja duplicatas
        for pessoa in pessoas:
            cursor.execute("INSERT OR IGNORE INTO Pessoa (nome, idade, plano, senha) VALUES (?, ?, ?, ?)", 
                           (pessoa.nome, pessoa.idade, pessoa.plano, pessoa.senha))
        for filme in filmes:
            cursor.execute("INSERT OR IGNORE INTO Filme (titulo, diretor, duracao, ano) VALUES (?, ?, ?, ?)", 
                           (filme.titulo, filme.diretor, filme.duracao, filme.ano))
       
        self.conexao.commit()

    def buscar_todos_filmes(self):
        # Retorna uma lista de todos os filmes cadastrados
        filmes = []
        if self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, titulo, diretor FROM Filme")
            filmes = cursor.fetchall()
        return filmes

    def excluir_filme(self, filme_id):
        # Exclui um filme pelo ID
        if self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM Filme WHERE id = ?", (filme_id,))
            self.conexao.commit()

    def validar_usuario(self, nome, senha):
        # Valida um usuário pelo nome e senha
        if self.conexao:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM Pessoa WHERE nome = ? AND senha = ?", (nome, senha))
            return cursor.fetchone() is not None

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados
        if self.conexao:
            self.conexao.close()
