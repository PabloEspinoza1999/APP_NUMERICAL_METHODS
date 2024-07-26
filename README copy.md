# APP_NUMERICAL-METHODS

Setup the environment:

1. Install docker on the machine.
2. Copy the file `.env.example` to `.env` file name.
3. Run `docker compose up -d` to start the app.
4. Optionally run `pip install -r requirements.txt` command (require python +3.10)
5. Open `http://127.0.0.1` in a browser.cls

### Adding dependencies

If you are working in the source code and requires to add a new dependencies, please do the following:

1. Install the required dependency.
2. Run `pip freeze > requirements.txt` tp include it at the project.
