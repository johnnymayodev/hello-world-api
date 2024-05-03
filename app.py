import sys
import time
from flask import Flask, jsonify  # type: ignore

VERSION = 1
PATH = f"/api/V{VERSION}"

# Colors for the console
WHITE = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

DEBUG = False
PORT = 5000

"""
Command Line Arguments:
--debug             : Enable debug mode
--port [PORT]       : Set port number

Example:
python app.py --debug --port 5000
This will run the app in debug mode and on port 5000
"""

valid_args = ["--debug", "--port"]
args = sys.argv
if len(args) > 1:  # Check if there are any arguments
    for arg in valid_args:  # Check if the arguments are valid
        if arg in args:  # If the argument is in the list of arguments
            if arg == "--debug":
                DEBUG = True
                print(f"{GREEN}Debug mode enabled{WHITE}")
            elif arg == "--port":
                try:
                    PORT = int(args[args.index("--port") + 1])
                    print(f"{GREEN}Port number set to {PORT}{WHITE}")
                except ValueError:
                    print(
                        f"{RED}ERROR:{WHITE} Invalid port number of {YELLOW}{args[args.index('--port') + 1]}{WHITE}"
                    )
                    exit(1)


print(f"{YELLOW}Starting Flask Server...{WHITE}")
time.sleep(1)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<a href='./api/V1/hello'>API</a>"


@app.route(f"{PATH}/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello World!"})


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
