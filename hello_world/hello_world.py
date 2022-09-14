from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Hrishikesh Thula'


app.run(host='0.0.0.0', port=80)
