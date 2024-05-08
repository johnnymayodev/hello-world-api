# Hello World API

This is a simple API that returns a hello world message.

## Author

- [johnnymayodev](https://github.com/johnnymayodev)

## Contributing

Please feel free to fork this repo and contribute by submitting a pull request to enhance the functionalities.

##### [GitHub's Contributing to a Project Guide](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)

## How to run

Notice: The following commands are for Unix-based systems (they work on my ZorinOS box and macOS laptop). Please adjust the commands accordingly if you are using a different operating system (e.g. Windows).

1. Clone the repository and navigate to the project directory.

2. Create a new virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python app.py
```

### Command Line Arguments

- `--debug` runs the api in debug mode

- `--port 8090` makes the api run on port 8090

- `--version 42` changes the api route to `/api/v42/hello` effectively changing the version of the api

## Testing the API

To run the tests, execute the following command:

```bash
python3 tester.py
```

### Command Line Arguments

- `--port 8090` makes the script test port 8090

- `--version 42` changes the script test route to `/api/v42/hello` effectively changing the version of the api

- `--live` makes the script test the live api instead of the local one

## License

This package is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/mit).
