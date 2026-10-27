from flask import Blueprint, jsonify, request
from data_store import calculate_ktu_cie, KTU_REGULATIONS

calculator_bp = Blueprint("calculator_bp", __name__)

@calculator_bp.route("/api/calculator/cie", methods=["POST"])
def compute_cie():
    data = request.get_json(silent=True) or {}
    try:
        s1 = float(data.get("series1", 30.0))
        s2 = float(data.get("series2", 35.0))
        assign = float(data.get("assignment", 10.0))
        att = float(data.get("attendance_pct", 85.0))
        
        result = calculate_ktu_cie(s1, s2, assign, att)
        result["status"] = "success"
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": f"Calculation error: {str(e)}"}), 400

@calculator_bp.route("/api/calculator/regulations", methods=["GET"])
def get_regulations():
    return jsonify({
        "status": "success",
        "regulations": KTU_REGULATIONS
    })
