import sys
import requests  # type: ignore

"""
Command Line Arguments:
--port [PORT]       : Set port number
--version [VERSION] : Set API version
--route [ROUTE]     : Set API route
--live              : Use the live API (https://hello.johnnymayo.com/api/V1/hello as of May 7th, 2024)
"""


# Set the default values (these can be changed with command line arguments)
PORT = 5000 if "--port" not in sys.argv else int(sys.argv[sys.argv.index("--port") + 1])
VERSION = (
    1 if "--version" not in sys.argv else int(sys.argv[sys.argv.index("--version") + 1])
)
ROUTE = (
    "/hello" if "--route" not in sys.argv else sys.argv[sys.argv.index("--route") + 1]
)

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


# Piece together the path using the version and route
PATH = f"/V{VERSION}{ROUTE}"

# Set the URL based on whether the --live flag is present
URL = (
    f"https://hello.johnnymayo.com/api{PATH}"
    if "--live" in sys.argv
    else f"http://localhost:{PORT}{PATH}"
)


def call_api(url):
    print(f"{YELLOW}Calling API...{WHITE}")
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error calling API:{WHITE} {e}")
        sys.exit(1)

    return response


if __name__ == "__main__":
    res = call_api(URL)
    if res.status_code == 200:
        print(f"{GREEN}API call successful!{WHITE}")
        print(res.json())
    else:
        print(f"{RED}API returned status code {res.status_code}.{WHITE}")
        print(res.text)
