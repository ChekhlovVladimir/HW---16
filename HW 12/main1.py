from flask import Flask, send_from_directory, Blueprint

app = Flask(__name__)
profile_blueprint = Blueprint("profile_blueprint", __name__)


@profile_blueprint.route("/profile/<int:user_id>")
def static_dir(user_id):
    return f"я страничка профиля пользователя {user_id}"


app.run()
