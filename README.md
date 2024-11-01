# RAD_py
Projeto aplicações rápidas em python
# Tela Cheia Locadora ( Locadora de Filmes)

Este é um projeto de uma aplicação de locadora de filmes, que permite a gestão de usuários e filmes usando uma interface gráfica simples em Python com Tkinter e um banco de dados SQLite.

## Requisitos

Para rodar este projeto, você precisará do seguinte:

- Python 3.x
- Bibliotecas:
  - `tkinter` (geralmente já incluído na instalação do Python)
  - `sqlite3` (também já incluído na instalação do Python)
  
### Instalação

1. **Copie os códigos :**
   Copie os códigos e o banco de dados para sua máquina.

2. **Certifique-se de que o Python esteja instalado:**
  

3. **Execute a aplicação:**
  

## Funcionalidades Principais

A aplicação oferece as seguintes funcionalidades:

1. **Login de Usuário:**
   - Os usuários podem fazer login na aplicação com seu nome e senha. 
   - As credenciais de exemplo são:
     - Andre / Pa1234
     - Jessica / Easy2024
     - Gabriel / life321
     - Taina / wic616

2. **Gestão de Filmes:**
   - Após o login bem-sucedido, os usuários podem visualizar uma lista de filmes.
   - Os filmes são armazenados em um banco de dados SQLite e incluem informações como título, diretor, duração e ano de lançamento.
   
3. **Adicionar Filmes:**
   - Os usuários podem adicionar novos filmes à lista, preenchendo um formulário com as informações do filme.

4. **Excluir Filmes:**
   - Os usuários podem excluir filmes da lista selecionando um filme e clicando no botão de exclusão.

## Estrutura do Projeto

- `frontend.py`: Contém a interface gráfica da aplicação, utilizando Tkinter.
- `backend.py`: Implementa a lógica de gerenciamento de dados, incluindo a conexão com o banco de dados SQLite e as operações CRUD (Criar, Ler, Atualizar, Excluir).
- `banco.sqlite`: O arquivo do banco de dados gerado automaticamente, que armazena informações sobre usuários e filmes.


## Licença

Este projeto é de código aberto e pode ser utilizado e modificado conforme a [Licença MIT](LICENSE).
