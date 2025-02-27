# third party
import plotly.express as px
import pandas as pd

def math_scores_box_plot(df):
    """
    Creates a full-width box plot comparing Mathematics raw scores across parishes for each year.
    """
    fig = px.box(
        df,
        x="examYear",
        y="MathRawScore",
        color="StudentParish",
        title="Mathematics Raw Scores by Parish Over Time (Box Plot)",
        labels={
            "examYear": "Year",
            "MathRawScore": "Math Score (Raw, %)",
            "StudentParish": "Parish"
        }
    )

    fig.update_layout(
        width=1400,  # Full width
        height=700,  # Higher for better visibility
        legend=dict(
            title="Parish",
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,  # Moves legend to the right
        ),
        xaxis=dict(
            tickmode="linear",
            dtick=1  # Ensure all years appear
        ),
        yaxis=dict(
            range=[0, 100],  # Ensure raw scores are between 0 and 100
            title="Math Score (Raw, %)"
        ),
    )

    return fig