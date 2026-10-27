"""
KTU ScholarOS - Comprehensive 5-Branch S1-S8 Academic Repository (B.Tech 2024 Scheme)
Includes full curriculum structures, courses, and syllabi for:
1. CSE - Computer Science & Engineering
2. ECE - Electronics & Communication Engineering
3. EEE - Electrical & Electronics Engineering
4. MECH - Mechanical Engineering
5. CE / CN - Civil Engineering & Computer Networking
"""

from typing import Dict, List, Any

# KTU 2024 Scheme S1 to S8 Semester Credit Distribution Matrix
SEMESTER_CREDIT_MATRIX = {
    "S1": {"credits": 20, "focus": "Basic Sciences & Common Engineering Foundation"},
    "S2": {"credits": 24, "focus": "Engineering Sciences, Programming in C & Digital 101"},
    "S3": {"credits": 25, "focus": "Core Discipline Foundations & Mathematics"},
    "S4": {"credits": 24, "focus": "Applied Core Engineering & Project-Based Learning"},
    "S5": {"credits": 23, "focus": "Advanced Professional Core & Program Elective I"},
    "S6": {"credits": 23, "focus": "Design Electives, Open Elective I & Mini Project"},
    "S7": {"credits": 17, "focus": "Industry Electives, Seminar & Project Phase I"},
    "S8": {"credits": 11, "focus": "Major Project Phase II & Comprehensive Viva"},
    "TOTAL_ACADEMIC": 167,
    "ACTIVITY_CREDITS": 3,
    "GRAND_TOTAL": 170,
    "HONORS_TOTAL": 185
}

# 5 Major Engineering Branches S1 to S8 Courses
KTU_BRANCHES = [
    {"id": "cse", "name": "Computer Science & Engineering", "short": "CSE", "code_prefix": "CST"},
    {"id": "ece", "name": "Electronics & Communication Engineering", "short": "ECE", "code_prefix": "ECT"},
    {"id": "eee", "name": "Electrical & Electronics Engineering", "short": "EEE", "code_prefix": "EET"},
    {"id": "mech", "name": "Mechanical Engineering", "short": "MECH", "code_prefix": "MET"},
    {"id": "ce_cn", "name": "Civil Engineering & Computer Networking", "short": "CE / CN", "code_prefix": "CET/CNT"}
]

# Comprehensive Course Database across S1-S8 for all 5 Branches (Imported from courses_data.py)
from courses_data import KTU_COURSES

# KTU 2024 Scheme Evaluation & Grading Regulations
KTU_REGULATIONS = {
    "scheme": "2024 Scheme (NEP Aligned)",
    "internal_max": 50,
    "esa_max": 100,
    "total_max": 150,
    "activity_credits": 3,
    "activity_points_required": 120, # REVISED KTU 2024 REGULATION
    "min_points_per_group": 40,      # MANDATORY THREE-GROUP THRESHOLD
    "passing_criteria": {
        "min_esa_marks": 40,  # 40% in University Exam is MANDATORY
        "min_aggregate_pct": 50.0, # Minimum 50% overall to pass
        "attendance_eligibility_pct": 75.0 # Minimum 75% attendance to write exam
    },
    "grade_scale": [
        {"grade": "O", "name": "Outstanding", "grade_point": 10.0, "min_aggregate_pct": 90.0, "desc": "Top Tier Academic Distinction"},
        {"grade": "A+", "name": "Excellent", "grade_point": 9.0, "min_aggregate_pct": 85.0, "desc": "High Honors Eligibility"},
        {"grade": "A", "name": "Very Good", "grade_point": 8.5, "min_aggregate_pct": 80.0, "desc": "Eligible for B.Tech Honors (>8.5 CGPA)"},
        {"grade": "B+", "name": "Good", "grade_point": 8.0, "min_aggregate_pct": 70.0, "desc": "First Class with Distinction range"},
        {"grade": "B", "name": "Above Average", "grade_point": 7.0, "min_aggregate_pct": 60.0, "desc": "First Class Range"},
        {"grade": "C", "name": "Average", "grade_point": 6.0, "min_aggregate_pct": 50.0, "desc": "Minimum Pass Grade without Supply"},
        {"grade": "P", "name": "Pass", "grade_point": 5.0, "min_aggregate_pct": 45.0, "desc": "Marginal Pass"},
        {"grade": "F", "name": "Failed / Supplementary", "grade_point": 0.0, "min_aggregate_pct": 0.0, "desc": "Requires Supplementary Exam (Supply)"}
    ]
}

