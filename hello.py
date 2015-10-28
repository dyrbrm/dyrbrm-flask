from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is a test page!!"

@app.route("/test/")
def test():
    return "Test environment"

@app.route("/prod/")
def prod():
    return "Production environment"

@app.route("/login")
def login(): pass

@app.route("/user/<username>")
def profile(username): pass

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('profile', username='Steven Wong')

if __name__ == "__main__":
    app.debug = True
    app.run()
