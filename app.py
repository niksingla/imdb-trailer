from flask import Flask, jsonify
import trailer

app = Flask(__name__)

@app.route("/")
def hello_world():
    t= trailer.getTrailer()
    if not t=='failed':
        return jsonify({'url':t})
    else:
        return jsonify({'request':'failed'})

if __name__ == "__main__":
    app.run(debug=True)