from flask import Flask
from controllers.register_face import register_face

app = Flask(__name__)

@app.route('/api/register', methods=['POST'])
def register():
    return register_face()