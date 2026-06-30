from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    # VULNERABILIDAD XSS REFLEJADO INTENCIONAL:
    # Toma el parámetro 'name' directo de la URL y lo imprime en el navegador sin sanitizar.
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    # VULNERABILIDAD DE CONFIGURACIÓN:
    # Ejecutar con debug=True en producción permite inyección de código.
    app.run(debug=True, host='0.0.0.0', port=5000)