# KTU 2024 Scheme REVISED 120-Activity-Point Regulations (Three-Group Rule)
KTU_2024_ACTIVITY_GROUPS: List[Dict[str, Any]] = [
    {
        "group_id": "group-1",
        "group_name": "Group 1: National Initiatives, Social & Community Engagement, Basic Life Skills",
        "min_required": 40,
        "max_capped": 60,
        "focus": "Social commitment, community service, health & emergency preparedness",
        "activities": [
            {"name": "NSS Active Volunteer (2 Years + 7-Day Special Camp)", "points": 60, "doc_req": "NSS State Cell Completion Certificate signed by Programme Officer"},
            {"name": "NCC 'B' or 'C' Certificate", "points": 50, "doc_req": "NCC Directorate Official Certificate"},
            {"name": "Emergency Response / CPR / First Aid / Fire Safety Training", "points": 20, "doc_req": "Certified Red Cross / Fire & Rescue Training Certificate"},
            {"name": "Blood Donation at Govt Blood Bank / Campus Camp", "points": 8, "doc_req": "Hospital / Blood Bank Certificate (Max 2 times/year = 16 pts)"},
            {"name": "Acquiring Valid Four-Wheeler (LMV) Driving License", "points": 15, "doc_req": "Driving License Copy obtained during B.Tech tenure"},
            {"name": "Certified Basic Swimming Course", "points": 15, "doc_req": "Sports Council / Certified Aquatic Center Certificate"},
            {"name": "Tree Planting / Environmental Drive (Geo-tagged)", "points": 10, "doc_req": "Faculty Advisor verified geo-tagged photo + report"}
        ]
    },
    {
        "group_id": "group-2",
        "group_name": "Group 2: Cultural, Sports, Leadership & Management",
        "min_required": 40,
        "max_capped": 60,
        "focus": "Extracurricular talents, physical fitness, institutional governance and events",
        "activities": [
            {"name": "KTU Inter-Collegiate University Winner / Runner-up in Sports", "points": 40, "doc_req": "KTU Sports Directorate Official Certificate"},
            {"name": "KTU University Arts Fest (Kalolsavam) Prize Winner (1st/2nd/3rd)", "points": 40, "doc_req": "KTU University Kalolsavam Merit Certificate"},
            {"name": "Elected College Union Office Bearer (Chairman, Gen Sec, Councilor)", "points": 30, "doc_req": "College Principal Notification & Election Record"},
            {"name": "Student Club Lead / Chief Student Coordinator (IEDC, NSS, IEEE)", "points": 20, "doc_req": "Faculty In-Charge Appointment Letter + Completion Report"},
            {"name": "Editor / Core Committee Member of College Magazine", "points": 15, "doc_req": "Principal Certificate + Copy of Published Magazine"},
            {"name": "Annual Sports Day / Arts Day College Level Prize Winner", "points": 15, "doc_req": "College Level Merit Certificate"},
            {"name": "Inter-Collegiate Cultural Fest Participation", "points": 10, "doc_req": "Host Institution Participation Certificate"}
        ]
    },
    {
        "group_id": "group-3",
        "group_name": "Group 3: Professional Self-Initiatives, Tech Competitions, Innovation & Skilling",
        "min_required": 40,
        "max_capped": 60,
        "focus": "Technical expertise, coding hackathons, NPTEL/MOOC certifications, research and startups",
        "activities": [
            {"name": "12-Week NPTEL / SWAYAM Online Course (Elite / Gold)", "points": 50, "doc_req": "Official NPTEL Score Certificate with Proctored Exam Score"},
            {"name": "8-Week NPTEL / SWAYAM Course Certificate", "points": 35, "doc_req": "Official NPTEL Score Certificate"},
            {"name": "Hackathon Winner (National / State Level - 24 to 36 hr)", "points": 40, "doc_req": "Prize Certificate + Verified GitHub Project Link"},
            {"name": "Hackathon Participation (24-36 hr National/State)", "points": 15, "doc_req": "Participation Certificate + Code Repository Evidence"},
            {"name": "Paper Published in Scopus / IEEE Indexed Conference", "points": 35, "doc_req": "Conference Proceedings + Certificate of Presentation"},
            {"name": "Student Startup Founder / Registered LLP Company", "points": 60, "doc_req": "Ministry of Corporate Affairs / KSUM Registration Certificate"},
            {"name": "Active Professional Body Membership (IEEE, CSI, ACM, SAE)", "points": 10, "doc_req": "Valid Membership ID Card Copy for the Academic Year"},
            {"name": "Industrial Training / Internship (Min 2 Weeks) in Core Engineering", "points": 20, "doc_req": "Company Certificate with Attendance and Project Report"}
        ]
    }
]

