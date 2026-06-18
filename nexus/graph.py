from dataclasses import dataclass, field

@dataclass
class Node:
    id: str
    type: str
    properties: dict = field(default_factory=dict)

@dataclass
class Edge:
    source: str
    target: str
    relation: str
    weight: float = 1.0
    properties: dict = field(default_factory=dict)

class NexusGraph:
    """In-memory intelligence graph foundation.

    Community edition uses in-memory graph.
    Enterprise versions can map this to Neo4j, ArangoDB, or Postgres.
    """

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []

    def add_node(self, node_id: str, node_type: str, **properties) -> Node:
        node = Node(node_id, node_type, properties)
        self.nodes[node_id] = node
        return node

    def connect(self, source: str, target: str, relation: str, weight: float = 1.0, **properties) -> Edge:
        edge = Edge(source, target, relation, weight, properties)
        self.edges.append(edge)
        return edge

    def neighbors(self, node_id: str) -> list[Node]:
        ids = [e.target for e in self.edges if e.source == node_id]
        return [self.nodes[i] for i in ids if i in self.nodes]

    def conviction_score(self, asset_id: str) -> float:
        relevant = [e for e in self.edges if e.source == asset_id or e.target == asset_id]
        if not relevant:
            return 0.0
        return round(min(100, sum(max(0, e.weight) for e in relevant) / len(relevant) * 100), 2)
