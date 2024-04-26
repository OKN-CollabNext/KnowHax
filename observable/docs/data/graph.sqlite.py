import os
import sqlite3
import tempfile

import pandas as pd

from collabnext.openalex.authors import get_affiliated_authors
from collabnext.openalex.edges import (
    make_author_institution_edges,
    make_author_work_edges,
    make_work_topic_edges,
)
from collabnext.openalex.inference import infer_author_topic_edges
from collabnext.openalex.institutions import (
    get_institutions,
)
from collabnext.openalex.nodes import (
    make_author_nodes,
    make_institution_nodes,
    make_topic_nodes,
    make_work_nodes,
)
from collabnext.openalex.topics import get_work_topics
from collabnext.openalex.utils import clamp_author_nodes_to_author_edges
from collabnext.openalex.works import (
    clamp_works_to_institutions,
    get_works_by_authors,
)

#
# Get and filter date from OpenAlex
#

# Get institutions
institutions = get_institutions()

# Get unique affiliated authors
authors = get_affiliated_authors(institutions)

# Get works by authors in these institutions
works = get_works_by_authors(authors)

# Clamp works to institutions
works = clamp_works_to_institutions(works, institutions)

# Get topics from works
topics = get_work_topics(works)

#
# Convert into nodes and edges
#

# Create nodes
institution_nodes = make_institution_nodes(institutions)

# Get all authors affiliated with each institution
author_nodes = make_author_nodes(authors)

# Create author -> instutition edges
author_institution_edges = make_author_institution_edges(authors, institutions)

# Create work nodes
work_nodes = make_work_nodes(works)

# Create author-work edges
author_work_edges = make_author_work_edges(authors, works)

# Clamp author nodes to those with works
author_nodes = clamp_author_nodes_to_author_edges(author_nodes, author_work_edges)

# Create topic nodes
topic_nodes = make_topic_nodes(topics)

# Create work-topic edges
work_topic_edges = make_work_topic_edges(works, topics)

# Infer author-topic edges
author_topic_edges = infer_author_topic_edges(author_work_edges, work_topic_edges)

# Clamp author nodes to author topic edges
author_nodes = clamp_author_nodes_to_author_edges(author_nodes, author_topic_edges)

# Group all nodes and edges together
nodes = [*institution_nodes, *author_nodes, *work_nodes, *topic_nodes]
edges = [
    *author_institution_edges,
    *author_work_edges,
    *author_topic_edges,
    *work_topic_edges,
]

#
# Create SQLite database
#

# Create nodes dataframe
df_nodes = pd.DataFrame(
    nodes,
    columns=[
        "id",
        "label",
        "type",
        "name",
        "institution_type",
        "homepage",
        "works_count",
        "cited_by_count",
        "field",
        "description",
        "subfield",
        "domain",
    ],
)

# Create edges dataframe
df_edges = pd.DataFrame(
    edges, columns=["id", "start", "end", "label", "start_type", "end_type"]
)

# Save the dataframe to a SQLite database
with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as temp_file:
    temp_filename = temp_file.name
    with sqlite3.connect(temp_filename) as conn:
        df_nodes.to_sql("nodes", conn, index=False)
        df_edges.to_sql("edges", conn, index=False)

# Print db file to stdout
os.system(f"cat {temp_filename}")
