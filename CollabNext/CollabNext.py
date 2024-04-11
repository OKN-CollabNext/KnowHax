"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from custom_components.orb.orb import Orb
from rxconfig import config

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


orb = Orb.create


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to CollabNext!", size="9"),
            rx.text("Search for anything"),
            rx.input(),
            orb(),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
