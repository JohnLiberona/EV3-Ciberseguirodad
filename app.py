from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'mundo')
    safe_name = escape(name)
    return f"Hello, {safe_name}!"


@app.route('/health')
def health():
    return {"status": "ok"}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
