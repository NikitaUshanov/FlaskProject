from flask import render_template, request, flash, redirect, url_for, session
from flask_login import login_required
from flask_babel import _
from config import Config
from app.machine import bp
import pandas as pd
from joblib import dump, load
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from flask import jsonify

sent_data = []


@bp.route("/machine")
@login_required
def machine():
    return render_template("machine.html")


@bp.route("/send_data", methods=["POST"])
@login_required
def send_data():
    battery = int(request.form.get("battery"))
    memory = int(request.form.get("memory"))
    weight = int(request.form.get("weight"))


    pos = {k: "Good phone" for k in range(1, 11)}
    neg = {k: "Old phone" for k in range(-10, 0)}
    category = {**pos, **neg, 0: "Simple phone"}

    lst = [battery, memory, weight]
    model = load("../../final.joblib")
    category_prediction = int(model.predict([lst]))

    result = {"cat": category_prediction, "body": category[category_prediction]}
    sent_data.append({"battery": battery, "memory": memory, "weight": weight, "result": result})

    return jsonify(result)


@bp.route("/results")
@login_required
def show_results():
    enumerated_data = list(enumerate(sent_data))
    try:
        if session["result"] == 1:
            session["result"] = 0
            return ""
        session["result"] = 1
        return render_template("results.html", data=enumerated_data)
    except KeyError:
        session["result"] = 1
        return render_template("results.html", data=enumerated_data)

@bp.route("/retrain_model")
@login_required
def retrain_model():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    df = pd.read_sql_query("select * from fin", con=engine)
    df = df.drop(["index", "blue", "clock_speed", "dual_sim", "fc", "four_g", "m_dep", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "three_g", "touch_screen", "wifi"], axis=1)

    y = df["price_range"]
    X = df.drop("price_range", axis=1)

    x_train, x_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state=42)
    gbc = GradientBoostingClassifier(n_estimators=300,
                                 learning_rate=0.05,
                                 random_state=100)
    model = gbc.fit(x_train, y_train)
    dump(model, "../../final.joblib")

    return "Model retrained successfully"