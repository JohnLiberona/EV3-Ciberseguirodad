from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name', 'mundo')
    return f"Hello, {name}!"


@app.route('/health')
def health():
    return {"status": "ok"}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
