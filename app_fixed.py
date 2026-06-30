from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello')
def hello():
    # Antes: f"Hello, {name}!"  -> permitía XSS reflejado
    # (ej: /hello?name=<script>alert(1)</script>)
    # Ahora: escape() neutraliza < > " ' & antes de insertarlos en el HTML
    name = request.args.get('name', 'mundo')
    safe_name = escape(name)
    return f"Hello, {safe_name}!"


@app.route('/health')
def health():
    return {"status": "ok"}, 200


if __name__ == '__main__':
    # debug=False en la versión corregida: debug=True expone el
    # debugger interactivo de Werkzeug, que permite ejecución remota
    # de código si el endpoint queda accesible.
    app.run(host='0.0.0.0', port=5000, debug=False)
