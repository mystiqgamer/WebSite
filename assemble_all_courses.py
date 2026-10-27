"""
Assembles all courses from Common S1/S2, CSE, ECE, EEE, MECH, CE/CN
and exports KTU_COURSES into courses_data.py.
"""
from typing import List, Dict, Any
from build_cse import get_cse_courses
from build_ece import get_ece_courses
from build_eee import get_eee_courses
from build_mech import get_mech_courses
from build_ce_cn import get_ce_cn_courses
from generate_all_courses import build as build_base

def assemble():
    # 1. Base Common S1/S2 courses
    _, add_c = build_base()
    
    # We can fetch the raw common courses by running build_base logic
    from build_courses_catalog import courses as common_courses
    
    all_courses: List[Dict[str, Any]] = []
    
    # Track added IDs to avoid duplicates
    seen_ids = set()
    
    # Add common
    for c in common_courses:
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])
            
    # Add CSE
    for c in get_cse_courses():
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])

    # Add ECE
    for c in get_ece_courses():
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])

    # Add EEE
    for c in get_eee_courses():
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])

    # Add MECH
    for c in get_mech_courses():
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])

    # Add CE / CN
    for c in get_ce_cn_courses():
        if c["id"] not in seen_ids:
            all_courses.append(c)
            seen_ids.add(c["id"])

    print(f"Total Unique Courses Assembled: {len(all_courses)}")
    
    # Verify branches and semesters
    by_branch = {}
    by_sem = {}
    total_mods = 0
    total_pyqs = 0
    
    for c in all_courses:
        b = c["branch_id"]
        s = c["semester"]
        by_branch[b] = by_branch.get(b, 0) + 1
        by_sem[s] = by_sem.get(s, 0) + 1
        total_mods += len(c.get("modules", []))
        for m in c.get("modules", []):
            total_pyqs += len(m.get("high_yield_pyqs", []))

    print("Courses per branch:", by_branch)
    print("Courses per semester:", by_sem)
    print(f"Total Modules: {total_mods}")
    print(f"Total High-Yield PYQs: {total_pyqs}")
    
    # Write courses_data.py
    with open("courses_data.py", "w", encoding="utf-8") as f:
        f.write('"""\n')
        f.write('KTU ScholarOS - Comprehensive Course Database (B.Tech 2024 Scheme)\n')
        f.write('All semesters S1 to S8 across 5 major branches (CSE, ECE, EEE, MECH, CE/CN) and Common Foundation.\n')
        f.write('"""\n\n')
        f.write('from typing import List, Dict, Any\n\n')
        f.write('KTU_COURSES: List[Dict[str, Any]] = [\n')
        
        for c in all_courses:
            f.write('    {\n')
            f.write(f'        "id": {repr(c["id"])},\n')
            f.write(f'        "code": {repr(c["code"])},\n')
            f.write(f'        "title": {repr(c["title"])},\n')
            f.write(f'        "credits": {c["credits"]},\n')
            f.write(f'        "semester": {repr(c["semester"])},\n')
            f.write(f'        "branch": {repr(c["branch"])},\n')
            f.write(f'        "branch_id": {repr(c["branch_id"])},\n')
            f.write(f'        "category": {repr(c["category"])},\n')
            f.write('        "modules": [\n')
            for m in c["modules"]:
                f.write('            {\n')
                f.write(f'                "module_no": {m["module_no"]},\n')
                f.write(f'                "title": {repr(m["title"])},\n')
                f.write(f'                "syllabus": {repr(m["syllabus"])},\n')
                f.write(f'                "weightage_marks": {m.get("weightage_marks", 15)},\n')
                f.write('                "high_yield_pyqs": [\n')
                for q in m.get("high_yield_pyqs", []):
                    f.write(f'                    {{"q": {repr(q["q"])}, "marks": {q["marks"]}, "frequency": {repr(q["frequency"])}}},\n')
                f.write('                ]\n')
                f.write('            },\n')
            f.write('        ]\n')
            f.write('    },\n')
            
        f.write(']\n')

    print("Successfully generated courses_data.py!")

if __name__ == "__main__":
    assemble()
