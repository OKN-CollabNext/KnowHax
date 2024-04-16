import os

import pyalex

# Initialize the pyalex client
pyalex.config.email = os.getenv("OPENALEX_EMAIL")
