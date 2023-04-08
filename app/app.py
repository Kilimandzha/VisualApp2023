from dash import Dash, dcc, html, dash

app = dash.Dash(__name__,)

server = app.server
app.config.suppress_callback_exceptions = True
app.layout = html.Div([
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal', multi=True)
])


if __name__ == '__main__':
    app.run_server(debug=True)