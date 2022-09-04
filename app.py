from flask import Flask, jsonify
import trailer

app = Flask(__name__)
st = 'adad'
print(st[:2])
@app.route("/<string:s>")
def hello_world(s):
    if s[:2]=='tt':
        t= trailer.getTrailer(s)
    else:
        return jsonify({'message':'enter valid imdb id'})
    if not t=='failed':
        return jsonify({'url':t})
    else:
        return jsonify({'request':'failed'})

if __name__ == "__main__":
    app.run(debug=False)