# std
import os
import logging

# third party
import dash_mantine_components as dmc

# project
import components
from app import app, server

# initialise pages to add to directory
from layouts.dashboard import dashboard_layout

logging.info("Setting main layout")

app.layout = dmc.MantineProvider(
    children=dashboard_layout,
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=os.environ.get("PORT", 8080))
