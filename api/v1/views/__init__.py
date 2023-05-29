#!/usr/bin/python3
from flask import Flask
from flask import Blueprint
from api.v1.views import *

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app.register_blueprint(app_views)

if __name__ == '__main__':
    import os

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)