# KTU 10-Mark Model Answer Blueprint Templates Across Branches
KTU_ANSWER_ARCHITECT = [
    {
        "id": "model-bankers",
        "subject": "Operating Systems (CST 206 - CSE/CN)",
        "question": "Explain Banker's Algorithm for Deadlock Avoidance with Safety and Resource Request algorithms.",
        "marks": 10,
        "blueprint": [
            {"section": "1. Definition & Core Premise", "recommended_time": "2 mins", "marks_allocated": 1.5, "content": "Define Banker's algorithm as a deadlock avoidance algorithm. Resources are granted ONLY if granting leads to a Safe State."},
            {"section": "2. Data Structures Required", "recommended_time": "3 mins", "marks_allocated": 2.0, "content": "Need[i][j] = Max[i][j] - Allocation[i][j]. Available[m], Max[n][m], Allocation[n][m]."},
            {"section": "3. Safety Algorithm Step-by-Step", "recommended_time": "5 mins", "marks_allocated": 3.5, "content": "Work = Available, Finish[i] = false. If Finish[i] == false and Need_i <= Work -> Work = Work + Allocation_i, Finish[i] = true."},
            {"section": "4. Resource-Request Algorithm", "recommended_time": "3 mins", "marks_allocated": 2.0, "content": "If Request_i <= Need_i and Request_i <= Available, pretentiously allocate and check safety."},
            {"section": "5. Limitations & Exam Tip", "recommended_time": "2 mins", "marks_allocated": 1.0, "content": "Requires prior knowledge of maximum resources. Always frame the Safe Sequence inside a neat box."}
        ]
    },
    {
        "id": "model-kmap",
        "subject": "Logic System Design (CST 203 / ECT 203 - ECE/EEE/CSE)",
        "question": "Minimize F(A, B, C, D) = Sigma m(0, 1, 2, 5, 8, 9, 10) + d(3, 11, 15) using 4-variable K-Map and draw the NAND logic diagram.",
        "marks": 10,
        "blueprint": [
            {"section": "1. K-Map Grid Setup & Gray Coding", "recommended_time": "3 mins", "marks_allocated": 2.0, "content": "Draw 4x4 matrix with Gray coded row labels (00, 01, 11, 10) and column labels (00, 01, 11, 10)."},
            {"section": "2. Plotting Minterms & Don't Cares", "recommended_time": "3 mins", "marks_allocated": 2.0, "content": "Place 1s at minterms and Xs at don't-cares."},
            {"section": "3. Grouping & Prime Implicants", "recommended_time": "5 mins", "marks_allocated": 3.0, "content": "Group Corner Quad m(0,2,8,10) -> B'D', Quad m(0,1,8,9) -> B'C'. Final: F = B' + A'C'D."},
            {"section": "4. Universal NAND Realization", "recommended_time": "4 mins", "marks_allocated": 3.0, "content": "Apply DeMorgan's theorem and draw two-level NAND circuit."}
        ]
    },
    {
        "id": "model-diesel",
        "subject": "Engineering Thermodynamics (MET 203 - MECH)",
        "question": "Derive the air standard thermal efficiency expression for Diesel cycle in terms of compression ratio (r) and cutoff ratio (r_c).",
        "marks": 10,
        "blueprint": [
            {"section": "1. P-v and T-s Diagrams", "recommended_time": "3 mins", "marks_allocated": 2.5, "content": "Draw P-v and T-s diagrams showing: 1-2 Isentropic compression, 2-3 Constant pressure heat addition, 3-4 Isentropic expansion, 4-1 Constant volume heat rejection."},
            {"section": "2. Heat Added & Heat Rejected Equations", "recommended_time": "4 mins", "marks_allocated": 2.5, "content": "Heat supplied Q_in = m * C_p * (T3 - T2). Heat rejected Q_out = m * C_v * (T4 - T1). Thermal efficiency eta = 1 - (Q_out / Q_in) = 1 - (1/gamma) * (T4 - T1) / (T3 - T2)."},
            {"section": "3. Temperature & Volume Ratio Relationships", "recommended_time": "5 mins", "marks_allocated": 4.0, "content": "Define compression ratio r = V1 / V2 and cutoff ratio r_c = V3 / V2. Express temperatures in terms of T1, r, and r_c to yield final formula: eta = 1 - (1 / r^(gamma - 1)) * ((r_c^gamma - 1) / (gamma * (r_c - 1)))."},
            {"section": "4. Significance & Exam Tip", "recommended_time": "2 mins", "marks_allocated": 1.0, "content": "State: For the same compression ratio, Otto cycle is more efficient than Diesel cycle. Always define gamma = C_p / C_v."}
        ]
    },
    {
        "id": "model-sfd",
        "subject": "Mechanics of Solids (CET 201 - CE / CN)",
        "question": "Draw Shear Force Diagram (SFD) and Bending Moment Diagram (BMD) for a simply supported beam of length L carrying a UDL of w kN/m over its entire span.",
        "marks": 10,
        "blueprint": [
            {"section": "1. Beam Schematic & Support Reactions", "recommended_time": "3 mins", "marks_allocated": 2.5, "content": "Draw beam AB with span L, pin support at A, roller support at B, and uniform distributed load w. Total downward load = w*L. By symmetry, reactions R_A = R_B = w*L / 2."},
            {"section": "2. Shear Force Equation & SFD", "recommended_time": "4 mins", "marks_allocated": 3.0, "content": "At distance x from A: F_x = R_A - w*x = (w*L/2) - w*x. Linear variation: at x=0, F = +wL/2; at x=L/2, F = 0; at x=L, F = -wL/2. Draw linear inclined SFD."},
            {"section": "3. Bending Moment Equation & Maximum Moment", "recommended_time": "5 mins", "marks_allocated": 3.5, "content": "Bending moment at section x: M_x = R_A * x - (w * x^2 / 2) = (w*L/2)*x - (w*x^2 / 2). Parabolic curve. Maximum bending moment occurs where shear force is zero (x = L/2): M_max = w * L^2 / 8."},
            {"section": "4. Exam Presentation Tip", "recommended_time": "2 mins", "marks_allocated": 1.0, "content": "Draw SFD directly below the beam schematic and BMD directly below the SFD with all peak values (wL/2 and wL^2/8) clearly marked."}
        ]
    }
]

