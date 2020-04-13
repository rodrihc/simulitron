from flask import Flask, render_template, jsonify
import pandas as pd
import pathlib as pl
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('names.html')


@app.route('/names')
def more_stuff():
    fn = pl.Path(__file__).parent / 'data/names.csv'

    dfx = pd.read_csv(fn.absolute())

    # Id,Name,Year,Gender,State,Count

    n = len(dfx)
    data = json.loads(dfx.to_json(orient="split"))["data"];
    info = [
        {"title": str(col)} for col in json.loads(dfx.to_json(orient="split"))["columns"]

    ]

    return jsonify(data=data)


if __name__ == '__main__':
    app.run()
