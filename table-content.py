import pandas as pd
# import numpy as np
# import flask as fl
# import matplotlib as mtp
# import matplotlib.pyplot as plt
import pathlib as pl

from sklearn.linear_model import LinearRegression

fn = pl.Path(__file__).parent / 'data/names.csv'

df = pd.read_csv(fn.absolute())

print(df.to_json())

x = (df["Name"] == "Anna") & (df["Gender"] == "F") & (df["State"] == "CA")

dfx = df[x]

# Id  Name  Year Gender State  Count
year = dfx["Year"]
count = dfx["Count"]

xs = []
for xi in year:
    xs.append([xi])

model = LinearRegression()

model.fit(xs, count)
prediction = model.predict(xs)
