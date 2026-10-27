from flask import Blueprint, jsonify, request
from data_store import SOCRATIC_CONTENT, PAPERS_DATABASE

socratic_bp = Blueprint("socratic_bp", __name__)

@socratic_bp.route("/api/socratic/paper/<paper_id>", methods=["GET"])
def get_socratic_paper(paper_id):
    content = SOCRATIC_CONTENT.get(paper_id)
    if not content:
        # Fallback generator for papers without full pre-stored quiz
        paper = next((p for p in PAPERS_DATABASE if p["id"] == paper_id), None)
        if not paper:
            return jsonify({"status": "error", "message": f"Paper '{paper_id}' not found"}), 404
            
        content = {
            "paper_id": paper["id"],
            "title": paper["title"],
            "feynman": {
                "title": f"Feynman Analogy: {paper['title']}",
                "explanation": paper.get("feynman_analogy", "Intuitive conceptual framing connecting abstract theory to concrete physical observations."),
                "key_takeaway": paper.get("key_claims", ["Core breakthrough."])[0]
            },
            "rigorous": {
                "title": "Formal Mathematical Foundations & Methodological Specification",
                "derivation": f"### Methodological Foundation\n{paper.get('methodology', '')}\n\n$$\\text{{Core Formula: }} {paper.get('formula_latex', '')}$$\n\nDataset validation: {paper.get('dataset', '')}",
                "key_takeaway": f"Published in {paper.get('venue', '')} ({paper.get('year', '')}) with {paper.get('reproducibility_score', 95)}% verified replicability."
            },
            "critique": {
                "title": "Methodological Limitations & Critical Review",
                "points": [
                    paper.get("critique", "Assumptions must be verified across non-stationary distributions."),
                    "Generalization bounds are contingent on training dataset distributions.",
                    "Potential edge-case vulnerabilities under extreme parameter shifts."
                ],
                "key_takeaway": "Critical scientific scrutiny balances transformative breakthroughs with empirical boundary conditions."
            },
            "questions": [
                {
                    "id": f"q-{paper['id']}-1",
                    "question": f"What is the primary architectural or theoretical mechanism introduced in '{paper['title']}'?",
                    "options": [
                        paper.get("key_claims", ["Core Mechanism"])[0],
                        "Rejection of all empirical data in favor of heuristic heuristics",
                        "Static constant regression with zero variance bounds",
                        "Sequential single-threaded recurrence"
                    ],
                    "correct_index": 0,
                    "explanation": f"The paper's defining contribution: {paper.get('key_claims', ['Core breakthrough'])[0]}"
                }
            ]
        }
        
    return jsonify({
        "status": "success",
        "content": content
    })

@socratic_bp.route("/api/socratic/evaluate", methods=["POST"])
def evaluate_answer():
    data = request.get_json(silent=True) or {}
    paper_id = data.get("paper_id")
    question_id = data.get("question_id")
    selected_index = data.get("selected_index")
    
    if paper_id not in SOCRATIC_CONTENT:
        # Fallback check
        is_correct = (selected_index == 0)
        return jsonify({
            "status": "success",
            "is_correct": is_correct,
            "feedback": "Correct! You grasped the foundational contribution of this research." if is_correct else "Not quite. Revisit the core claims and methodological derivation.",
            "explanation": "Mastery of primary scientific claims builds strong conceptual scaffolding."
        })
        
    paper_data = SOCRATIC_CONTENT[paper_id]
    target_q = next((q for q in paper_data.get("questions", []) if q["id"] == question_id), None)
    
    if not target_q:
        return jsonify({"status": "error", "message": "Question not found"}), 404
        
    is_correct = (selected_index == target_q["correct_index"])
    
    return jsonify({
        "status": "success",
        "question_id": question_id,
        "is_correct": is_correct,
        "correct_index": target_q["correct_index"],
        "feedback": "Bravo! Precision conceptual deduction verified." if is_correct else "Insightful attempt! Consider the underlying mathematical constraint.",
        "explanation": target_q["explanation"]
    })

@socratic_bp.route("/api/socratic/prerequisites/<concept_id>", methods=["GET"])
def get_prerequisites(concept_id):
    """Returns prerequisite knowledge DAG for a given advanced topic."""
    prereq_graph = {
        "n-transformers": [
            {"name": "Linear Algebra (Dot Products, Projections)", "status": "Mastered", "level": "Foundational"},
            {"name": "Softmax & Probability Distributions", "status": "Mastered", "level": "Foundational"},
            {"name": "Gradient Descent & Backpropagation", "status": "Review Recommended", "level": "Intermediate"},
            {"name": "Recurrent Sequence Modeling (RNNs / LSTMs)", "status": "Optional Context", "level": "Historical"}
        ],
        "n-alphafold": [
            {"name": "Protein Primary & Tertiary Structure", "status": "Mastered", "level": "Foundational"},
            {"name": "Multiple Sequence Alignments (MSAs)", "status": "Mastered", "level": "Intermediate"},
            {"name": "SE(3) Equivariance & 3D Rigid Body Transformations", "status": "Review Recommended", "level": "Advanced"},
            {"name": "Attention Mechanisms (Transformers)", "status": "Mastered", "level": "Intermediate"}
        ],
        "n-chaos": [
            {"name": "Ordinary Differential Equations (ODEs)", "status": "Mastered", "level": "Foundational"},
            {"name": "Phase Space & Vector Fields", "status": "Mastered", "level": "Foundational"},
            {"name": "Bifurcation Theory & Eigenvalues", "status": "Review Recommended", "level": "Intermediate"},
            {"name": "Lyapunov Exponents & Fractal Dimensions", "status": "Target Skill", "level": "Advanced"}
        ],
        "n-sir": [
            {"name": "Coupled Non-Linear Differential Equations", "status": "Mastered", "level": "Foundational"},
            {"name": "Mass-Action Kinetics", "status": "Mastered", "level": "Intermediate"},
            {"name": "Eigenvalue Stability of Fixed Points", "status": "Review Recommended", "level": "Intermediate"},
            {"name": "Stochastic Jump Markov Processes", "status": "Target Skill", "level": "Advanced"}
        ]
    }
    
    prereqs = prereq_graph.get(concept_id, [
        {"name": "Foundational Calculus & Linear Algebra", "status": "Mastered", "level": "Foundational"},
        {"name": "Probability & Statistical Inference", "status": "Review Recommended", "level": "Intermediate"}
    ])
    
    return jsonify({
        "status": "success",
        "concept_id": concept_id,
        "prerequisites": prereqs
    })
