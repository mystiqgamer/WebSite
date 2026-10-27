from flask import Blueprint, jsonify, request
from data_store import KNOWLEDGE_GRAPH
from collections import deque

graph_bp = Blueprint("graph_bp", __name__)

@graph_bp.route("/api/graph", methods=["GET"])
def get_graph():
    discipline_filter = request.args.get("discipline", "").strip().lower()
    
    nodes = KNOWLEDGE_GRAPH["nodes"]
    edges = KNOWLEDGE_GRAPH["edges"]
    
    if discipline_filter and discipline_filter != "all":
        filtered_node_ids = {n["id"] for n in nodes if discipline_filter in n["discipline"].lower() or discipline_filter in n["cluster"].lower()}
        filtered_nodes = [n for n in nodes if n["id"] in filtered_node_ids]
        filtered_edges = [e for e in edges if e["source"] in filtered_node_ids and e["target"] in filtered_node_ids]
    else:
        filtered_nodes = nodes
        filtered_edges = edges

    # Compute network metrics
    degree_counts = {}
    for e in edges:
        s, t = e["source"], e["target"]
        degree_counts[s] = degree_counts.get(s, 0) + 1
        degree_counts[t] = degree_counts.get(t, 0) + 1

    stats = {
        "node_count": len(filtered_nodes),
        "edge_count": len(filtered_edges),
        "density": round((2.0 * len(filtered_edges)) / max(len(filtered_nodes) * (len(filtered_nodes) - 1), 1), 3),
        "disciplines_covered": list({n["discipline"] for n in nodes}),
        "highest_degree_node": max(nodes, key=lambda n: degree_counts.get(n["id"], 0))["label"] if nodes else "N/A"
    }

    return jsonify({
        "status": "success",
        "graph": {
            "nodes": filtered_nodes,
            "edges": filtered_edges
        },
        "stats": stats
    })

@graph_bp.route("/api/graph/bridge", methods=["GET"])
def find_bridge():
    """Finds the shortest semantic interdisciplinary path between two nodes using Breadth-First Search."""
    start_id = request.args.get("source", "").strip()
    end_id = request.args.get("target", "").strip()
    
    if not start_id or not end_id:
        # Default sample bridge: Transformer -> AlphaFold -> CRISPR
        start_id = "n-transformers"
        end_id = "n-crispr"
        
    nodes_map = {n["id"]: n for n in KNOWLEDGE_GRAPH["nodes"]}
    if start_id not in nodes_map or end_id not in nodes_map:
        return jsonify({"status": "error", "message": "Source or target node not found"}), 404

    # Build adjacency list
    adj = {n["id"]: [] for n in KNOWLEDGE_GRAPH["nodes"]}
    edge_map = {}
    for e in KNOWLEDGE_GRAPH["edges"]:
        u, v = e["source"], e["target"]
        adj[u].append((v, e))
        adj[v].append((u, e))
        edge_map[(u, v)] = e
        edge_map[(v, u)] = e

    # BFS for shortest path
    queue = deque([[start_id]])
    visited = {start_id}
    shortest_path = None

    while queue:
        path = queue.popleft()
        curr = path[-1]
        if curr == end_id:
            shortest_path = path
            break
        for neighbor, edge_data in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    if not shortest_path:
        return jsonify({
            "status": "not_connected",
            "message": f"No direct graph bridge found between {nodes_map[start_id]['label']} and {nodes_map[end_id]['label']}"
        })

    # Detailed path metadata
    path_nodes = [nodes_map[nid] for nid in shortest_path]
    path_edges = []
    for i in range(len(shortest_path) - 1):
        u, v = shortest_path[i], shortest_path[i+1]
        e = edge_map.get((u, v))
        if e:
            path_edges.append(e)

    cross_disciplines = list({n["discipline"] for n in path_nodes})
    synergy_score = round(100.0 / len(shortest_path) + (len(cross_disciplines) * 12.5), 1)

    return jsonify({
        "status": "success",
        "source": nodes_map[start_id],
        "target": nodes_map[end_id],
        "path_nodes": path_nodes,
        "path_edges": path_edges,
        "hop_count": len(shortest_path) - 1,
        "cross_disciplines": cross_disciplines,
        "synergy_score": min(synergy_score, 99.5),
        "synthesis_summary": f"Connecting '{nodes_map[start_id]['label']}' to '{nodes_map[end_id]['label']}' via {len(shortest_path)-1} cross-domain bridges spanning {', '.join(cross_disciplines)}."
    })
