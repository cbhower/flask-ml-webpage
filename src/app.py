from flask import Flask, redirect, url_for, render_template, request
import pickle

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")


@app.route('/models', methods=['POST', 'GET'])
def models():
    if request.method == 'POST':
        features = [int(feature) for feature in request.form.values()]
        return render_template("models.html", prediction_text=features)
    else:
        return render_template("models.html")


@app.route("/music")
def music():
    return render_template("music.html")


@app.route('/simulations', methods=['POST', 'GET'])
def simulations():
    if request.method == 'POST':
        features = [int(feature) for feature in request.form.values()]
        return render_template("simulations.html", prediction_text=features)
    else:
        return render_template("simulations.html")


if __name__ == "__main__":
    app.run(debug=True)
