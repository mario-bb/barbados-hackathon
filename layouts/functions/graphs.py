# third party
import plotly.express as px
import plotly.graph_objects as go

def life_exp_scatter(df):
    fig = px.scatter(
        df,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=55,
    )

    fig.update_layout(transition_duration=500)

    return fig


def plot_employment_map(df, geojson_df):
    fig = px.choropleth(
        df, geojson=geojson_df, 
        locations='Parish', 
        color='worked_percentage',
        featureidkey="properties.name",
        color_continuous_scale="Viridis",
        labels={'worked_percentage':'% Worked'},
        fitbounds="locations",
        )
    
    fig.update_traces(hovertemplate="%{location}: %{z:.1f}%")

    return fig