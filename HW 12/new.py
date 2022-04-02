from flask import Flask, render_template, request

app = Flask(__name__)

LOGIN = "chekhlov"
PASSWORD = "chekhlov"

@app.route('/')
def page_index():
    return render_template("main.html")


@app.route('/login', methods=["POST"])
def page_form():
    user_login = request.form.get("username")
    user_password = request.form.get("password")
    if user_login == LOGIN and user_password == PASSWORD:
        return " enter"
    return "denied"
app.run()