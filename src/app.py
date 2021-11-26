from flask import Flask, redirect, url_for, render_template, request
import pickle
from simulations.monty_hall import MontyHallSimulation
# from flask_sqlalchemy import SQLAlchemy
from simulations.estimate_pi import EstimatePi
from simulations.cellular_automata import CellularAutomata

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
# db = SQLAlchemy(app)


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
        features = [int(feature) for feature in request.form.values()]
        return render_template("models.html", prediction_text=features)
    else:
        return render_template("models.html")


@app.route("/music")
def music():
    return render_template("music.html")


@app.route("/simulations")
def simulations():
    return render_template("simulations.html")


@app.route('/monty-hall', methods=['POST', 'GET'])
def monty_hall():
    if request.method == 'POST':
        features = [int(feature) for feature in request.form.values()]
        mh = MontyHallSimulation(features[0], features[1])
        mh.run_sim()
        scores = mh.calculate_scores()
        return render_template("simulations.html",
                               first_guess_score=scores[0],
                               change_guess_score=scores[1])
    else:
        return render_template("simulations.html")


@app.route('/cellular-automata', methods=['POST', 'GET'])
def cellular_automata():
    if request.method == 'POST':
        features = [int(feature) for feature in request.form.values()]
        ca = CellularAutomata(str(features[0]))
        grid = ca.run_ca()
        grid = grid.transpose()
        return render_template("simulations.html",
                               grid=grid)
    else:
        return render_template("simulations.html")


@app.route('/estimate-pi', methods=['POST', 'GET'])
def estimate_pi():
    if request.method == 'POST':
        features = [int(feature) for feature in request.form.values()]
        pi = EstimatePi()
        pi = pi.estimate(features[0])
        return render_template("simulations.html",
                               pi=pi)
    else:
        return render_template("simulations.html")


if __name__ == "__main__":
    app.run(debug=True)
