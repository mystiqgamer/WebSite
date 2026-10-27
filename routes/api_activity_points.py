from flask import Blueprint, jsonify, request
from data_store import KTU_2024_ACTIVITY_GROUPS

activity_bp = Blueprint("activity_bp", __name__)

@activity_bp.route("/api/activity_points", methods=["GET"])
def get_activity_directory():
    return jsonify({
        "status": "success",
        "scheme": "KTU 2024 Scheme (NEP Aligned)",
        "required_total": 120,
        "min_per_group": 40,
        "activity_credits": 3,
        "groups": KTU_2024_ACTIVITY_GROUPS
    })

@activity_bp.route("/api/activity_points/audit", methods=["POST"])
def audit_activity_points():
    data = request.get_json(silent=True) or {}
    user_activities = data.get("user_activities", [])
    
    # Track points per group
    group_totals = {"group-1": 0.0, "group-2": 0.0, "group-3": 0.0}
    
    for act in user_activities:
        gid = act.get("group_id")
        pts = float(act.get("points", 0))
        if gid in group_totals:
            group_totals[gid] += pts

    total_valid_points = 0.0
    group_breakdowns = []
    deficits = []
    
    for g in KTU_2024_ACTIVITY_GROUPS:
        gid = g["group_id"]
        raw = group_totals.get(gid, 0.0)
        cap = g["max_capped"]
        min_req = g["min_required"]
        
        # Capped value per group
        capped = min(raw, cap)
        total_valid_points += capped
        
        has_met_minimum = (capped >= min_req)
        group_deficit = max(0.0, min_req - capped)
        
        if not has_met_minimum:
            deficits.append(f"{g['group_name'].split(':')[0]} has a deficit of {group_deficit} points (Needs min {min_req} pts)")
            
        group_breakdowns.append({
            "group_id": gid,
            "group_name": g["group_name"],
            "focus": g["focus"],
            "raw_points": raw,
            "capped_points": capped,
            "min_required": min_req,
            "max_capped": cap,
            "has_met_minimum": has_met_minimum,
            "deficit": group_deficit,
            "progress_pct": min(100.0, round((capped / min_req) * 100, 1))
        })

    overall_deficit = max(0.0, 120.0 - total_valid_points)
    is_degree_eligible = (overall_deficit == 0 and len(deficits) == 0)
    
    if is_degree_eligible:
        verdict = "Degree Eligible! (All 3 groups satisfied with >=40 points and Total >=120 points earned for 3 Activity Credits)."
    elif len(deficits) > 0:
        verdict = f"Not Yet Eligible: Failed Three-Group Rule! {'; '.join(deficits)}."
    else:
        verdict = f"Overall Deficit: Earned {total_valid_points}/120 points. Need {overall_deficit} more points."

    # Smart personalized recommendations
    recommendations = []
    if group_totals.get("group-1", 0) < 40:
        recommendations.append("Group 1: Donate blood (+8 to +16 pts), acquire 4-wheeler driving license (+15 pts), or take First Aid/CPR training (+20 pts).")
    if group_totals.get("group-2", 0) < 40:
        recommendations.append("Group 2: Participate in KTU Kalolsavam / Inter-collegiate sports (+20 to +40 pts) or take club coordinator role (+20 pts).")
    if group_totals.get("group-3", 0) < 40:
        recommendations.append("Group 3: Complete a 12-week NPTEL/SWAYAM certification (+50 pts) or participate in an IEDC hackathon (+15 to +40 pts).")

    return jsonify({
        "status": "success",
        "total_verified_points": total_valid_points,
        "required_total": 120,
        "overall_progress_pct": min(100.0, round((total_valid_points / 120.0) * 100, 1)),
        "is_degree_eligible": is_degree_eligible,
        "verdict": verdict,
        "three_group_compliance": (len(deficits) == 0),
        "group_breakdowns": group_breakdowns,
        "recommendations": recommendations
    })
