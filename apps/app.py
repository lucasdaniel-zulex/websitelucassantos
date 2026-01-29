from flask import Flask, render_template, request
import mysql.connector
import os
import time

app = Flask(__name__)

# Configuração do Banco (Pega do docker-compose)
def get_db_connection():
    # Loop de tentativa simples para esperar o MySQL iniciar
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=os.environ.get('DB_HOST'),
                user=os.environ.get('DB_USER'),
                password=os.environ.get('DB_PASSWORD'),
                database=os.environ.get('DB_NAME')
            )
            return conn
        except mysql.connector.Error as err:
            print(f"Banco ainda não está pronto... tentando novamente em 5s. Erro: {err}")
            time.sleep(5)
            retries -= 1
    return None

# Inicializa a tabela ao abrir o app
def init_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                email VARCHAR(100)
            )
        ''')
        conn.commit()
        conn.close()

# Inicia o banco na primeira execução
with app.app_context():
    init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem = ''
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome, email))
            conn.commit()
            conn.close()
            mensagem = 'Usuário cadastrado com sucesso!'
        else:
            mensagem = 'Erro ao conectar no banco.'

    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)