from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Conectar ao banco de dados
DB_PATH = "ret_database.db"

def query_db(query, args=(), one=False):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return (result[0] if result else None) if one else result

# Rota para cadastro de usuários
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    query_db("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
             (data['username'], data['password'], data['email']))
    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

# Rota para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = query_db("SELECT * FROM users WHERE username = ? AND password = ?", 
                    (data['username'], data['password']), one=True)
    if user:
        return jsonify({"message": "Login bem-sucedido!"}), 200
    return jsonify({"message": "Credenciais inválidas!"}), 401

# Rota para postar conteúdo na rede social
@app.route('/post', methods=['POST'])
def post():
    data = request.json
    query_db("INSERT INTO posts (user_id, content) VALUES (?, ?)", 
             (data['user_id'], data['content']))
    return jsonify({"message": "Postagem criada com sucesso!"}), 201

# Rota para adicionar produtos no marketplace
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    query_db("INSERT INTO marketplace (seller_id, product_name, price, description) VALUES (?, ?, ?, ?)", 
             (data['seller_id'], data['product_name'], data['price'], data['description']))
    return jsonify({"message": "Produto adicionado ao marketplace!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
