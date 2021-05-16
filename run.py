#!flask/bin/python
from application.main import app


if __name__ == '__main__':
    app.run(debug=False, port=5000)