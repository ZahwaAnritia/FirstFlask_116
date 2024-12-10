from flask import Flask #ambil liberary

app = Flask(__name__) #nama project

@app.route("/")
def hello_world():
    return "<div>Hello, World!</div>"

@app.route('/salam')
def hello():
    return "Assalamu'alaikum!"

if  __name__ == "__main__":
    app.run(debug=True)