# KTU 2024 Scheme Calculation Utilities
def calculate_ktu_cie(series1: float, series2: float, assignment: float, attendance_pct: float) -> Dict[str, Any]:
    """Computes Continuous Internal Evaluation (CIE) out of 50 marks according to KTU 2024 Scheme."""
    s1_clamped = min(max(series1, 0.0), 50.0)
    s2_clamped = min(max(series2, 0.0), 50.0)
    series_avg_50 = (s1_clamped + s2_clamped) / 2.0
    series_contribution = (series_avg_50 / 50.0) * 25.0

    assign_clamped = min(max(assignment, 0.0), 15.0)

    att_clamped = min(max(attendance_pct, 0.0), 100.0)
    if att_clamped >= 90.0:
        att_marks = 10.0
    elif att_clamped >= 85.0:
        att_marks = 8.0
    elif att_clamped >= 80.0:
        att_marks = 6.0
    elif att_clamped >= 75.0:
        att_marks = 4.0
    else:
        att_marks = 0.0

    total_cie = round(series_contribution + assign_clamped + att_marks, 1)
    attendance_eligible = att_clamped >= 75.0
    
    grade_targets = []
    for g in KTU_REGULATIONS["grade_scale"]:
        if g["grade"] == "F":
            continue
        req_total_marks = (g["min_aggregate_pct"] / 100.0) * 150.0
        req_esa = req_total_marks - total_cie
        final_req_esa = max(40.0, round(req_esa, 1))
        
        achievable = (final_req_esa <= 100.0)
        grade_targets.append({
            "grade": g["grade"],
            "grade_point": g["grade_point"],
            "target_pct": g["min_aggregate_pct"],
            "min_esa_required": final_req_esa if achievable else "Not Achievable",
            "status": "Achievable" if achievable else "Out of reach with current CIE",
            "desc": g["desc"]
        })

    min_pass_esa = max(40.0, round((45.0 / 100.0 * 150.0) - total_cie, 1))
    supply_risk = "LOW"
    risk_advice = "Safe position. Focus on scoring 45+ in ESA for B+/A grade."
    if min_pass_esa > 80.0:
        supply_risk = "HIGH RISK"
        risk_advice = f"Warning! You need at least {min_pass_esa}/100 in the University Exam to clear the paper. Must prepare Modules 1, 2, and 3 thoroughly!"
    elif min_pass_esa > 55.0:
        supply_risk = "MODERATE RISK"
        risk_advice = f"You need {min_pass_esa}/100 in the University Exam to avoid supplementary. Focus on high-yield 10-mark questions."

    return {
        "cie_total": total_cie,
        "cie_breakdown": {
            "series_marks": round(series_contribution, 1),
            "assignment_marks": assign_clamped,
            "attendance_marks": att_marks,
            "attendance_pct": att_clamped,
            "attendance_eligible": attendance_eligible
        },
        "supply_risk": supply_risk,
        "risk_advice": risk_advice,
        "min_esa_to_pass": min_pass_esa if min_pass_esa <= 100 else "Impossible (CIE too low)",
        "grade_targets": grade_targets
    }

