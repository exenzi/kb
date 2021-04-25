from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=os.getenv('PORT'))