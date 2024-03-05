from flask import Flask

from controllers import crawls_blueprint

app = Flask(__name__)

# support multiple controllers
app.register_blueprint(crawls_blueprint, prefix='/crawl')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # Starting the Flask Server

