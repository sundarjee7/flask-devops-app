from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # simple check (no database needed)
        if username == "admin" and password == "admin":
            return "Login Successful!"
        else:
            return "Invalid Credentials!"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

