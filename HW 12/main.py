from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_json():
    name = request.json.get("name")
    return jsonify({"name_received": name})


app.config['JSON_AS_ASCII'] = False
if __name__ == "__main__":
    app.run()
