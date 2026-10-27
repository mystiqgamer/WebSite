from flask import Blueprint, jsonify, request
from data_store import RESEARCH_GAPS, KNOWLEDGE_GRAPH
import uuid

hypotheses_bp = Blueprint("hypotheses_bp", __name__)

# In-memory store initialized from seed
ACTIVE_GAPS = list(RESEARCH_GAPS)

@hypotheses_bp.route("/api/hypotheses", methods=["GET"])
def get_hypotheses():
    return jsonify({
        "status": "success",
        "total": len(ACTIVE_GAPS),
        "gaps": ACTIVE_GAPS
    })

@hypotheses_bp.route("/api/hypotheses/generate", methods=["POST"])
def generate_hypothesis():
    data = request.get_json(silent=True) or {}
    domain_a = data.get("domain_a", "Quantum Computing").strip()
    domain_b = data.get("domain_b", "Epigenetic Regulation").strip()
    user_prompt = data.get("prompt", "").strip()

    new_id = f"gap-{uuid.uuid4().hex[:6]}"
    
    # Calculate a synthetic synergy & opportunity score
    score = round(85.0 + (len(domain_a) + len(domain_b)) % 13, 1)

    new_gap = {
        "id": new_id,
        "title": f"Synthesis: {domain_a} × {domain_b}",
        "domain_a": domain_a,
        "domain_b": domain_b,
        "opportunity_score": score,
        "gap_analysis": f"Critical literature synthesis reveals an unmapped cross-domain convergence between {domain_a} and {domain_b}. Current paradigms treat them in isolation, omitting shared mathematical structures." if not user_prompt else f"User-prompted investigation into {domain_a} and {domain_b}: {user_prompt}",
        "proposed_hypothesis": f"Applying computational representations from {domain_a} directly to the non-linear observables in {domain_b} yields a 2.4x improvement in early boundary state detection.",
        "experiment_protocol": {
            "target_dataset": f"Curated benchmark combining {domain_a} state traces and open {domain_b} longitudinal measurements.",
            "sample_size": "2,400 multi-condition cross-validated trials with p < 0.001 threshold.",
            "metrics": ["Statistical Power (1 - beta) > 0.85", "Mean Absolute Percentage Error (MAPE)", "False Positive Discovery Rate"],
            "baseline_comparison": f"Current state-of-the-art mono-disciplinary {domain_b} heuristics."
        },
        "endorsements": 1,
        "created_at": "Just now"
    }

    ACTIVE_GAPS.insert(0, new_gap)

    return jsonify({
        "status": "success",
        "hypothesis": new_gap
    })

@hypotheses_bp.route("/api/hypotheses/<gap_id>/vote", methods=["POST"])
def endorse_hypothesis(gap_id):
    gap = next((g for g in ACTIVE_GAPS if g["id"] == gap_id), None)
    if not gap:
        return jsonify({"status": "error", "message": "Hypothesis gap not found"}), 404
        
    gap["endorsements"] = gap.get("endorsements", 0) + 1
    return jsonify({
        "status": "success",
        "gap_id": gap_id,
        "endorsements": gap["endorsements"]
    })
