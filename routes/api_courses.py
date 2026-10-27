from flask import Blueprint, jsonify, request
from data_store import KTU_COURSES, KTU_ANSWER_ARCHITECT, KTU_BRANCHES, SEMESTER_CREDIT_MATRIX

courses_bp = Blueprint("courses_bp", __name__)

@courses_bp.route("/api/courses", methods=["GET"])
def get_courses():
    semester = request.args.get("semester", "").strip().lower()
    branch = request.args.get("branch", "").strip().lower()
    query = request.args.get("q", "").strip().lower()
    
    results = []
    for c in KTU_COURSES:
        if semester and semester != "all":
            if semester not in c["semester"].lower():
                continue
        if branch and branch != "all":
            # Common matches all branches
            if c.get("branch_id") != "common" and c.get("branch_id") != branch:
                continue
        if query:
            match_code = query in c["code"].lower()
            match_title = query in c["title"].lower()
            match_branch = query in c["branch"].lower()
            match_syllabus = any(query in m["syllabus"].lower() for m in c.get("modules", []))
            if not (match_code or match_title or match_branch or match_syllabus):
                continue
        results.append(c)

    return jsonify({
        "status": "success",
        "total": len(results),
        "courses": results
    })

@courses_bp.route("/api/courses/<course_id>", methods=["GET"])
def get_course_detail(course_id):
    course = next((c for c in KTU_COURSES if c["id"] == course_id), None)
    if not course:
        return jsonify({"status": "error", "message": f"Course '{course_id}' not found"}), 404
        
    return jsonify({
        "status": "success",
        "course": course
    })

@courses_bp.route("/api/branches", methods=["GET"])
def get_branches():
    return jsonify({
        "status": "success",
        "branches": KTU_BRANCHES,
        "credit_matrix": SEMESTER_CREDIT_MATRIX
    })

@courses_bp.route("/api/answers/blueprints", methods=["GET"])
def get_answer_blueprints():
    return jsonify({
        "status": "success",
        "total": len(KTU_ANSWER_ARCHITECT),
        "blueprints": KTU_ANSWER_ARCHITECT
    })
