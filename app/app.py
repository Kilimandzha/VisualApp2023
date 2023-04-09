import os

import pandas as pd
import yaml
from dash import Dash, dcc, html, dash, Output, Input
import plotly.express as px

df = pd.read_csv("../data/train.csv")
df = df.fillna("?")
df["sentence word count"] = df["sentence"].apply(lambda x: len(x.split()))
app = dash.Dash(
    __name__,
)

server = app.server
app.config.suppress_callback_exceptions = True

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
            id="hist2",
            figure=px.histogram(
                df,
                x="sentence word count",
                opacity=0.3,
                color="sentiment",
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
    app.run_server(debug=True)
