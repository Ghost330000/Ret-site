from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Respostas do chatbot
responses = {
    "oi": "Olá! Como posso te ajudar hoje?",
    "como você está?": "Estou sempre pronto para ajudar!",
    "o que você faz?": "Eu sou um assistente inteligente do site Ret!",
    "tchau": "Até logo! Volte sempre ao Ret!"
}

# Rota do chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get("message", "").lower()
    response = responses.get(user_message, "Desculpe, não entendi. Pode reformular?")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
