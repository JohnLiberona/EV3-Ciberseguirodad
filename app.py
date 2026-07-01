from flask import Flask, request
from markupsafe import escape
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # expone automáticamente /metrics


@app.after_request
def add_security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'
    response.headers.pop('Server', None)
    return response


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
