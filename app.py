from flask import Flask, render_template, request
from prometheus_client import Counter, generate_latest  # Import Prometheus client

app = Flask(__name__)

# ---------- Prometheus metrics setup ----------
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests')

@app.before_request
def before_request():
    REQUEST_COUNT.inc()  # Increment request count on every request

@app.route('/metrics')
def metrics():
    return generate_latest()  # Expose metrics for Prometheus
# ---------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # simple check (no database needed)
        if username == "admin" and password == "admin":
            return "Login Successful Buddy!"
        else:
            return "Invalid Credentials!"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

