import json
import os
import sys

from pyalex import Institution, Institutions

BUILD_ENV = os.getenv("BUILD_ENV") or "development"


def get_institutions() -> list[Institution]:
    institutions = []

    institutions_file_path = (
        "docs/data/institutions.json"
        if BUILD_ENV == "production"
        else "docs/data/institutions-dev.json"
    )

    # Load institutions from JSON file
    try:
        institutions = json.load(open(institutions_file_path))
    except Exception as e:
        print(
            "\nError loading institutions from JSON file",
            institutions_file_path,
            ":",
            e,
            "\n",
            file=sys.stderr,
        )

    # Get 5 random institutions in case of error
    if institutions is None or len(institutions) == 0:
        print(
            "No institutions found in JSON file, fetching random institutions\n",
            file=sys.stderr,
        )
        institutions = [Institutions().random() for _ in range(5)]

    return institutions
