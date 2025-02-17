# stdlib
import logging
import os

# third party
import dash
import dash_bootstrap_components as dbc
import dotenv


dotenv.load_dotenv()
# enable logging
logging.basicConfig(level=logging.INFO)

# include external css and js
# TODO: review
external_js = [
    "https://code.jquery.com/jquery-3.4.1.slim.min.js",
    "https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js",
]


dash._dash_renderer._set_react_version("18.2.0")
inter_font = "https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,100;0,300;0,400;0,500;0,600;0,650;0,700;0,900;1,100;1,300;1,400;1,700;1,900"

app = dash.Dash(
    __name__,
    external_scripts=external_js,
    external_stylesheets=[
        inter_font,
        "https://unpkg.com/@mantine/dates@7/styles.css",
        "https://unpkg.com/@mantine/code-highlight@7/styles.css",
        "https://unpkg.com/@mantine/charts@7/styles.css",
        "https://unpkg.com/@mantine/carousel@7/styles.css",
        "https://unpkg.com/@mantine/notifications@7/styles.css",
        "https://unpkg.com/@mantine/nprogress@7/styles.css",
    ],
    url_base_pathname=os.environ.get("PREFIX_URL", "/"),
)

prefix_url = os.environ.get("PREFIX_URL", "/")

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Data Science Tool</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""


server = app.server
app.config.suppress_callback_exceptions = True
