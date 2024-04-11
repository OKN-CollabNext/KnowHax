---
tilte: CollabNext Challenge
---

# CollabNext Challenge

Exercitation ut mollit fugiat sunt. Lorem deserunt consequat voluptate consectetur reprehenderit qui. Sit exercitation commodo non esse aliqua commodo enim aliquip est dolore sit laboris occaecat tempor. Culpa commodo ad magna dolore veniam commodo est eiusmod qui eu dolore nisi pariatur eiusmod. Est mollit esse pariatur nisi eu sunt fugiat culpa. Veniam excepteur amet duis veniam officia elit cillum sunt.

## Search for anything

```js
const query = view(Inputs.text());
```

### Your Peer Network

<script src="https://unpkg.com/@memgraph/orb/dist/browser/orb.min.js"></script>

```js
const container = document.getElementById("graph");

const nodes = [
  { id: 1, label: "Orb" },
  { id: 2, label: "Graph" },
  { id: 3, label: "Canvas" },
];
const edges = [
  { id: 1, start: 1, end: 2, label: "DRAWS" },
  { id: 2, start: 2, end: 3, label: "ON" },
];

const orb = new Orb.Orb(container);

orb.view.setSettings({
  render: {
    backgroundColor: "#DDDDDD",
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

    if (node.data.label === "Node A") {
      return {
        ...basicStyle,
        size: 10,
        color: "#00FF2B",
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

// Initialize nodes and edges
orb.data.setup({ nodes, edges });

// Render and recenter the view
orb.view.render(() => {
  orb.view.recenter();
});
```

<div id="graph"></div>
