# third party
import json
from dash import dcc, Input, Output
import dash_mantine_components as dmc

# project
from app import app
from .functions.prep_data import import_data
from .functions.graphs import life_exp_scatter, plot_employment_map


df = import_data("gapminder.csv")

with open("data/bb.json") as file:
    barbados_parish_geojson = json.loads(file.read())


bb_employment = import_data("barbados_census_working.csv")
parish_employment =bb_employment[bb_employment['Parish']!='Barbados']

dashboard_layout = [
    dmc.Grid(
        gutter=10,
        grow=True,
        children=[
            dmc.GridCol(
                dmc.Alert(
                    """
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                        incididunt ut labore et dolore magna aliqua. Etiam non quam lacus suspendisse 
                        faucibus interdum posuere lorem ipsum. Ac turpis egestas maecenas pharetra 
                        convallis. Elementum facilisis leo vel fringilla est. Mi bibendum neque egestas 
                        congue quisque egestas diam. Varius quam quisque id diam. Integer quis auctor 
                        elit sed. Mattis molestie a iaculis at erat pellentesque. Aliquam ut porttitor 
                        leo a diam sollicitudin tempor id. Non tellus orci ac auctor augue mauris augue 
                        neque. Mi eget mauris pharetra et ultrices neque ornare aenean euismod. Vestibulum 
                        morbi blandit cursus risus. Et ultrices neque ornare aenean euismod. Eros in 
                        cursus turpis massa tincidunt dui. Urna condimentum mattis pellentesque id nibh 
                        tortor.
                    """,
                    title="This is a test alert",
                ),
                span=4,
            ),
            dmc.GridCol(
                [
                    dcc.Graph(id="graph-with-slider", className="pr-5"),
                    dcc.Slider(
                        id="year-slider",
                        min=df["year"].min(),
                        max=df["year"].max(),
                        value=1982,
                        marks={str(year): str(year) for year in df["year"].unique()},
                        step=None,
                        className="pr-5",
                    ),
                ],
                span=8,
            ),
            dmc.GridCol(
                [
                    dcc.Graph(id="map", className="pr-5"),
                    dcc.Dropdown(['Male', 'Female', 'Both Sexes'], 'Both Sexes', id='sex-selector', className="pr-5"),
                ],
                span=8
            )

        ],
    )
]


@app.callback(Output("graph-with-slider", "figure"), Input("year-slider", "value"))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    fig = life_exp_scatter(filtered_df)

    return fig


@app.callback(Output("map", "figure"), Input("sex-selector", "value"))
def update_map(selected_sex):
    filtered_df = parish_employment[parish_employment["Sex"] == selected_sex]
    fig = plot_employment_map(filtered_df, barbados_parish_geojson)
    return fig
