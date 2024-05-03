import requests # type: ignore

HOST = 'localhost:'
PORT = 5000
VERSION = 1
ROUTE = '/hello'
PATH = f'/V{VERSION}{ROUTE}'

URL = f'http://{HOST}{PORT}{PATH}'

def call_api(url):
    print(f'Calling API at {url}')
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    print(call_api(URL))