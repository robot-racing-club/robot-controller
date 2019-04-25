from flask import Flask, render_template
from flask_socketio import SocketIO

from motor_controller import forward, backward

app = Flask(__name__)
app.config["SECRET_KEY"] = "A_VERY_SECRET_KEY"
socketio = SocketIO(app)


@app.route("/")
def controller():
    return render_template("controller.html")


def messageReceived(methods=["GET", "POST"]):
    print("message was received!!!")


@socketio.on("command")
def handle_command_event(json, methods=["GET", "POST"]):
    print("received event: " + str(json))
    socketio.emit("response", json, callback=messageReceived)


if __name__ == "__main__":
    socketio.run(app, debug=True)
