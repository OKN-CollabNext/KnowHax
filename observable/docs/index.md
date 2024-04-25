---
tilte: CollabNext Challenge
style: ./styles.css

---

# CollabNext Challenge

Exercitation ut mollit fugiat sunt. Lorem deserunt consequat voluptate consectetur reprehenderit qui. Sit exercitation commodo non esse aliqua commodo enim aliquip est dolore sit laboris occaecat tempor. Culpa commodo ad magna dolore veniam commodo est eiusmod qui eu dolore nisi pariatur eiusmod. Est mollit esse pariatur nisi eu sunt fugiat culpa. Veniam excepteur amet duis veniam officia elit cillum sunt.

Search

```js
const query = view(Inputs.text());
```

```js
import { SQLiteDatabaseClient } from "npm:@observablehq/sqlite";
const db = FileAttachment("data/graph.sqlite").sqlite();
```

```js
const nodes = db.query(
  `
  SELECT
    *
  FROM
    nodes
  WHERE
    nodes.type <> 'WORK'
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

const loaderOverlay = document.getElementById('loader-overlay');
const graphContainer = document.getElementById('graph');

// Show loader overlay
loaderOverlay.style.display = 'flex';

// Initialize nodes and edges
orb.data.setup({ nodes, edges });

// Render and recenter the view
orb.view.render(() => {
  loaderOverlay.style.display = 'none';
  orb.view.recenter();
});
```

```js
let selectedNode;

orb.events.on('node-click', (event) => {
  getData(event)
});


function getData(event) {
  selectedNode = event.node.data;
  console.log(selectedNode)
  updateDetails(selectedNode)
}

const details = document.querySelector('.details')

function updateDetails(selectedNode) {
  details.innerHTML = '';

  let html = '';

  if (selectedNode) {
    html += `<h1>${selectedNode.label}</h1>`;

    if (selectedNode.type === 'INSTITUTION') {
      html += `<p><b>Institution type:</b> ${selectedNode.type}</p>`;
      html += `<p><b>Homepage:</b> ${selectedNode.homepage}</p>`;
      html += `<p><b>Works:</b> ${selectedNode.works_count}</p>`;
      html += `<p><b>Cited by:</b> ${selectedNode.cited_by_count}</p>`;
    } else if (selectedNode.type === 'AUTHOR') {
      html += `<p><b>Works:</b> ${selectedNode.works_count}</p>`;
      html += `<p><b>Cited by:</b> ${selectedNode.cited_by_count}</p>`;
    } else if (selectedNode.type === 'TOPIC') {
      html += `<p><b>Description:</b> ${selectedNode.description}</p>`;
      html += `<p><b>Field:</b> ${selectedNode.field}</p>`;
      html += `<p><b>Subfield:</b> ${selectedNode.subfield}</p>`;
      html += `<p><b>Domain:</b> ${selectedNode.domain}</p>`;
    }
  }

  // Set the generated HTML content to the details element
  details.innerHTML = html;
}
```

<div class="content">
  <div class="loader-overlay" id="loader-overlay">
    <div class="loader"></div>
  </div>
  <div id="graph" style="width:100%; height:800px"></div>
  <div class="details">
  <h3>Click on any node to see more details.</h3>
  </div>
</div>
