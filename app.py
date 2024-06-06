import sys
import time
from flask import Flask, jsonify  # type: ignore

"""
Command Line Arguments:
--debug             : Enable debug mode
--port [PORT]       : Set port number
--version [VERSION] : Set API version
"""

DEBUG = False if "--debug" not in sys.argv else True
PORT = 5000 if "--port" not in sys.argv else int(sys.argv[sys.argv.index("--port") + 1])
VERSION = (
    1 if "--version" not in sys.argv else sys.argv[sys.argv.index("--version") + 1]
)
PATH = f"/api/V{VERSION}"

# Colors for the console
WHITE = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

# Check the variables
try:
    assert isinstance(PORT, int)
    assert 1024 < PORT < 65536
except AssertionError:
    print(
        f"{RED}Invalid port number. Please provide a number between 1024 and 65536.{WHITE}"
    )
    sys.exit(1)

try:
    assert isinstance(VERSION, int)
    assert VERSION > 0
except AssertionError:
    print(f"{RED}Invalid API version. Please provide a positive integer.{WHITE}")
    sys.exit(1)


print(f"{GREEN}Starting Flask Server...{WHITE}")
time.sleep(1)

# Initialize the Flask app
app = Flask(__name__)


# Routes
@app.route("/", methods=["GET"])
def index():
    return "<a href='./api/V1/hello'>API</a>"


# API Routes
@app.route(f"{PATH}/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World!"})


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
