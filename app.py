from flask import Flask, request, jsonify

app = Flask(__name__)

comando_atual = "NADA"   # Comando que o ESP32 vai ler

@app.route('/')
def home():
    return f"<h1>Servidor ESP32 Online!</h1><p>Comando atual: {comando_atual}</p>"

@app.route('/comando')
def get_comando():
    return jsonify({"comando": comando_atual})

@app.route('/enviar', methods=['POST'])
def enviar_comando():
    global comando_atual
    data = request.get_json() or request.form
    if 'comando' in data:
        comando_atual = data['comando']
        print("Novo comando:", comando_atual)
        return jsonify({"status": "ok", "comando": comando_atual})
    return jsonify({"status": "erro"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
