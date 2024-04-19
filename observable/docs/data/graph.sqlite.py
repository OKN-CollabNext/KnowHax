import os
import sqlite3
import tempfile

import pandas as pd

from collabnext.openalex.authors import get_affiliated_authors
from collabnext.openalex.edges import (
    make_affiliated_author_edges,
    make_author_work_edges,
    make_work_topic_edges,
)
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
from collabnext.openalex.works import get_works_by_authors

# Get institutions
institutions = get_institutions()

# Create nodes
institution_nodes = make_institution_nodes(institutions)

# Get unique affiliated authors
authors = get_affiliated_authors(institutions)

# Get all authors affiliated with each institution
author_nodes = make_author_nodes(authors)

# Create instutition edges
affiliated_author_edges = make_affiliated_author_edges(authors)

# Get works by authors
works = get_works_by_authors(authors)

# Create work nodes
work_nodes = make_work_nodes(works)

# Create work author edges
work_author_edges = make_author_work_edges(works)

# Get topics from works
topics = get_work_topics(works)

# Create topic nodes
topic_nodes = make_topic_nodes(topics)

# Create work topic edges
work_topic_edges = make_work_topic_edges(works)


# Group all nodes and edges together
nodes = [*institution_nodes, *author_nodes, *work_nodes, *topic_nodes]
edges = [*affiliated_author_edges, *work_author_edges, *work_topic_edges]

# Create nodes dataframe
df_nodes = pd.DataFrame(nodes, columns=["id", "label", "type"])

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
