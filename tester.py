import sys
import requests  # type: ignore

# Set the default values (these can be changed with command line arguments)
PORT = 5000 if "--port" not in sys.argv else int(sys.argv[sys.argv.index("--port") + 1])
VERSION = 1 if "--version" not in sys.argv else int(sys.argv[sys.argv.index("--version") + 1])
ROUTE = "/hello" if "--route" not in sys.argv else sys.argv[sys.argv.index("--route") + 1]

# Piece together the path using the version and route
PATH = f"/V{VERSION}{ROUTE}"

# Set the URL based on whether the --live flag is present
URL = (
    f"https://hello.johnnymayo.com/api{PATH}"
    if "--live" in sys.argv
    else f"http://localhost:{PORT}{PATH}"
)


def call_api(url):
    print(f"Calling API at {url}")
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    print(call_api(URL))
