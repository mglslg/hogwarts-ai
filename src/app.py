from flask import Flask
from rest import openai_rest


def create_dev_app():
    app = Flask(__name__)
    openai_rest.init_app(app)
    return app


if __name__ == '__main__':
    dev_app = create_dev_app()
    dev_app.run(debug=True, port=8080)
