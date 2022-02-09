from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello flask on readmi" \
           "<br><h2>运行flask提供的调试服务器"

if __name__ == '__main__':
    app.run(debug=True)