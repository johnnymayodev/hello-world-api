import requests # type: ignore

HOST = 'localhost:'
PORT = 5000
ROUTE = '/hello'

URL = f'http://{HOST}{PORT}{ROUTE}'

def call_api(url):
    print(f'Calling API at {url}')
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    print(call_api(URL))