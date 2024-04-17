import json

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

print(json.dumps({"nodes": nodes, "edges": edges}))
