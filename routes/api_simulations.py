from flask import Blueprint, jsonify, request
from data_store import run_cpu_scheduling

simulations_bp = Blueprint("simulations_bp", __name__)

@simulations_bp.route("/api/simulations/cpu_scheduling", methods=["POST"])
def simulate_cpu():
    data = request.get_json(silent=True) or {}
    processes = data.get("processes", [
        {"name": "P1", "arrival": 0, "burst": 5},
        {"name": "P2", "arrival": 1, "burst": 3},
        {"name": "P3", "arrival": 2, "burst": 8},
        {"name": "P4", "arrival": 3, "burst": 6}
    ])
    quantum = int(data.get("quantum", 2))
    
    result = run_cpu_scheduling(processes, quantum)
    return jsonify(result)

@simulations_bp.route("/api/simulations/kmap", methods=["POST"])
def simulate_kmap():
    data = request.get_json(silent=True) or {}
    # Array of active minterms [0, 1, 2, 5, 8, 9, 10]
    minterms = set(data.get("minterms", [0, 1, 2, 5, 8, 9, 10]))
    dont_cares = set(data.get("dont_cares", [3, 11]))

    # Gray code 4x4 coordinate mapping
    # Rows AB: 00 (0), 01 (1), 11 (3), 10 (2)
    # Cols CD: 00 (0), 01 (1), 11 (3), 10 (2)
    row_codes = [0, 1, 3, 2] # binary integer representation
    col_codes = [0, 1, 3, 2]
    
    grid = []
    for r in row_codes:
        row = []
        for c in col_codes:
            m = (r << 2) | c
            val = 1 if m in minterms else ('X' if m in dont_cares else 0)
            row.append({"minterm": m, "value": val, "binary": f"{r:02b}{c:02b}"})
        grid.append(row)

    # Simplified mock reduction demo for KTU syllabus
    terms = []
    if 0 in minterms and 2 in minterms and 8 in minterms and 10 in minterms:
        terms.append("B' D' (Corner Quad)")
    if 0 in minterms and 1 in minterms and 8 in minterms and 9 in minterms:
        terms.append("B' C' (Quad m(0,1,8,9))")
    if 5 in minterms:
        terms.append("A' B C' D (Single Minterm)")

    expression = " + ".join(terms) if terms else "F = Sigma m(" + ", ".join(map(str, sorted(minterms))) + ")"

    return jsonify({
        "status": "success",
        "grid": grid,
        "minterms": sorted(list(minterms)),
        "simplified_expression": expression,
        "nand_gate_count": len(terms) + 1
    })

@simulations_bp.route("/api/simulations/bst", methods=["POST"])
def simulate_bst():
    data = request.get_json(silent=True) or {}
    elements = data.get("elements", [45, 23, 65, 12, 34, 55, 78])

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def insert(root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root

    def inorder(root, res):
        if root:
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

    def preorder(root, res):
        if root:
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)

    def postorder(root, res):
        if root:
            postorder(root.left, res)
            postorder(root.right, res)
            res.append(root.val)

    def height(root):
        if not root:
            return 0
        return 1 + max(height(root.left), height(root.right))

    def to_dict(root):
        if not root:
            return None
        return {
            "name": str(root.val),
            "val": root.val,
            "children": [c for c in [to_dict(root.left), to_dict(root.right)] if c is not None]
        }

    root = None
    for el in elements:
        root = insert(root, el)

    in_res, pre_res, post_res = [], [], []
    inorder(root, in_res)
    preorder(root, pre_res)
    postorder(root, post_res)

    return jsonify({
        "status": "success",
        "inorder": in_res,
        "preorder": pre_res,
        "postorder": post_res,
        "tree_height": height(root),
        "node_count": len(elements),
        "tree_hierarchy": to_dict(root)
    })
