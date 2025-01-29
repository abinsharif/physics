from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_page():
    return send_from_directory('.', 'physics.html')

if __name__ == '__main__':
    app.run(host='192.168.0.106', port=1234, debug=True)
