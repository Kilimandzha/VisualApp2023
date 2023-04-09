import os

import pandas as pd
import yaml
from dash import Dash, dcc, html, dash, Output, Input
import plotly.express as px

df = pd.read_csv("../data/train.csv")
print("Read csv")
df.drop(columns=["Unnamed: 0"])
df = df.fillna("?")
df["sentence word count"] = df["sentence"].apply(lambda x: len(x.split()))
app = dash.Dash(
    __name__, external_scripts=[
        'https://cdn.plot.ly/plotly-2.20.0.min.js']
)

server = app.server
app.config.suppress_callback_exceptions = False

cols = ["1category", "2category", "sentiment"]

app.layout = html.Div(
    [
        html.Div(children="Distributions by column"),
        html.Hr(),
        dcc.Dropdown(id="dropdown", options=cols, value="1category"),
        dcc.Graph(
            id="hist1",
            figure=px.histogram(
                df,
                x="sentiment",
                opacity=0.6,
                color_discrete_sequence=["indianred"],
            ),
        ),
        dcc.Graph(
            id="hist2",
            figure=px.histogram(
                df,
                x="1category",
                opacity=0.6,
                color="sentiment",
                barmode="stack",
                category_orders={"sentiment": ["-", "?", "+"]},
                color_discrete_sequence=["indianred", "goldenrod", "green"],
            ),
        ),
        html.Div(children="Word count in sentences"),
        html.Hr(),
        dcc.Graph(
            id="hist3",
            figure=px.histogram(
                df,
                x="sentence word count",
                opacity=0.3,
                color="sentiment",
                category_orders={"sentiment": ["-", "?", "+"]},
                color_discrete_sequence=["indianred", "goldenrod", "green"],
            ),
        ),

    ]
)


@app.callback(Output("hist1", "figure"), Input("dropdown", "value"))
def change(x):
    fig = px.histogram(
        df, x=x, opacity=0.6, color_discrete_sequence=["indianred"]
    )
    return fig


if __name__ == "__main__":
    try:
        app.run_server(debug=False)
    except Exception as e:
        print(e)
        print(e.__traceback__)
