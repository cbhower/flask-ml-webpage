from flask import Flask, redirect, url_for, render_template, request
import pickle

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")


@app.route('/models', methods=['POST', 'GET'])
def models():
    if request.method == 'POST':
        model = request.form["model"]
        return redirect(url_for("model", name=model))
    else:
        return render_template("models.html")


@app.route("/<name>")
def model(name):
    return f"{name} page"


if __name__ == "__main__":
    app.run(debug=True)
