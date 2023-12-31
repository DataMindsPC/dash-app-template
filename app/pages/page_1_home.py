######################
#                    #
#    PAGE 1: HOME    #
#                    #
######################

# Import libraries
from dash import html, dcc
import dash_mantine_components as dmc

# Import components
from components.ui_cards import (complex_card_with_image,
                                 numbers_and_ring_card,
                                 numbers_and_comparison_card)

# Define the page layout
# ------------------------
layout = html.Div(
    [

        dmc.Container(
            [
                dmc.Title("Home", order=1),
            ]
        ),
        
        dmc.Container(
            children=[
                dmc.Grid(
                    children=[
                        dmc.Col(complex_card_with_image(), span=6),
                        dmc.Col(complex_card_with_image(), span=6)
                    ],
                    gutter="md",
                    style={"margin-top": "20px"}
                )
            ]
        ),

        dmc.Center(
            children=[
                numbers_and_ring_card()
            ], style={"margin-top": "20px"}
        ),

        dmc.Container(
            [
                dmc.Center(
                    children=[
                        dmc.Grid(
                            [
                                dmc.Col(numbers_and_comparison_card(), span=4),
                                dmc.Col(numbers_and_comparison_card(), span=4),
                                dmc.Col(numbers_and_comparison_card(), span=4),
                            ]
                        )
                    ]
                )
            ], style={"margin-top": "20px"}, size="xl"
        ),
    ]
)
