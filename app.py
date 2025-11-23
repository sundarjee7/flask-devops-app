from flask import Flask, render_template, request, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# ---------- Prometheus metrics setup ----------
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total number of HTTP requests served'
)

@app.before_request
def before_request():
    # Prevent Prometheus scrapes from incrementing the counter
    if request.path != "/metrics":
        REQUEST_COUNT.inc()

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
# ----------------------------------------------

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin":
            return "Login Successful Buddy!"
        else:
            return "Invalid Credentials!"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

