from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK', 200

@app.route('/check')
def check():
    data = {
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Jonatan Garcia - 202000424"
    }
    return jsonify(data)
    


if __name__ == '__main__':
    app.run(port=8081)
