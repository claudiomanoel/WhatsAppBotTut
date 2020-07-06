import sqlite3

def get_pizzas():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT id, nome, preco_pequeno, preco_medio, preco_grande, media_url from PIZZA')
    data = cur.fetchall()
    con.close()
    return data