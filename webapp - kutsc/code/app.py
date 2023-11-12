from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register")
def contact():
    return render_template("register.html")

@app.route("/login")
def datasets():
    return render_template("login.html")

@app.route("/account")
def contact():
    return render_template("account.html")

@app.route("/accountsettings")
def contact():
    return render_template("accountsettings.html")

@app.route("/simplesearch")
def contact():
    return render_template("simplesearch.html")

@app.route("/advancedsearch")
def contact():
    return render_template("advancedsearch.html")

@app.route("/cart")
def contact():
    return render_template("cart.html")

@app.route("/checkout")
def contact():
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)