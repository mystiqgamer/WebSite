import os
from flask import Flask, send_from_directory, jsonify
from routes.api_courses import courses_bp
from routes.api_calculator import calculator_bp
from routes.api_activity_points import activity_bp
from routes.api_simulations import simulations_bp
from routes.api_notes import notes_bp
from data_store import KTU_COURSES, KTU_REGULATIONS, KTU_2024_ACTIVITY_GROUPS, KTU_ANSWER_ARCHITECT

app = Flask(__name__, static_folder="static", static_url_path="")
app.config["JSON_SORT_KEYS"] = False
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Register API blueprints
app.register_blueprint(courses_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(activity_bp)
app.register_blueprint(simulations_bp)
app.register_blueprint(notes_bp)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/presentation")
def presentation():
    return send_from_directory(app.static_folder, "presentation.html")

@app.route("/download/pptx")
def download_pptx():
    pptx_filename = "KTU_Nexus_Presentation.pptx"
    if not os.path.exists(os.path.join(app.static_folder, pptx_filename)):
        pptx_filename = "KTU_ScholarOS_Presentation.pptx"
    return send_from_directory(app.static_folder, pptx_filename, as_attachment=True, download_name="KTU_Nexus_Presentation.pptx")

@app.route("/api/overview")
def overview():
    total_modules = sum(len(c["modules"]) for c in KTU_COURSES)
    total_pyqs = sum(sum(len(m["high_yield_pyqs"]) for m in c["modules"]) for c in KTU_COURSES)
    
    return jsonify({
        "status": "success",
        "platform_name": "KTU Nexus",
        "scheme": "2024 Scheme (B.Tech - NEP Aligned)",
        "tagline": "Academic Intelligence & Exam Success Suite",
        "creators": ["Felix Louie Sojan", "Adithya Jobies"],
        "stats": {
            "ktu_courses": len(KTU_COURSES),
            "modules_mapped": total_modules,
            "high_yield_pyqs": total_pyqs,
            "activity_groups": len(KTU_2024_ACTIVITY_GROUPS),
            "activity_points_required": KTU_REGULATIONS["activity_points_required"],
            "min_points_per_group": KTU_REGULATIONS["min_points_per_group"],
            "answer_blueprints": len(KTU_ANSWER_ARCHITECT),
            "passing_esa_min": KTU_REGULATIONS["passing_criteria"]["min_esa_marks"]
        }
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "scheme": "KTU 2024 Scheme",
        "regulations": "120 Activity Points / Three-Group Rule Active",
        "subsystems": {
            "cie_calculator": "online",
            "pyq_engine": "ready",
            "three_group_activity_auditor": "active",
            "simulators": "online"
        }
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "message": "Resource endpoint not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"status": "error", "message": "Internal processing error", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"[*] KTU Nexus running at http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