# CPU Scheduling Simulation Runner
def run_cpu_scheduling(processes: List[Dict[str, Any]], quantum: int = 2) -> Dict[str, Any]:
    fcfs_procs = sorted([dict(p) for p in processes], key=lambda x: x["arrival"])
    cur_time = 0
    gantt_fcfs = []
    for p in fcfs_procs:
        if cur_time < p["arrival"]:
            cur_time = p["arrival"]
        start_t = cur_time
        cur_time += p["burst"]
        end_t = cur_time
        p["completion"] = end_t
        p["turnaround"] = p["completion"] - p["arrival"]
        p["waiting"] = p["turnaround"] - p["burst"]
        gantt_fcfs.append({"process": p["name"], "start": start_t, "end": end_t, "duration": p["burst"]})
        
    avg_wt_fcfs = round(sum(p["waiting"] for p in fcfs_procs) / len(fcfs_procs), 2)
    avg_tat_fcfs = round(sum(p["turnaround"] for p in fcfs_procs) / len(fcfs_procs), 2)

    rr_procs = sorted([dict(p, remaining=p["burst"]) for p in processes], key=lambda x: x["arrival"])
    queue = []
    gantt_rr = []
    t = 0
    completed = 0
    n = len(rr_procs)
    visited = set()
    
    for p in rr_procs:
        if p["arrival"] <= t and p["name"] not in visited:
            queue.append(p)
            visited.add(p["name"])
            
    while completed < n:
        if not queue:
            remaining = [p for p in rr_procs if p["name"] not in visited]
            if remaining:
                next_p = min(remaining, key=lambda x: x["arrival"])
                t = next_p["arrival"]
                queue.append(next_p)
                visited.add(next_p["name"])
            else:
                break
                
        curr = queue.pop(0)
        exec_t = min(quantum, curr["remaining"])
        start_t = t
        t += exec_t
        curr["remaining"] -= exec_t
        gantt_rr.append({"process": curr["name"], "start": start_t, "end": t, "duration": exec_t})
        
        for p in rr_procs:
            if p["arrival"] <= t and p["name"] not in visited:
                queue.append(p)
                visited.add(p["name"])
                
        if curr["remaining"] > 0:
            queue.append(curr)
        else:
            completed += 1
            curr["completion"] = t
            curr["turnaround"] = curr["completion"] - curr["arrival"]
            curr["waiting"] = curr["turnaround"] - curr["burst"]

    avg_wt_rr = round(sum(p["waiting"] for p in rr_procs) / n, 2)
    avg_tat_rr = round(sum(p["turnaround"] for p in rr_procs) / n, 2)

    return {
        "status": "success",
        "fcfs": {"gantt": gantt_fcfs, "avg_waiting": avg_wt_fcfs, "avg_turnaround": avg_tat_fcfs, "processes": fcfs_procs},
        "round_robin": {"gantt": gantt_rr, "quantum": quantum, "avg_waiting": avg_wt_rr, "avg_turnaround": avg_tat_rr, "processes": rr_procs}
    }
