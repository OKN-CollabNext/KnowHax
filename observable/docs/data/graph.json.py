import json

from collabnext.openalex.authors import get_affiliated_authors
from collabnext.openalex.edges import (
    make_affiliated_author_edges,
    make_associated_institution_edges,
)
from collabnext.openalex.institutions import (
    dedup_institutions,
    get_associated_institutions,
    get_institutions,
)
from collabnext.openalex.nodes import make_author_nodes, make_institution_nodes

# Get institutions
institutions = get_institutions()

# Get associated institutions
associated_institutions = get_associated_institutions(institutions)

# Combine all unique institutions
all_institutions = dedup_institutions([*institutions, *associated_institutions])

# Create nodes
institution_nodes = make_institution_nodes(all_institutions)

# Get unique affiliated authors
authors = get_affiliated_authors(all_institutions)

# Get unique authors affiliated with each institution
author_nodes = make_author_nodes(authors)

# Create associated institution edges
associated_institution_edges = make_associated_institution_edges(institutions)
affiliated_author_edges = make_affiliated_author_edges(authors)

# Group all nodes and edges together
nodes = [*institution_nodes, *author_nodes]
edges = [*associated_institution_edges, *affiliated_author_edges]

print(json.dumps({"nodes": nodes, "edges": edges}))
