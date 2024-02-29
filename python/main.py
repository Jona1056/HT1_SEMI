from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "Instancia": "Instancia #1 - API #1",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Jonatan Garcia - 202000424"
    }
    return jsonify(data)

@app.route('/check')
def check():
   return 'OK', 200
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
