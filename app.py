from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    # Mitiga los warnings reportados por OWASP ZAP:
    response.headers['X-Frame-Options'] = 'DENY'                      # Missing Anti-clickjacking Header [10020]
    response.headers['X-Content-Type-Options'] = 'nosniff'            # X-Content-Type-Options Header Missing [10021]
    response.headers['Content-Security-Policy'] = "default-src 'self'"  # CSP Header Not Set [10038]
    response.headers['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'  # Permissions Policy Header Not Set [10063]
    response.headers.pop('Server', None)                              # Server Leaks Version Information [10036]
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
