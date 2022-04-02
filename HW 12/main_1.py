from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def page_index():
    if request.method == "POST":
        file = request.files["file"]
        file.save(f"./uploads/{file.filename}")
        return "Загружено"

    return render_template("main_1.html")


app.run()
