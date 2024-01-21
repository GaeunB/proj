from flask import Flask, send_from_directory
import random

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)