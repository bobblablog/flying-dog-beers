import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Sam Adams Utopias', 'BrewDog Tactical Nuclear Penguin', 'Struise Black Damnation VI', 'BrewDog Sink The Bismarck'] #variable contains a list

bitterness = go.Bar(
    x=beers,
    y=[29, 32, 39, 42],
    name='ABV',
    marker={'color':'green'} 
)
alcohol = go.Bar(
    x=beers,
    y=[7.4, 17.1, 5.2, 9.5],
    name='IBU',
    marker={'color':'red'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Strong Beers'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
