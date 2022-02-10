from flask import Flask, g
import sqlite3

DATABASE = "blog.bd"
SECRET_KEY = "pudim"


app = Flask(__name__) #nomeia com nome do arq
app.config.from_object(__name__) #pega config do proprio arq

def conectar_bd(): #requisicao de conexao do bd
    return sqlite3.connect(DATABASE)

@app.before_request  #antes de toda requisicao ele vem aqui
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request #fecha requisicao
def fim_requisicao(exc):
    g.bd.close()



@app.route('/')
def exibir_entradas():
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    return str(entradas)