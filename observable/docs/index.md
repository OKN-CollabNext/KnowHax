---
tilte: CollabNext Challenge
style: ./styles.css
---

# CollabNext Challenge

<div class="intro">
  <p>Researchers struggle to discover connections between researchers and topics from HBCUs and underrepresented universities due to the lack of tools available that focus on diversity and inclusion of underrepresented researchers. Our app seeks to address this problem by creating a knowledge graph visualization with an intuitive user interface that allows researchers, students, conference organizers and others to discover researchers from HBCUs and understand how they are connected through their institutions and research topics.<p>

  <p>With a sample of 5 HBCUs as our example, our app provides and interface for the user to explore a visual interactive representation of data from OpenAlex. Our app represents a scalable starting point towards addressing the broader systemic issue of diversity and inclusion in research data.</p>
</div>

```js
const query = view(Inputs.text({ placeholder: "Search" }));
```

```js
import { SQLiteDatabaseClient } from "npm:@observablehq/sqlite";
const db = FileAttachment("data/graph.sqlite").sqlite();
```

```js
const institutions = db.query(
  `
  SELECT
    *
  FROM
    nodes
  WHERE
    nodes.type = 'INSTITUTION'
  `
);
const authors = db.query(
  query
    ? `
  SELECT
    *
  FROM
    nodes
  WHERE
    nodes.type = 'AUTHOR'
    AND nodes.name like '%${query}%'
  `
    : `
  SELECT
    *
  FROM
    nodes
  WHERE
    nodes.type = 'AUTHOR'
  `
);
const topics = db.query(
  `
  SELECT
    *
  FROM
    nodes
  WHERE
    nodes.type = 'TOPIC'
  `
);
```

```js
const edges = db.query(
  `
  SELECT
    *
  FROM
    edges
  WHERE
    edges.start_type <> 'WORK'
    OR edges.end_type <> 'WORK'
  `
);
```

<script src="https://unpkg.com/@memgraph/orb/dist/browser/orb.min.js"></script>

```js
const container = document.getElementById("graph");

const orb = new Orb.Orb(container);

orb.view.setSettings({
  render: {
    backgroundColor: "#f4faff",
    padding: "0",
    margin: "0",
  },
});

// Assign a basic style
orb.data.setDefaultStyle({
  getNodeStyle(node) {
    const basicStyle = {
      borderColor: "#1d1d1d",
      borderWidth: 0.6,
      color: "#DD2222",
      colorHover: "#e7644e",
      colorSelected: "#e7644e",
      fontSize: 3,
      label: node.data.label,
      size: 6,
    };

    if (node.data.type === "AUTHOR") {
      return {
        ...basicStyle,
        size: 10,
        color: "#0df2c9",
        zIndex: 1,
      };
    }

    if (node.data.type === "WORK") {
      return {
        ...basicStyle,
        size: 10,
        color: "#245cc3",
        zIndex: 1,
      };
    }

    if (node.data.type === "TOPIC") {
      return {
        ...basicStyle,
        size: 10,
        color: "#f8ee35",
        zIndex: 1,
      };
    }

    return {
      ...basicStyle,
    };
  },
  getEdgeStyle(edge) {
    return {
      color: "#999999",
      colorHover: "#1d1d1d",
      colorSelected: "#1d1d1d",
      fontSize: 3,
      width: 0.3,
      widthHover: 0.9,
      widthSelected: 0.9,
      label: edge.data.label,
    };
  },
});

const loaderOverlay = document.getElementById("loader-overlay");
const graphContainer = document.getElementById("graph");
const details = document.querySelector(".details");

// Show loader overlay
loaderOverlay.style.display = "flex";

// Initialize nodes and edges
orb.data.setup({ nodes: [...institutions, ...topics, ...authors], edges });

// Render and recenter the view
orb.view.render(() => {
  loaderOverlay.style.display = "none";
  details.style.display = "block";
  orb.view.recenter();
});
```

```js
let selectedNode;

orb.events.on("node-click", (event) => {
  getData(event);
});

function getData(event) {
  selectedNode = event.node.data;
  updateDetails(selectedNode);
}

const details = document.querySelector(".details");

function updateDetails(selectedNode) {
  details.innerHTML = "";
  let html = "";

  if (selectedNode) {
    details.style.display = "block";
    html += `<h2>${selectedNode.label}</h2>`;

    if (selectedNode.type === "INSTITUTION") {
      html += `<p><b>Homepage:</b> <a href="${selectedNode.homepage}">${selectedNode.homepage}</a></p>`;
      html += `<p><b>Works:</b> ${selectedNode.works_count}</p>`;
      html += `<p><b>Cited by:</b> ${selectedNode.cited_by_count}</p>`;
      html += `<a href="${selectedNode.id}" target="_blank">View on OpenAlex</a>`;
    } else if (selectedNode.type === "AUTHOR") {
      html += `<p><b>Works:</b> ${selectedNode.works_count}</p>`;
      html += `<p><b>Cited by:</b> ${selectedNode.cited_by_count}</p>`;
      html += `<a href="${selectedNode.id}" target="_blank">View on OpenAlex</a>`;
    } else if (selectedNode.type === "TOPIC") {
      html += `<p><b>Subfield:</b> ${selectedNode.subfield}</p>`;
      html += `<p><b>Domain:</b> ${selectedNode.domain}</p>`;
      html += `<a href="${selectedNode.id}" target="_blank">View on OpenAlex</a>`;
    }
  }
  details.innerHTML = html;
}
```

<div class="content">
  <div class="loader-overlay" id="loader-overlay">
    <div class="loader"></div>
  </div>
  <div id="graph" style="width:100%; height:800px"></div>
  <div class="details">
    <h3>Click any node to see more details.</h3>
  </div>
</div>
